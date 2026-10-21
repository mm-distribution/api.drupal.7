# forum_node_load()

- **Type:** Function
- **File:** [`modules/forum/forum.module`](_file.md), lines 428–445 · [local source](../../../../source/modules/forum/forum.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module#L428-L445)
- **Module/theme:** forum
- **Implements:** [hook_node_load()](../../node/node.api.php/hook_node_load.md)

## Signature

```php
function forum_node_load($nodes)
```

## Documentation

```text
Implements hook_node_load().
```

## Code

```php
function forum_node_load($nodes) {
  $node_vids = array();
  foreach ($nodes as $node) {
    if (_forum_node_check_node_type($node)) {
      $node_vids[] = $node->vid;
    }
  }
  if (!empty($node_vids)) {
    $query = db_select('forum', 'f');
    $query
      ->fields('f', array('nid', 'tid'))
      ->condition('f.vid', $node_vids);
    $result = $query->execute();
    foreach ($result as $record) {
      $nodes[$record->nid]->forum_tid = $record->tid;
    }
  }
}
```

---
_Drupal 7.103 · [modules/forum/forum.module](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module) · Licensed GPL-2.0-or-later (see LICENSE)._
