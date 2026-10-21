# node_revision_list()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 2225–2233 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L2225-L2233)
- **Module/theme:** node

## Signature

```php
function node_revision_list($node)
```

## Documentation

```text
Returns a list of all the existing revision numbers.

@param $node
  The node object.

@return
  An associative array keyed by node revision number.
```

## Code

```php
function node_revision_list($node) {
  $revisions = array();
  $result = db_query('SELECT r.vid, r.title, r.log, r.uid, n.vid AS current_vid, r.timestamp, u.name FROM {node_revision} r LEFT JOIN {node} n ON n.vid = r.vid INNER JOIN {users} u ON u.uid = r.uid WHERE r.nid = :nid ORDER BY r.vid DESC', array(':nid' => $node->nid));
  foreach ($result as $revision) {
    $revisions[$revision->vid] = $revision;
  }

  return $revisions;
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
