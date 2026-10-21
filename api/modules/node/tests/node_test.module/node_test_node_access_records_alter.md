# node_test_node_access_records_alter()

- **Type:** Function
- **File:** [`modules/node/tests/node_test.module`](_file.md), lines 105–115 · [local source](../../../../../source/modules/node/tests/node_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/tests/node_test.module#L105-L115)
- **Module/theme:** node_test
- **Implements:** [hook_node_access_records_alter()](../../node.api.php/hook_node_access_records_alter.md)

## Signature

```php
function node_test_node_access_records_alter(&$grants, $node)
```

## Documentation

```text
Implements hook_node_access_records_alter().
```

## Code

```php
function node_test_node_access_records_alter(&$grants, $node) {
  if (!empty($grants)) {
    foreach ($grants as $key => $grant) {
      // Alter grant from test_page_realm to test_alter_realm and modify the gid.
      if ($grant['realm'] == 'test_page_realm' && $node->promote) {
        $grants[$key]['realm'] = 'test_alter_realm';
        $grants[$key]['gid'] = 2;
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/node/tests/node_test.module](https://github.com/drupal/drupal/blob/7.103/modules/node/tests/node_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
