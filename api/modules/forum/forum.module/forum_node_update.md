# forum_node_update()

- **Type:** Function
- **File:** [`modules/forum/forum.module`](_file.md), lines 349–392 · [local source](../../../../source/modules/forum/forum.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module#L349-L392)
- **Module/theme:** forum
- **Implements:** [hook_node_update()](../../node/node.api.php/hook_node_update.md)

## Signature

```php
function forum_node_update($node)
```

## Documentation

```text
Implements hook_node_update().
```

## Code

```php
function forum_node_update($node) {
  if (_forum_node_check_node_type($node)) {
    if (empty($node->revision) && db_query('SELECT tid FROM {forum} WHERE nid=:nid', array(':nid' => $node->nid))->fetchField()) {
      if (!empty($node->forum_tid)) {
        db_update('forum')
          ->fields(array('tid' => $node->forum_tid))
          ->condition('vid', $node->vid)
          ->execute();
      }
      // The node is removed from the forum.
      else {
        db_delete('forum')
          ->condition('nid', $node->nid)
          ->execute();
      }
    }
    else {
      if (!empty($node->forum_tid)) {
        db_insert('forum')
          ->fields(array(
            'tid' => $node->forum_tid,
            'vid' => $node->vid,
            'nid' => $node->nid,
          ))
          ->execute();
      }
    }
    // If the node has a shadow forum topic, update the record for this
    // revision.
    if (!empty($node->shadow)) {
      db_delete('forum')
        ->condition('nid', $node->nid)
        ->condition('vid', $node->vid)
        ->execute();
      db_insert('forum')
        ->fields(array(
          'nid' => $node->nid,
          'vid' => $node->vid,
          'tid' => $node->forum_tid,
        ))
        ->execute();
     }
  }
}
```

---
_Drupal 7.103 · [modules/forum/forum.module](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module) · Licensed GPL-2.0-or-later (see LICENSE)._
