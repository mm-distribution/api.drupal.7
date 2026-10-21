# user_profile_form_submit()

- **Type:** Function
- **File:** [`modules/user/user.pages.inc`](_file.md), lines 449–478 · [local source](../../../../source/modules/user/user.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.pages.inc#L449-L478)
- **Module/theme:** user

## Signature

```php
function user_profile_form_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for user_profile_form().

@see user_profile_form_validate()
```

## Code

```php
function user_profile_form_submit($form, &$form_state) {
  $account = $form_state['user'];
  $category = $form['#user_category'];
  // Remove unneeded values.
  form_state_values_clean($form_state);

  // Before updating the account entity, keep an unchanged copy for use with
  // user_save() later. This is necessary for modules implementing the user
  // hooks to be able to react on changes by comparing the values of $account
  // and $edit.
  $account_unchanged = clone $account;

  entity_form_submit_build_entity('user', $account, $form, $form_state);

  // Populate $edit with the properties of $account, which have been edited on
  // this form by taking over all values, which appear in the form values too.
  $edit = array_intersect_key((array) $account, $form_state['values']);

  user_save($account_unchanged, $edit, $category);
  $form_state['values']['uid'] = $account->uid;

  if ($category == 'account' && !empty($edit['pass'])) {
    // Remove the password reset tag since a new password was saved.
    unset($_SESSION['pass_reset_'. $account->uid]);
  }
  // Clear the page cache because pages can contain usernames and/or profile information:
  cache_clear_all();

  drupal_set_message(t('The changes have been saved.'));
}
```

---
_Drupal 7.103 · [modules/user/user.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/user/user.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
