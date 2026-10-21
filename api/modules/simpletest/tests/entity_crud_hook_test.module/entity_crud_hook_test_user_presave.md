# entity_crud_hook_test_user_presave()

- **Type:** Function
- **File:** [`modules/simpletest/tests/entity_crud_hook_test.module`](_file.md), lines 53–55 · [local source](../../../../../source/modules/simpletest/tests/entity_crud_hook_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.module#L53-L55)
- **Module/theme:** batch_test
- **Implements:** [hook_user_presave()](../../../user/user.api.php/hook_user_presave.md)

## Signature

```php
function entity_crud_hook_test_user_presave()
```

## Documentation

```text
Implements hook_user_presave().
```

## Code

```php
function entity_crud_hook_test_user_presave() {
  $_SESSION['entity_crud_hook_test'][] = (__FUNCTION__ . ' called');
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/entity_crud_hook_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
