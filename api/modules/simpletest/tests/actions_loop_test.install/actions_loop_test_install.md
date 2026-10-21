# actions_loop_test_install()

- **Type:** Function
- **File:** [`modules/simpletest/tests/actions_loop_test.install`](_file.md), lines 6–11 · [local source](../../../../../source/modules/simpletest/tests/actions_loop_test.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/actions_loop_test.install#L6-L11)
- **Module/theme:** batch_test
- **Implements:** [hook_install()](../../../system/system.api.php/hook_install.md)

## Signature

```php
function actions_loop_test_install()
```

## Documentation

```text
Implements hook_install().
```

## Code

```php
function actions_loop_test_install() {
   db_update('system')
    ->fields(array('weight' => 1))
    ->condition('name', 'actions_loop_test')
    ->execute();
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/actions_loop_test.install](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/actions_loop_test.install) · Licensed GPL-2.0-or-later (see LICENSE)._
