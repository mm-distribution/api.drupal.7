# user_form_test_form_user_profile_form_alter()

- **Type:** Function
- **File:** [`modules/user/tests/user_form_test.module`](_file.md), lines 69–73 · [local source](../../../../../source/modules/user/tests/user_form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/tests/user_form_test.module#L69-L73)
- **Module/theme:** user_flood_test
- **Implements:** [hook_form_FORM_ID_alter()](../../../system/system.api.php/hook_form_FORM_ID_alter.md)

## Signature

```php
function user_form_test_form_user_profile_form_alter(&$form, &$form_state)
```

## Documentation

```text
Implements hook_form_FORM_ID_alter().
```

## Code

```php
function user_form_test_form_user_profile_form_alter(&$form, &$form_state) {
  if (variable_get('user_form_test_user_profile_form_rebuild', FALSE)) {
    $form['#submit'][] = 'user_form_test_user_account_submit';
  }
}
```

---
_Drupal 7.103 · [modules/user/tests/user_form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/user/tests/user_form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
