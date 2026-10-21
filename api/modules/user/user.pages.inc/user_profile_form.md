# user_profile_form()

- **Type:** Function
- **File:** [`modules/user/user.pages.inc`](_file.md), lines 389–433 · [local source](../../../../source/modules/user/user.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.pages.inc#L389-L433)
- **Module/theme:** user
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function user_profile_form($form, &$form_state, $account, $category = 'account')
```

## Documentation

```text
Form builder; edit a user account or one of their profile categories.

@ingroup forms
@see user_account_form()
@see user_account_form_validate()
@see user_profile_form_validate()
@see user_profile_form_submit()
@see user_cancel_confirm_form_submit()
```

## Code

```php
function user_profile_form($form, &$form_state, $account, $category = 'account') {
  global $user;

  // During initial form build, add the entity to the form state for use during
  // form building and processing. During a rebuild, use what is in the form
  // state.
  if (!isset($form_state['user'])) {
    $form_state['user'] = $account;
  }
  else {
    $account = $form_state['user'];
  }

  // @todo Legacy support. Modules are encouraged to access the entity using
  //   $form_state. Remove in Drupal 8.
  $form['#user'] = $account;
  $form['#user_category'] = $category;

  if ($category == 'account') {
    user_account_form($form, $form_state);
    // Attach field widgets.
    $langcode = entity_language('user', $account);
    field_attach_form('user', $account, $form, $form_state, $langcode);
  }

  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Save'),
  );
  if ($category == 'account') {
    $form['actions']['cancel'] = array(
      '#type' => 'submit',
      '#value' => t('Cancel account'),
      '#submit' => array('user_edit_cancel_submit'),
      '#access' => $account->uid > 1 && (($account->uid == $user->uid && user_access('cancel account')) || user_access('administer users')),
    );
  }

  $form['#validate'][] = 'user_profile_form_validate';
  // Add the final user profile form submit handler.
  $form['#submit'][] = 'user_profile_form_submit';

  return $form;
}
```

---
_Drupal 7.103 · [modules/user/user.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/user/user.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
