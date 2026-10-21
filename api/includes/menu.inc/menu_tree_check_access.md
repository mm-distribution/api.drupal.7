# menu_tree_check_access()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 1498–1526 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L1498-L1526)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_tree_check_access(&$tree, $node_links = array())
```

## Documentation

```text
Checks access and performs dynamic operations for each link in the tree.

@param $tree
  The menu tree you wish to operate on.
@param $node_links
  A collection of node link references generated from $tree by
  menu_tree_collect_node_links().
```

## Code

```php
function menu_tree_check_access(&$tree, $node_links = array()) {
  if ($node_links && (user_access('access content') || user_access('bypass node access'))) {
    $nids = array_keys($node_links);
    $select = db_select('node', 'n');
    $select->addField('n', 'nid');
    // When a menu administrator who we know has permission to see unpublished
    // nodes is administering the menu, included the unpublished nodes in the
    // tree, with a special flag so that the Menu module can label them.
    // Otherwise, exclude these nodes from the tree.
    if (!empty($GLOBALS['menu_admin']) && user_access('bypass node access')) {
      $select->addField('n', 'status');
    }
    else {
      $select->condition('n.status', 1);
    }
    $select->condition('n.nid', $nids, 'IN');
    $select->addTag('node_access');
    $node_objects = $select->execute()->fetchAll();
    foreach ($node_objects as $node_object) {
      foreach ($node_links[$node_object->nid] as $mlid => $link) {
        $node_links[$node_object->nid][$mlid]['access'] = TRUE;
        if (isset($node_object->status)) {
          $node_links[$node_object->nid][$mlid]['node_unpublished'] = !$node_object->status;
        }
      }
    }
  }
  _menu_tree_check_access($tree);
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
