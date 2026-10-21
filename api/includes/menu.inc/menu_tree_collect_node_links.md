# menu_tree_collect_node_links()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 1474–1487 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L1474-L1487)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_tree_collect_node_links(&$tree, &$node_links)
```

## Documentation

```text
Collects node links from a given menu tree recursively.

@param $tree
  The menu tree you wish to collect node links from.
@param $node_links
  An array in which to store the collected node links.
```

## Code

```php
function menu_tree_collect_node_links(&$tree, &$node_links) {
  foreach ($tree as $key => $v) {
    if ($tree[$key]['link']['router_path'] == 'node/%') {
      $nid = substr($tree[$key]['link']['link_path'], 5);
      if (is_numeric($nid)) {
        $node_links[$nid][$tree[$key]['link']['mlid']] = &$tree[$key]['link'];
        $tree[$key]['link']['access'] = FALSE;
      }
    }
    if ($tree[$key]['below']) {
      menu_tree_collect_node_links($tree[$key]['below'], $node_links);
    }
  }
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
