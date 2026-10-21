# _install_module_batch()

- **Type:** Function
- **File:** [`includes/install.core.inc`](_file.md), lines 1615–1623 · [local source](../../../source/includes/install.core.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc#L1615-L1623)

## Signature

```php
function _install_module_batch($module, $module_name, &$context)
```

## Documentation

```text
Implements callback_batch_operation().

Performs batch installation of modules.
```

## Code

```php
function _install_module_batch($module, $module_name, &$context) {
  // Install and enable the module right away, so that the module will be
  // loaded by drupal_bootstrap in subsequent batch requests, and other
  // modules possibly depending on it can safely perform their installation
  // steps.
  module_enable(array($module), FALSE);
  $context['results'][] = $module;
  $context['message'] = st('Installed %module module.', array('%module' => $module_name));
}
```

---
_Drupal 7.103 · [includes/install.core.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
