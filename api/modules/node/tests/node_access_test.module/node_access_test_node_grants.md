# node_access_test_node_grants()

- **Type:** Function
- **File:** [`modules/node/tests/node_access_test.module`](_file.md), lines 15–26 · [local source](../../../../../source/modules/node/tests/node_access_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/tests/node_access_test.module#L15-L26)
- **Module/theme:** node_test
- **Implements:** [hook_node_grants()](../../node.api.php/hook_node_grants.md)

## Signature

```php
function node_access_test_node_grants($account, $op)
```

## Documentation

```text
Implements hook_node_grants().
```

## Code

```php
function node_access_test_node_grants($account, $op) {
  $grants = array();
  // First grant a grant to the author for own content.
  $grants['node_access_test_author'] = array($account->uid);
  if ($op == 'view' && user_access('node test view', $account)) {
    $grants['node_access_test'] = array(8888, 8889);
  }
  if ($op == 'view' && $account->uid == variable_get('node_test_node_access_all_uid', 0)) {
    $grants['node_access_all'] = array(0);
  }
  return $grants;
}
```

---
_Drupal 7.103 · [modules/node/tests/node_access_test.module](https://github.com/drupal/drupal/blob/7.103/modules/node/tests/node_access_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
