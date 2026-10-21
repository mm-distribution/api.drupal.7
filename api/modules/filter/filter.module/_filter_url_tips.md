# _filter_url_tips()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 1703–1705 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L1703-L1705)
- **Module/theme:** filter
- **Topics:** [standard_filters](../../../topics/standard_filters.md)

## Signature

```php
function _filter_url_tips($filter, $format, $long = FALSE)
```

## Documentation

```text
Implements callback_filter_tips().

Provides help for the URL filter.

@see filter_filter_info()
```

## Code

```php
function _filter_url_tips($filter, $format, $long = FALSE) {
  return t('Web page addresses and e-mail addresses turn into links automatically.');
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._
