# filter_permission_name()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 380–385 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L380-L385)
- **Module/theme:** filter

## Signature

```php
function filter_permission_name($format)
```

## Documentation

```text
Returns the machine-readable permission name for a provided text format.

@param $format
  An object representing a text format.

@return
  The machine-readable permission name, or FALSE if the provided text format
  is malformed or is the fallback format (which is available to all users).
```

## Code

```php
function filter_permission_name($format) {
  if (isset($format->format) && $format->format != filter_fallback_format()) {
    return 'use text format ' . $format->format;
  }
  return FALSE;
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._
