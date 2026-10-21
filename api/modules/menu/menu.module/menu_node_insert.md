# menu_node_insert()

- **Type:** Function
- **File:** [`modules/menu/menu.module`](_file.md), lines 535–537 · [local source](../../../../source/modules/menu/menu.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module#L535-L537)
- **Module/theme:** menu
- **Implements:** [hook_node_insert()](../../node/node.api.php/hook_node_insert.md)

## Signature

```php
function menu_node_insert($node)
```

## Documentation

```text
Implements hook_node_insert().
```

## Code

```php
function menu_node_insert($node) {
  menu_node_save($node);
}
```

---
_Drupal 7.103 · [modules/menu/menu.module](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module) · Licensed GPL-2.0-or-later (see LICENSE)._
