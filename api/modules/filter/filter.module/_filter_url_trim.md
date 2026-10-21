# _filter_url_trim()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 1682–1694 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L1682-L1694)
- **Module/theme:** filter
- **Topics:** [standard_filters](../../../topics/standard_filters.md)

## Signature

```php
function _filter_url_trim($text, $length = NULL)
```

## Documentation

```text
Shortens long URLs to http://www.example.com/long/url...
```

## Code

```php
function _filter_url_trim($text, $length = NULL) {
  static $_length;
  if ($length !== NULL) {
    $_length = $length;
  }

  // Use +3 for '...' string length.
  if ($_length && strlen((string) $text) > $_length + 3) {
    $text = substr($text, 0, $_length) . '...';
  }

  return $text;
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._
