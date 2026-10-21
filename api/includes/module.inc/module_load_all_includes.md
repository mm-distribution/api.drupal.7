# module_load_all_includes()

- **Type:** Function
- **File:** [`includes/module.inc`](_file.md), lines 356–361 · [local source](../../../source/includes/module.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/module.inc#L356-L361)

## Signature

```php
function module_load_all_includes($type, $name = NULL)
```

## Documentation

```text
Loads an include file for each module enabled in the {system} table.
```

## Code

```php
function module_load_all_includes($type, $name = NULL) {
  $modules = module_list();
  foreach ($modules as $module) {
    module_load_include($type, $module, $name);
  }
}
```

---
_Drupal 7.103 · [includes/module.inc](https://github.com/drupal/drupal/blob/7.103/includes/module.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
