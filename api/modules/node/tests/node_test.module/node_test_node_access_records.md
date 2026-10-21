# node_test_node_access_records()

- **Type:** Function
- **File:** [`modules/node/tests/node_test.module`](_file.md), lines 71–100 · [local source](../../../../../source/modules/node/tests/node_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/tests/node_test.module#L71-L100)
- **Module/theme:** node_test
- **Implements:** [hook_node_access_records()](../../node.api.php/hook_node_access_records.md)

## Signature

```php
function node_test_node_access_records($node)
```

## Documentation

```text
Implements hook_node_access_records().
```

## Code

```php
function node_test_node_access_records($node) {
  // Return nothing when testing for empty responses.
  if (!empty($node->disable_node_access)) {
    return;
  }
  $grants = array();
  if ($node->type == 'article') {
    // Create grant in arbitrary article_realm for article nodes.
    $grants[] = array(
      'realm' => 'test_article_realm',
      'gid' => 1,
      'grant_view' => 1,
      'grant_update' => 0,
      'grant_delete' => 0,
      'priority' => 0,
    );
  }
  elseif ($node->type == 'page') {
    // Create grant in arbitrary page_realm for page nodes.
    $grants[] = array(
      'realm' => 'test_page_realm',
      'gid' => 1,
      'grant_view' => 1,
      'grant_update' => 0,
      'grant_delete' => 0,
      'priority' => 0,
    );
  }
  return $grants;
}
```

---
_Drupal 7.103 · [modules/node/tests/node_test.module](https://github.com/drupal/drupal/blob/7.103/modules/node/tests/node_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
