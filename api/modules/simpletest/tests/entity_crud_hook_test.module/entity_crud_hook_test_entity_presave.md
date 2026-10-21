# entity_crud_hook_test_entity_presave()

- **Type:** Function
- **File:** [`modules/simpletest/tests/entity_crud_hook_test.module`](_file.md), lines 11–13 · [local source](../../../../../source/modules/simpletest/tests/entity_crud_hook_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.module#L11-L13)
- **Module/theme:** batch_test
- **Implements:** [hook_entity_presave()](../../../system/system.api.php/hook_entity_presave.md)

## Signature

```php
function entity_crud_hook_test_entity_presave($entity, $type)
```

## Documentation

```text
Implements hook_entity_presave().
```

## Code

```php
function entity_crud_hook_test_entity_presave($entity, $type) {
  $_SESSION['entity_crud_hook_test'][] = (__FUNCTION__ . ' called for type ' . $type);
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/entity_crud_hook_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
