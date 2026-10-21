# drupal_http_build_query()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 486–507 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L486-L507)
- **Topics:** [http_handling](../../topics/http_handling.md), [php_wrappers](../../topics/php_wrappers.md)

## Signature

```php
function drupal_http_build_query(array $query, $parent = '')
```

## Documentation

```text
Parses an array into a valid, rawurlencoded query string.

This differs from http_build_query() as we need to rawurlencode() (instead of
urlencode()) all query parameters.

@param $query
  The query parameter array to be processed, e.g. $_GET.
@param $parent
  Internal use only. Used to build the $query array key for nested items.

@return
  A rawurlencoded string which can be used as or appended to the URL query
  string.

@see drupal_get_query_parameters()
@ingroup php_wrappers
```

## Code

```php
function drupal_http_build_query(array $query, $parent = '') {
  $params = array();

  foreach ($query as $key => $value) {
    $key = $parent ? $parent . rawurlencode('[' . $key . ']') : rawurlencode($key);

    // Recurse into children.
    if (is_array($value)) {
      $params[] = drupal_http_build_query($value, $key);
    }
    // If a query parameter value is NULL, only append its key.
    elseif (!isset($value)) {
      $params[] = $key;
    }
    else {
      // For better readability of paths in query strings, we decode slashes.
      $params[] = $key . '=' . str_replace('%2F', '/', rawurlencode($value));
    }
  }

  return implode('&', $params);
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
