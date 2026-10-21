# menu_node_delete()

- **Type:** Function
- **File:** [`modules/menu/menu.module`](_file.md), lines 578–584 · [local source](../../../../source/modules/menu/menu.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module#L578-L584)
- **Module/theme:** menu
- **Implements:** [hook_node_delete()](../../node/node.api.php/hook_node_delete.md)

## Signature

```php
function menu_node_delete($node)
```

## Documentation

```text
Implements hook_node_delete().
```

## Code

```php
function menu_node_delete($node) {
  // Delete all menu module links that point to this node.
  $result = db_query("SELECT mlid FROM {menu_links} WHERE link_path = :path AND module = 'menu'", array(':path' => 'node/' . $node->nid), array('fetch' => PDO::FETCH_ASSOC));
  foreach ($result as $m) {
    menu_link_delete($m['mlid']);
  }
}
```

---
_Drupal 7.103 · [modules/menu/menu.module](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module) · Licensed GPL-2.0-or-later (see LICENSE)._
