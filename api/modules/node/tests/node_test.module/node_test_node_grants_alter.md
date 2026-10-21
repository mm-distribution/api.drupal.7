# node_test_node_grants_alter()

- **Type:** Function
- **File:** [`modules/node/tests/node_test.module`](_file.md), lines 120–123 · [local source](../../../../../source/modules/node/tests/node_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/tests/node_test.module#L120-L123)
- **Module/theme:** node_test
- **Implements:** [hook_node_grants_alter()](../../node.api.php/hook_node_grants_alter.md)

## Signature

```php
function node_test_node_grants_alter(&$grants, $account, $op)
```

## Documentation

```text
Implements hook_node_grants_alter().
```

## Code

```php
function node_test_node_grants_alter(&$grants, $account, $op) {
  // Return an empty array of grants to prove that we can alter by reference.
  $grants = array();
}
```

---
_Drupal 7.103 · [modules/node/tests/node_test.module](https://github.com/drupal/drupal/blob/7.103/modules/node/tests/node_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
