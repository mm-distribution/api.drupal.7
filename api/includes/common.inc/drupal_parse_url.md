# drupal_parse_url()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 575–622 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L575-L622)
- **Topics:** [http_handling](../../topics/http_handling.md), [php_wrappers](../../topics/php_wrappers.md)

## Signature

```php
function drupal_parse_url($url)
```

## Documentation

```text
Parses a URL string into its path, query, and fragment components.

This function splits both internal paths like @code node?b=c#d @endcode and
external URLs like @code https://example.com/a?b=c#d @endcode into their
component parts. See
@link http://tools.ietf.org/html/rfc3986#section-3 RFC 3986 @endlink for an
explanation of what the component parts are.

Note that, unlike the RFC, when passed an external URL, this function
groups the scheme, authority, and path together into the path component.

@param string $url
  The internal path or external URL string to parse.

@return array
  An associative array containing:
  - path: The path component of $url. If $url is an external URL, this
    includes the scheme, authority, and path.
  - query: An array of query parameters from $url, if they exist.
  - fragment: The fragment component from $url, if it exists.

@see drupal_goto()
@see l()
@see url()
@see http://tools.ietf.org/html/rfc3986

@ingroup php_wrappers
```

## Code

```php
function drupal_parse_url($url) {
  $options = array(
    'path' => NULL,
    'query' => array(),
    'fragment' => '',
  );

  // External URLs: not using parse_url() here, so we do not have to rebuild
  // the scheme, host, and path without having any use for it.
  if (strpos($url, '://') !== FALSE) {
    // Split off everything before the query string into 'path'.
    $parts = explode('?', $url);
    $options['path'] = $parts[0];
    // If there is a query string, transform it into keyed query parameters.
    if (isset($parts[1])) {
      $query_parts = explode('#', $parts[1]);
      parse_str($query_parts[0], $options['query']);
      // Take over the fragment, if there is any.
      if (isset($query_parts[1])) {
        $options['fragment'] = $query_parts[1];
      }
    }
  }
  // Internal URLs.
  else {
    // parse_url() does not support relative URLs, so make it absolute. E.g. the
    // relative URL "foo/bar:1" isn't properly parsed.
    $parts = parse_url('http://example.com/' . $url);
    // Strip the leading slash that was just added.
    $options['path'] = substr($parts['path'], 1);
    if (isset($parts['query'])) {
      parse_str($parts['query'], $options['query']);
    }
    if (isset($parts['fragment'])) {
      $options['fragment'] = $parts['fragment'];
    }
  }
  // The 'q' parameter contains the path of the current page if clean URLs are
  // disabled. It overrides the 'path' of the URL when present, even if clean
  // URLs are enabled, due to how Apache rewriting rules work. The path
  // parameter must be a string.
  if (isset($options['query']['q']) && is_string($options['query']['q'])) {
    $options['path'] = $options['query']['q'];
    unset($options['query']['q']);
  }

  return $options;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
