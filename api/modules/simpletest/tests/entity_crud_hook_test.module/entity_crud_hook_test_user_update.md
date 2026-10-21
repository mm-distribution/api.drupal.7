# entity_crud_hook_test_user_update()

- **Type:** Function
- **File:** [`modules/simpletest/tests/entity_crud_hook_test.module`](_file.md), lines 200–202 · [local source](../../../../../source/modules/simpletest/tests/entity_crud_hook_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.module#L200-L202)
- **Module/theme:** batch_test
- **Implements:** [hook_user_update()](../../../user/user.api.php/hook_user_update.md)

## Signature

```php
function entity_crud_hook_test_user_update()
```

## Documentation

```text
Implements hook_user_update().
```

## Code

```php
function entity_crud_hook_test_user_update() {
  $_SESSION['entity_crud_hook_test'][] = (__FUNCTION__ . ' called');
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/entity_crud_hook_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
