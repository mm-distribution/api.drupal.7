# user_form_test_current_password_submit()

- **Type:** Function
- **File:** [`modules/user/tests/user_form_test.module`](_file.md), lines 62–64 · [local source](../../../../../source/modules/user/tests/user_form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/tests/user_form_test.module#L62-L64)
- **Module/theme:** user_flood_test

## Signature

```php
function user_form_test_current_password_submit($form, &$form_state)
```

## Documentation

```text
Submit function for the test form for user_validate_current_pass().
```

## Code

```php
function user_form_test_current_password_submit($form, &$form_state) {
  drupal_set_message(t('The password has been validated and the form submitted successfully.'));
}
```

---
_Drupal 7.103 · [modules/user/tests/user_form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/user/tests/user_form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
