# entity_crud_hook_test_node_delete()

- **Type:** Function
- **File:** [`modules/simpletest/tests/entity_crud_hook_test.module`](_file.md), lines 228–230 · [local source](../../../../../source/modules/simpletest/tests/entity_crud_hook_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.module#L228-L230)
- **Module/theme:** batch_test
- **Implements:** [hook_node_delete()](../../../node/node.api.php/hook_node_delete.md)

## Signature

```php
function entity_crud_hook_test_node_delete()
```

## Documentation

```text
Implements hook_node_delete().
```

## Code

```php
function entity_crud_hook_test_node_delete() {
  $_SESSION['entity_crud_hook_test'][] = (__FUNCTION__ . ' called');
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/entity_crud_hook_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
