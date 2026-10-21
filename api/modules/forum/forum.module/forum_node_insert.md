# forum_node_insert()

- **Type:** Function
- **File:** [`modules/forum/forum.module`](_file.md), lines 397–409 · [local source](../../../../source/modules/forum/forum.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module#L397-L409)
- **Module/theme:** forum
- **Implements:** [hook_node_insert()](../../node/node.api.php/hook_node_insert.md)

## Signature

```php
function forum_node_insert($node)
```

## Documentation

```text
Implements hook_node_insert().
```

## Code

```php
function forum_node_insert($node) {
  if (_forum_node_check_node_type($node)) {
    if (!empty($node->forum_tid)) {
      $nid = db_insert('forum')
        ->fields(array(
          'tid' => $node->forum_tid,
          'vid' => $node->vid,
          'nid' => $node->nid,
        ))
        ->execute();
    }
  }
}
```

---
_Drupal 7.103 · [modules/forum/forum.module](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module) · Licensed GPL-2.0-or-later (see LICENSE)._
