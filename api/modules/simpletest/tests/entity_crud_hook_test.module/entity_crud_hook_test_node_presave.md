# entity_crud_hook_test_node_presave()

- **Type:** Function
- **File:** [`modules/simpletest/tests/entity_crud_hook_test.module`](_file.md), lines 32–34 · [local source](../../../../../source/modules/simpletest/tests/entity_crud_hook_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.module#L32-L34)
- **Module/theme:** batch_test
- **Implements:** [hook_node_presave()](../../../node/node.api.php/hook_node_presave.md)

## Signature

```php
function entity_crud_hook_test_node_presave()
```

## Documentation

```text
Implements hook_node_presave().
```

## Code

```php
function entity_crud_hook_test_node_presave() {
  $_SESSION['entity_crud_hook_test'][] = (__FUNCTION__ . ' called');
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/entity_crud_hook_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
