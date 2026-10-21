# forum_node_delete()

- **Type:** Function
- **File:** [`modules/forum/forum.module`](_file.md), lines 414–423 · [local source](../../../../source/modules/forum/forum.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module#L414-L423)
- **Module/theme:** forum
- **Implements:** [hook_node_delete()](../../node/node.api.php/hook_node_delete.md)

## Signature

```php
function forum_node_delete($node)
```

## Documentation

```text
Implements hook_node_delete().
```

## Code

```php
function forum_node_delete($node) {
  if (_forum_node_check_node_type($node)) {
    db_delete('forum')
      ->condition('nid', $node->nid)
      ->execute();
    db_delete('forum_index')
      ->condition('nid', $node->nid)
      ->execute();
  }
}
```

---
_Drupal 7.103 · [modules/forum/forum.module](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module) · Licensed GPL-2.0-or-later (see LICENSE)._
