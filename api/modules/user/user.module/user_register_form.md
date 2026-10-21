# user_register_form()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 3909–3963 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L3909-L3963)
- **Module/theme:** user
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function user_register_form($form, &$form_state)
```

## Documentation

```text
Form builder; the user registration form.

@ingroup forms
@see user_account_form()
@see user_account_form_validate()
@see user_register_submit()
```

## Code

```php
function user_register_form($form, &$form_state) {
  global $user;

  $admin = user_access('administer users');

  // Pass access information to the submit handler. Running an access check
  // inside the submit function interferes with form processing and breaks
  // hook_form_alter().
  $form['administer_users'] = array(
    '#type' => 'value',
    '#value' => $admin,
  );

  // If we aren't admin but already logged on, go to the user page instead.
  if (!$admin && $user->uid) {
    drupal_goto('user/' . $user->uid);
  }

  $form['#user'] = drupal_anonymous_user();
  $form['#user_category'] = 'register';

  $form['#attached']['library'][] = array('system', 'jquery.cookie');
  $form['#attributes']['class'][] = 'user-info-from-cookie';

  // Start with the default user account fields.
  user_account_form($form, $form_state);

  // Attach field widgets, and hide the ones where the 'user_register_form'
  // setting is not on.
  $langcode = entity_language('user', $form['#user']);
  field_attach_form('user', $form['#user'], $form, $form_state, $langcode);
  foreach (field_info_instances('user', 'user') as $field_name => $instance) {
    if (empty($instance['settings']['user_register_form'])) {
      $form[$field_name]['#access'] = FALSE;
    }
  }

  if ($admin) {
    // Redirect back to page which initiated the create request;
    // usually admin/people/create.
    $form_state['redirect'] = $_GET['q'];
  }

  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Create new account'),
  );

  $form['#validate'][] = 'user_register_validate';
  // Add the final user registration form submit handler.
  $form['#submit'][] = 'user_register_submit';

  return $form;
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
