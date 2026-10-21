# session_test_form_user_login_alter()

- **Type:** Function
- **File:** [`modules/simpletest/tests/session_test.module`](_file.md), lines 180–182 · [local source](../../../../../source/modules/simpletest/tests/session_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session_test.module#L180-L182)
- **Module/theme:** batch_test
- **Implements:** [hook_form_FORM_ID_alter()](../../../system/system.api.php/hook_form_FORM_ID_alter.md)

## Signature

```php
function session_test_form_user_login_alter(&$form)
```

## Documentation

```text
Implements hook_form_FORM_ID_alter().
```

## Code

```php
function session_test_form_user_login_alter(&$form) {
  $form['#https'] = TRUE;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/session_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
