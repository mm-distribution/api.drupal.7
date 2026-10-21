# drupal_page_set_cache()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 5465–5507 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L5465-L5507)

## Signature

```php
function drupal_page_set_cache()
```

## Documentation

```text
Stores the current page in the cache.

If page_compression is enabled, a gzipped version of the page is stored in
the cache to avoid compressing the output on each request. The cache entry
is unzipped in the relatively rare event that the page is requested by a
client without gzip support.

Page compression requires the PHP zlib extension
(http://php.net/manual/ref.zlib.php).

@see drupal_page_header()
```

## Code

```php
function drupal_page_set_cache() {
  global $base_root;

  if (drupal_page_is_cacheable()) {

    // Check whether the current page might be compressed.
    $page_compressed = variable_get('page_compression', TRUE) && extension_loaded('zlib');

    $cache = (object) array(
      'cid' => $base_root . request_uri(),
      'data' => array(
        'path' => $_GET['q'],
        'body' => ob_get_clean(),
        'title' => drupal_get_title(),
        'headers' => array(),
        // We need to store whether page was compressed or not,
        // because by the time it is read, the configuration might change.
        'page_compressed' => $page_compressed,
      ),
      'expire' => CACHE_TEMPORARY,
      'created' => REQUEST_TIME,
    );

    // Restore preferred header names based on the lower-case names returned
    // by drupal_get_http_header().
    $header_names = _drupal_set_preferred_header_name();
    foreach (drupal_get_http_header() as $name_lower => $value) {
      $cache->data['headers'][$header_names[$name_lower]] = $value;
      if ($name_lower == 'expires') {
        // Use the actual timestamp from an Expires header if available.
        $cache->expire = strtotime($value);
      }
    }

    if ($cache->data['body']) {
      if ($page_compressed) {
        $cache->data['body'] = gzencode($cache->data['body'], 9, FORCE_GZIP);
      }
      cache_set($cache->cid, $cache->data, 'cache_page', $cache->expire);
    }
    return $cache;
  }
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
