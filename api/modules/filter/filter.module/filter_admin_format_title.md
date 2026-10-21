# filter_admin_format_title()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 341–343 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L341-L343)
- **Module/theme:** filter

## Signature

```php
function filter_admin_format_title($format)
```

## Documentation

```text
Displays a text format form title.

@param object $format
  A format object.

@return string
  The name of the format.

@see filter_menu()
```

## Code

```php
function filter_admin_format_title($format) {
  return $format->name;
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._
