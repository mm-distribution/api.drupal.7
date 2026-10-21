# entity_crud_hook_test_entity_delete()

- **Type:** Function
- **File:** [`modules/simpletest/tests/entity_crud_hook_test.module`](_file.md), lines 207–209 · [local source](../../../../../source/modules/simpletest/tests/entity_crud_hook_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.module#L207-L209)
- **Module/theme:** batch_test
- **Implements:** [hook_entity_delete()](../../../system/system.api.php/hook_entity_delete.md)

## Signature

```php
function entity_crud_hook_test_entity_delete($entity, $type)
```

## Documentation

```text
Implements hook_entity_delete().
```

## Code

```php
function entity_crud_hook_test_entity_delete($entity, $type) {
  $_SESSION['entity_crud_hook_test'][] = (__FUNCTION__ . ' called for type ' . $type);
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/entity_crud_hook_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
