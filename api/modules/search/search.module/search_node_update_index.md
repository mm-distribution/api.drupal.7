# search_node_update_index()

- **Type:** Function
- **File:** [`modules/search/search.module`](_file.md), lines 794–804 · [local source](../../../../source/modules/search/search.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module#L794-L804)
- **Module/theme:** search
- **Implements:** [hook_node_update_index()](../../node/node.api.php/hook_node_update_index.md)

## Signature

```php
function search_node_update_index($node)
```

## Documentation

```text
Implements hook_node_update_index().
```

## Code

```php
function search_node_update_index($node) {
  // Transplant links to a node into the target node.
  $result = db_query("SELECT caption FROM {search_node_links} WHERE nid = :nid", array(':nid' => $node->nid), array('target' => 'slave'));
  $output = array();
  foreach ($result as $link) {
    $output[] = $link->caption;
  }
  if (count($output)) {
    return '<a>(' . implode(', ', $output) . ')</a>';
  }
}
```

---
_Drupal 7.103 · [modules/search/search.module](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module) · Licensed GPL-2.0-or-later (see LICENSE)._
