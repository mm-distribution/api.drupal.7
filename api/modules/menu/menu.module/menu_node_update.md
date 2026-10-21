# menu_node_update()

- **Type:** Function
- **File:** [`modules/menu/menu.module`](_file.md), lines 542–544 · [local source](../../../../source/modules/menu/menu.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module#L542-L544)
- **Module/theme:** menu
- **Implements:** [hook_node_update()](../../node/node.api.php/hook_node_update.md)

## Signature

```php
function menu_node_update($node)
```

## Documentation

```text
Implements hook_node_update().
```

## Code

```php
function menu_node_update($node) {
  menu_node_save($node);
}
```

---
_Drupal 7.103 · [modules/menu/menu.module](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module) · Licensed GPL-2.0-or-later (see LICENSE)._
