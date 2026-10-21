# user_form_test_form_user_pass_reset_alter()

- **Type:** Function
- **File:** [`modules/user/tests/user_form_test.module`](_file.md), lines 87–103 · [local source](../../../../../source/modules/user/tests/user_form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/tests/user_form_test.module#L87-L103)
- **Module/theme:** user_flood_test
- **Implements:** [hook_form_FORM_ID_alter()](../../../system/system.api.php/hook_form_FORM_ID_alter.md)

## Signature

```php
function user_form_test_form_user_pass_reset_alter(&$form, &$form_state)
```

## Documentation

```text
Implements hook_form_FORM_ID_alter().
```

## Code

```php
function user_form_test_form_user_pass_reset_alter(&$form, &$form_state) {
  // An unaltered form has no form values; the uid/timestmap/"confirm" are in
  // the URL arguments. (If for some reason a form_alter method needs the
  // hash, it can be retrieved from $form['#action'].)
  if (!is_numeric(arg(2)) || !is_numeric(arg(3)) || !is_string(arg(4)) || arg(4) !== 'confirm') {
    throw new Exception("Something unexpected changed in the user_pass_reset form; we are not getting the UID/timestamp/'confirm' passed anymore.");
  }
  // Use the variable system to communicate to the test code, since we don't
  // share a session with it.
  variable_set('user_test_pass_reset_form_build_' . arg(2), TRUE);

  $form['#submit'][] = 'user_form_test_form_user_pass_reset_submit';
  // We must cache the form to ensure the form builder (user_pass_reset()) is
  // skipped when processing the submitted form, otherwise we get redirected
  // already during form build.
  $form_state['cache'] = TRUE;
}
```

---
_Drupal 7.103 · [modules/user/tests/user_form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/user/tests/user_form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
