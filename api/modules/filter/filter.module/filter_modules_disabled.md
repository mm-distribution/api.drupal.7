# filter_modules_disabled()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 399–403 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L399-L403)
- **Module/theme:** filter
- **Implements:** [hook_modules_disabled()](../../system/system.api.php/hook_modules_disabled.md)

## Signature

```php
function filter_modules_disabled($modules)
```

## Documentation

```text
Implements hook_modules_disabled().
```

## Code

```php
function filter_modules_disabled($modules) {
  // Reset the static cache of module-provided filters, in case any of the
  // newly disabled modules defined or altered any filters.
  drupal_static_reset('filter_get_filters');
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._
