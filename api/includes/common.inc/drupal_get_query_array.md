# drupal_get_query_array()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 457–466 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L457-L466)
- **Topics:** [http_handling](../../topics/http_handling.md)

## Signature

```php
function drupal_get_query_array($query)
```

## Documentation

```text
Splits a URL-encoded query string into an array.

@param $query
  The query string to split.

@return
  An array of URL decoded couples $param_name => $value.
```

## Code

```php
function drupal_get_query_array($query) {
  $result = array();
  if (!empty($query)) {
    foreach (explode('&', $query) as $param) {
      $param = explode('=', $param, 2);
      $result[$param[0]] = isset($param[1]) ? rawurldecode($param[1]) : '';
    }
  }
  return $result;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
