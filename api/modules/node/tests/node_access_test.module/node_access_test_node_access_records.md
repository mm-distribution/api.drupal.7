# node_access_test_node_access_records()

- **Type:** Function
- **File:** [`modules/node/tests/node_access_test.module`](_file.md), lines 31–64 · [local source](../../../../../source/modules/node/tests/node_access_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/tests/node_access_test.module#L31-L64)
- **Module/theme:** node_test
- **Implements:** [hook_node_access_records()](../../node.api.php/hook_node_access_records.md)

## Signature

```php
function node_access_test_node_access_records($node)
```

## Documentation

```text
Implements hook_node_access_records().
```

## Code

```php
function node_access_test_node_access_records($node) {
  $grants = array();
  // For NodeAccessBaseTableTestCase, only set records for private nodes.
  if (!variable_get('node_access_test_private') || $node->private) {
    $grants[] = array(
      'realm' => 'node_access_test',
      'gid' => 8888,
      'grant_view' => 1,
      'grant_update' => 0,
      'grant_delete' => 0,
      'priority' => 0,
    );
    $grants[] = array(
      'realm' => 'node_access_test',
      'gid' => 8889,
      'grant_view' => 1,
      'grant_update' => 0,
      'grant_delete' => 0,
      'priority' => 0,
    );
    // For the author realm, the GID is equivalent to a UID, which
    // means there are many many groups of just 1 user.
    $grants[] = array(
      'realm' => 'node_access_test_author',
      'gid' => $node->uid,
      'grant_view' => 1,
      'grant_update' => 1,
      'grant_delete' => 1,
      'priority' => 0,
    );
  }

  return $grants;
}
```

---
_Drupal 7.103 · [modules/node/tests/node_access_test.module](https://github.com/drupal/drupal/blob/7.103/modules/node/tests/node_access_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
