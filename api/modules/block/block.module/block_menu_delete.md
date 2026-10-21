# block_menu_delete()

- **Type:** Function
- **File:** [`modules/block/block.module`](_file.md), lines 1062–1071 · [local source](../../../../source/modules/block/block.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module#L1062-L1071)
- **Module/theme:** block
- **Implements:** [hook_menu_delete()](../../menu/menu.api.php/hook_menu_delete.md)

## Signature

```php
function block_menu_delete($menu)
```

## Documentation

```text
Implements hook_menu_delete().
```

## Code

```php
function block_menu_delete($menu) {
  db_delete('block')
    ->condition('module', 'menu')
    ->condition('delta', $menu['menu_name'])
    ->execute();
  db_delete('block_role')
    ->condition('module', 'menu')
    ->condition('delta', $menu['menu_name'])
    ->execute();
}
```

---
_Drupal 7.103 · [modules/block/block.module](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module) · Licensed GPL-2.0-or-later (see LICENSE)._
