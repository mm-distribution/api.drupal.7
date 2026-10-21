# node_access_test_node_insert()

- **Type:** Function
- **File:** [`modules/node/tests/node_access_test.module`](_file.md), lines 209–211 · [local source](../../../../../source/modules/node/tests/node_access_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/tests/node_access_test.module#L209-L211)
- **Module/theme:** node_test
- **Implements:** [hook_node_insert()](../../node.api.php/hook_node_insert.md)

## Signature

```php
function node_access_test_node_insert($node)
```

## Documentation

```text
Implements hook_node_insert().
```

## Code

```php
function node_access_test_node_insert($node) {
  _node_access_test_node_write($node);
}
```

---
_Drupal 7.103 · [modules/node/tests/node_access_test.module](https://github.com/drupal/drupal/blob/7.103/modules/node/tests/node_access_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
