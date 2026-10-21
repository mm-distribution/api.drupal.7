# _contact_personal_tab_access()

- **Type:** Function
- **File:** [`modules/contact/contact.module`](_file.md), lines 115–145 · [local source](../../../../source/modules/contact/contact.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.module#L115-L145)
- **Module/theme:** contact

## Signature

```php
function _contact_personal_tab_access($account)
```

## Documentation

```text
Menu access callback for a user's personal contact form.

@param $account
  The user object of the user whose contact form is being requested.
```

## Code

```php
function _contact_personal_tab_access($account) {
  global $user;

  // Anonymous users cannot have contact forms.
  if (!$account->uid) {
    return FALSE;
  }

  // User administrators should always have access to personal contact forms.
  if (user_access('administer users')) {
    return TRUE;
  }

  // Users may not contact themselves.
  if ($user->uid == $account->uid) {
    return FALSE;
  }

  // If the requested user has disabled their contact form, or this preference
  // has not yet been saved, do not allow users to contact them.
  if (empty($account->data['contact'])) {
    return FALSE;
  }

  // If requested user has been blocked, do not allow users to contact them.
  if (empty($account->status)) {
    return FALSE;
  }

  return user_access('access user contact forms');
}
```

---
_Drupal 7.103 · [modules/contact/contact.module](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.module) · Licensed GPL-2.0-or-later (see LICENSE)._
