# user_form_test_form_user_pass_reset_submit()

- **Type:** Function
- **File:** [`modules/user/tests/user_form_test.module`](_file.md), lines 108–121 · [local source](../../../../../source/modules/user/tests/user_form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/tests/user_form_test.module#L108-L121)
- **Module/theme:** user_flood_test

## Signature

```php
function user_form_test_form_user_pass_reset_submit($form, &$form_state)
```

## Documentation

```text
Submit function for user_pass_reset().
```

## Code

```php
function user_form_test_form_user_pass_reset_submit($form, &$form_state) {
  // On submit, the hash is in arg(4).
  if (!is_numeric(arg(2)) || !is_numeric(arg(3)) || !is_string(arg(4)) || strlen(arg(4)) < 32) {
    throw new Exception("Something unexpected changed in the user_pass_reset form; we are not getting the UID/timestamp/hash passed anymore.");
  }
  variable_set('user_test_pass_reset_form_submit_' . arg(2), TRUE);
  // Because the form does no further processing and has no redirect set,
  // drupal_redirect_form() will redirect back to ourselves
  // (user/reset/UID/TIMESTAMP/HASH/login); we will be logged in and redirected
  // while the form is built again. FYI: we cannot set $form_state['rebuild']
  // to get around the first redirect without further hacks, because then the
  // form won't pass the hash. (Our original $form_state['build_info']['args']
  // contains "confirm" for the 3rd argument.)
}
```

---
_Drupal 7.103 · [modules/user/tests/user_form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/user/tests/user_form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
