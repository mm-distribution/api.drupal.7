# forum_node_presave()

- **Type:** Function
- **File:** [`modules/forum/forum.module`](_file.md), lines 327–344 · [local source](../../../../source/modules/forum/forum.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module#L327-L344)
- **Module/theme:** forum
- **Implements:** [hook_node_presave()](../../node/node.api.php/hook_node_presave.md)

## Signature

```php
function forum_node_presave($node)
```

## Documentation

```text
Implements hook_node_presave().

Assigns the forum taxonomy when adding a topic from within a forum.
```

## Code

```php
function forum_node_presave($node) {
  if (_forum_node_check_node_type($node)) {
    // Make sure all fields are set properly:
    $node->icon = !empty($node->icon) ? $node->icon : '';
    reset($node->taxonomy_forums);
    $langcode = key($node->taxonomy_forums);
    if (!empty($node->taxonomy_forums[$langcode])) {
      $node->forum_tid = $node->taxonomy_forums[$langcode][0]['tid'];
      if (isset($node->nid)) {
        $old_tid = db_query_range("SELECT f.tid FROM {forum} f INNER JOIN {node} n ON f.vid = n.vid WHERE n.nid = :nid ORDER BY f.vid DESC", 0, 1, array(':nid' => $node->nid))->fetchField();
        if ($old_tid && isset($node->forum_tid) && ($node->forum_tid != $old_tid) && !empty($node->shadow)) {
          // A shadow copy needs to be created. Retain new term and add old term.
          $node->taxonomy_forums[$langcode][] = array('tid' => $old_tid);
        }
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/forum/forum.module](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module) · Licensed GPL-2.0-or-later (see LICENSE)._
