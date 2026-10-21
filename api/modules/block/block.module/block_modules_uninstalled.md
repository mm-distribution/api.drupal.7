# block_modules_uninstalled()

- **Type:** Function
- **File:** [`modules/block/block.module`](_file.md), lines 1105–1112 · [local source](../../../../source/modules/block/block.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module#L1105-L1112)
- **Module/theme:** block
- **Implements:** [hook_modules_uninstalled()](../../system/system.api.php/hook_modules_uninstalled.md)

## Signature

```php
function block_modules_uninstalled($modules)
```

## Documentation

```text
Implements hook_modules_uninstalled().

Cleans up {block} and {block_role} tables from modules' blocks.
```

## Code

```php
function block_modules_uninstalled($modules) {
  db_delete('block')
    ->condition('module', $modules, 'IN')
    ->execute();
  db_delete('block_role')
    ->condition('module', $modules, 'IN')
    ->execute();
}
```

---
_Drupal 7.103 · [modules/block/block.module](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module) · Licensed GPL-2.0-or-later (see LICENSE)._
