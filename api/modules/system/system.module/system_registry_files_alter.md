# system_registry_files_alter()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 4146–4149 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L4146-L4149)
- **Module/theme:** system

## Signature

```php
function system_registry_files_alter(&$files, $modules)
```

## Documentation

```text
Implements hook_registry_files_alter
```

## Code

```php
function system_registry_files_alter(&$files, $modules) {
  // Database drivers that use DatabaseStatementPrefetch must include this file.
  unset($files['includes/database/prefetch.inc']);
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
