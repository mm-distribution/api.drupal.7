# entity_crud_hook_test_node_update()

- **Type:** Function
- **File:** [`modules/simpletest/tests/entity_crud_hook_test.module`](_file.md), lines 179–181 · [local source](../../../../../source/modules/simpletest/tests/entity_crud_hook_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.module#L179-L181)
- **Module/theme:** batch_test
- **Implements:** [hook_node_update()](../../../node/node.api.php/hook_node_update.md)

## Signature

```php
function entity_crud_hook_test_node_update()
```

## Documentation

```text
Implements hook_node_update().
```

## Code

```php
function entity_crud_hook_test_node_update() {
  $_SESSION['entity_crud_hook_test'][] = (__FUNCTION__ . ' called');
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/entity_crud_hook_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
