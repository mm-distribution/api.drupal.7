# _filter_disable_format_access()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 155–158 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L155-L158)
- **Module/theme:** filter

## Signature

```php
function _filter_disable_format_access($format)
```

## Documentation

```text
Access callback: Checks access for disabling text formats.

@param $format
  A text format object.

@return
  TRUE if the text format can be disabled by the current user, FALSE
  otherwise.

@see filter_menu()
```

## Code

```php
function _filter_disable_format_access($format) {
  // The fallback format can never be disabled.
  return user_access('administer filters') && ($format->format != filter_fallback_format());
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._
