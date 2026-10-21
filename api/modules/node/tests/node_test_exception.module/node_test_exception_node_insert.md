# node_test_exception_node_insert()

- **Type:** Function
- **File:** [`modules/node/tests/node_test_exception.module`](_file.md), lines 11–15 · [local source](../../../../../source/modules/node/tests/node_test_exception.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/tests/node_test_exception.module#L11-L15)
- **Module/theme:** node_test
- **Implements:** [hook_node_insert()](../../node.api.php/hook_node_insert.md)

## Signature

```php
function node_test_exception_node_insert($node)
```

## Documentation

```text
Implements hook_node_insert().
```

## Code

```php
function node_test_exception_node_insert($node) {
  if ($node->title == 'testing_transaction_exception') {
    throw new Exception('Test exception for rollback.');
  }
}
```

---
_Drupal 7.103 · [modules/node/tests/node_test_exception.module](https://github.com/drupal/drupal/blob/7.103/modules/node/tests/node_test_exception.module) · Licensed GPL-2.0-or-later (see LICENSE)._
