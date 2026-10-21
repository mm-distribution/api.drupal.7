# drupal_http_header_attributes()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 2468–2476 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L2468-L2476)

## Signature

```php
function drupal_http_header_attributes(array $attributes = array())
```

## Documentation

```text
Formats an attribute string for an HTTP header.

@param $attributes
  An associative array of attributes such as 'rel'.

@return
  A ; separated string ready for insertion in a HTTP header. No escaping is
  performed for HTML entities, so this string is not safe to be printed.

@see drupal_add_http_header()
```

## Code

```php
function drupal_http_header_attributes(array $attributes = array()) {
  foreach ($attributes as $attribute => &$data) {
    if (is_array($data)) {
      $data = implode(' ', $data);
    }
    $data = $attribute . '="' . $data . '"';
  }
  return $attributes ? ' ' . implode('; ', $attributes) : '';
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
