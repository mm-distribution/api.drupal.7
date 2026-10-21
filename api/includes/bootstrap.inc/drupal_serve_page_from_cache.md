# drupal_serve_page_from_cache()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 1606–1696 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L1606-L1696)

## Signature

```php
function drupal_serve_page_from_cache(stdClass $cache)
```

## Documentation

```text
Sets HTTP headers in preparation for a cached page response.

The headers allow as much as possible in proxies and browsers without any
particular knowledge about the pages. Modules can override these headers
using drupal_add_http_header().

If the request is conditional (using If-Modified-Since and If-None-Match),
and the conditions match those currently in the cache, a 304 Not Modified
response is sent.
```

## Code

```php
function drupal_serve_page_from_cache(stdClass $cache) {
  // Negotiate whether to use compression.
  $page_compression = !empty($cache->data['page_compressed']) && !empty($cache->data['body']);
  $return_compressed = $page_compression && isset($_SERVER['HTTP_ACCEPT_ENCODING']) && strpos($_SERVER['HTTP_ACCEPT_ENCODING'], 'gzip') !== FALSE;

  // Get headers set in hook_boot(). Keys are lower-case.
  $hook_boot_headers = drupal_get_http_header();

  // Headers generated in this function, that may be replaced or unset using
  // drupal_add_http_headers(). Keys are mixed-case.
  $default_headers = array();

  foreach ($cache->data['headers'] as $name => $value) {
    // In the case of a 304 response, certain headers must be sent, and the
    // remaining may not (see RFC 2616, section 10.3.5). Do not override
    // headers set in hook_boot().
    $name_lower = strtolower($name);
    if (in_array($name_lower, array('content-location', 'expires', 'cache-control', 'vary')) && !isset($hook_boot_headers[$name_lower])) {
      drupal_add_http_header($name, $value);
      unset($cache->data['headers'][$name]);
    }
  }

  // If the client sent a session cookie, a cached copy will only be served
  // to that one particular client due to Vary: Cookie. Thus, do not set
  // max-age > 0, allowing the page to be cached by external proxies, when a
  // session cookie is present unless the Vary header has been replaced or
  // unset in hook_boot().
  $max_age = !isset($_COOKIE[session_name()]) || isset($hook_boot_headers['vary']) ? variable_get('page_cache_maximum_age', 0) : 0;
  $default_headers['Cache-Control'] = 'public, max-age=' . $max_age;

  // Entity tag should change if the output changes.
  $etag = '"' . $cache->created . '-' . intval($return_compressed) . '"';
  header('Etag: ' . $etag);

  // See if the client has provided the required HTTP headers.
  $if_modified_since = isset($_SERVER['HTTP_IF_MODIFIED_SINCE']) ? strtotime($_SERVER['HTTP_IF_MODIFIED_SINCE']) : FALSE;
  $if_none_match = isset($_SERVER['HTTP_IF_NONE_MATCH']) ? stripslashes($_SERVER['HTTP_IF_NONE_MATCH']) : FALSE;

  if ($if_modified_since && $if_none_match
      && $if_none_match == $etag // etag must match
      && $if_modified_since == $cache->created) {  // if-modified-since must match
    header($_SERVER['SERVER_PROTOCOL'] . ' 304 Not Modified');
    drupal_send_headers($default_headers);
    return;
  }

  // Send the remaining headers.
  foreach ($cache->data['headers'] as $name => $value) {
    drupal_add_http_header($name, $value);
  }

  $default_headers['Last-Modified'] = gmdate(DATE_RFC7231, $cache->created);

  // HTTP/1.0 proxies does not support the Vary header, so prevent any caching
  // by sending an Expires date in the past. HTTP/1.1 clients ignores the
  // Expires header if a Cache-Control: max-age= directive is specified (see RFC
  // 2616, section 14.9.3).
  $default_headers['Expires'] = 'Sun, 19 Nov 1978 05:00:00 GMT';

  drupal_send_headers($default_headers);

  // Allow HTTP proxies to cache pages for anonymous users without a session
  // cookie. The Vary header is used to indicates the set of request-header
  // fields that fully determines whether a cache is permitted to use the
  // response to reply to a subsequent request for a given URL without
  // revalidation. If a Vary header has been set in hook_boot(), it is assumed
  // that the module knows how to cache the page.
  if (!isset($hook_boot_headers['vary']) && !variable_get('omit_vary_cookie')) {
    header('Vary: Cookie');
  }

  if ($page_compression) {
    header('Vary: Accept-Encoding', FALSE);
    // If page_compression is enabled, the cache contains gzipped data.
    if ($return_compressed) {
      // $cache->data['body'] is already gzip'ed, so make sure
      // zlib.output_compression does not compress it once more.
      ini_set('zlib.output_compression', '0');
      header('Content-Encoding: gzip');
    }
    else {
      // The client does not support compression, so unzip the data in the
      // cache. Strip the gzip header and run uncompress.
      $cache->data['body'] = gzinflate(substr(substr($cache->data['body'], 10), 0, -8));
    }
  }

  // Print the page.
  print $cache->data['body'];
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
