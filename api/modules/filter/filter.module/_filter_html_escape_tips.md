# _filter_html_escape_tips()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 1817–1819 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L1817-L1819)
- **Module/theme:** filter
- **Topics:** [standard_filters](../../../topics/standard_filters.md)

## Signature

```php
function _filter_html_escape_tips($filter, $format, $long = FALSE)
```

## Documentation

```text
Implements callback_filter_tips().

Provides help for the HTML escaping filter.

@see filter_filter_info()
```

## Code

```php
function _filter_html_escape_tips($filter, $format, $long = FALSE) {
  return t('No HTML tags allowed.');
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._
