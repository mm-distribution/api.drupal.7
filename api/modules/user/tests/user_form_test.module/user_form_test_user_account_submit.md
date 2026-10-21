# user_form_test_user_account_submit()

- **Type:** Function
- **File:** [`modules/user/tests/user_form_test.module`](_file.md), lines 78–82 · [local source](../../../../../source/modules/user/tests/user_form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/tests/user_form_test.module#L78-L82)
- **Module/theme:** user_flood_test

## Signature

```php
function user_form_test_user_account_submit($form, &$form_state)
```

## Documentation

```text
Submit function for user_profile_form().
```

## Code

```php
function user_form_test_user_account_submit($form, &$form_state) {
  // Rebuild the form instead of letting the process end. This allows us to
  // test for bugs that can be triggered in contributed modules.
  $form_state['rebuild'] = TRUE;
}
```

---
_Drupal 7.103 · [modules/user/tests/user_form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/user/tests/user_form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
