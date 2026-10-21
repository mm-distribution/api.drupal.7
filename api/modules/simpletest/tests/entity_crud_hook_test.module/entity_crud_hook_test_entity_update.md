# entity_crud_hook_test_entity_update()

- **Type:** Function
- **File:** [`modules/simpletest/tests/entity_crud_hook_test.module`](_file.md), lines 158–160 · [local source](../../../../../source/modules/simpletest/tests/entity_crud_hook_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.module#L158-L160)
- **Module/theme:** batch_test
- **Implements:** [hook_entity_update()](../../../system/system.api.php/hook_entity_update.md)

## Signature

```php
function entity_crud_hook_test_entity_update($entity, $type)
```

## Documentation

```text
Implements hook_entity_update().
```

## Code

```php
function entity_crud_hook_test_entity_update($entity, $type) {
  $_SESSION['entity_crud_hook_test'][] = (__FUNCTION__ . ' called for type ' . $type);
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/entity_crud_hook_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
