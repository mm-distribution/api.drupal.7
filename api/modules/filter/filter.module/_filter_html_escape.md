# _filter_html_escape()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 1806–1808 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L1806-L1808)
- **Module/theme:** filter
- **Topics:** [standard_filters](../../../topics/standard_filters.md)

## Signature

```php
function _filter_html_escape($text)
```

## Documentation

```text
Implements callback_filter_process().

Escapes all HTML tags, so they will be visible instead of being effective.
```

## Code

```php
function _filter_html_escape($text) {
  return trim(check_plain($text));
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._
