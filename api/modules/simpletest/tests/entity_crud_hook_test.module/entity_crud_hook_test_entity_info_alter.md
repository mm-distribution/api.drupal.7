# entity_crud_hook_test_entity_info_alter()

- **Type:** Function
- **File:** [`modules/simpletest/tests/entity_crud_hook_test.module`](_file.md), lines 256–261 · [local source](../../../../../source/modules/simpletest/tests/entity_crud_hook_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.module#L256-L261)
- **Module/theme:** batch_test
- **Implements:** [hook_entity_info_alter()](../../../system/system.api.php/hook_entity_info_alter.md)

## Signature

```php
function entity_crud_hook_test_entity_info_alter(&$entity_info)
```

## Documentation

```text
Implements hook_entity_info_alter().
```

## Code

```php
function entity_crud_hook_test_entity_info_alter(&$entity_info) {
  if (variable_get('entity_crud_hook_test_alter_controller_class', FALSE)) {
    // Set the controller class for nodes to NULL.
    $entity_info['node']['controller class'] = NULL;
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/entity_crud_hook_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
