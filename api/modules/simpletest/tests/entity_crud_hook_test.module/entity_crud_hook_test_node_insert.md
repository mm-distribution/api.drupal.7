# entity_crud_hook_test_node_insert()

- **Type:** Function
- **File:** [`modules/simpletest/tests/entity_crud_hook_test.module`](_file.md), lines 81–83 · [local source](../../../../../source/modules/simpletest/tests/entity_crud_hook_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.module#L81-L83)
- **Module/theme:** batch_test
- **Implements:** [hook_node_insert()](../../../node/node.api.php/hook_node_insert.md)

## Signature

```php
function entity_crud_hook_test_node_insert()
```

## Documentation

```text
Implements hook_node_insert().
```

## Code

```php
function entity_crud_hook_test_node_insert() {
  $_SESSION['entity_crud_hook_test'][] = (__FUNCTION__ . ' called');
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/entity_crud_hook_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
