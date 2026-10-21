# module_load_install()

- **Type:** Function
- **File:** [`includes/module.inc`](_file.md), lines 293–298 · [local source](../../../source/includes/module.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/module.inc#L293-L298)

## Signature

```php
function module_load_install($module)
```

## Documentation

```text
Loads a module's installation hooks.

@param $module
  The name of the module (without the .module extension).

@return
  The name of the module's install file, if successful; FALSE otherwise.
```

## Code

```php
function module_load_install($module) {
  // Make sure the installation API is available
  include_once DRUPAL_ROOT . '/includes/install.inc';

  return module_load_include('install', $module);
}
```

---
_Drupal 7.103 · [includes/module.inc](https://github.com/drupal/drupal/blob/7.103/includes/module.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
