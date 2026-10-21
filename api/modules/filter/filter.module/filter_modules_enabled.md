# filter_modules_enabled()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 390–394 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L390-L394)
- **Module/theme:** filter
- **Implements:** [hook_modules_enabled()](../../system/system.api.php/hook_modules_enabled.md)

## Signature

```php
function filter_modules_enabled($modules)
```

## Documentation

```text
Implements hook_modules_enabled().
```

## Code

```php
function filter_modules_enabled($modules) {
  // Reset the static cache of module-provided filters, in case any of the
  // newly enabled modules defines a new filter or alters existing ones.
  drupal_static_reset('filter_get_filters');
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._
