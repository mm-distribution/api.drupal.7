# _user_cancel()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 2554–2592 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L2554-L2592)
- **Module/theme:** user

## Signature

```php
function _user_cancel($edit, $account, $method)
```

## Documentation

```text
Implements callback_batch_operation().

Last step for cancelling a user account.

Since batch and session API require a valid user account, the actual
cancellation of a user account needs to happen last.

@see user_cancel()
```

## Code

```php
function _user_cancel($edit, $account, $method) {
  global $user;

  switch ($method) {
    case 'user_cancel_block':
    case 'user_cancel_block_unpublish':
    default:
      // Send account blocked notification if option was checked.
      if (!empty($edit['user_cancel_notify'])) {
        _user_mail_notify('status_blocked', $account);
      }
      user_save($account, array('status' => 0));
      drupal_set_message(t('%name has been disabled.', array('%name' => $account->name)));
      watchdog('user', 'Blocked user: %name %email.', array('%name' => $account->name, '%email' => '<' . $account->mail . '>'), WATCHDOG_NOTICE);
      break;

    case 'user_cancel_reassign':
    case 'user_cancel_delete':
      // Send account canceled notification if option was checked.
      if (!empty($edit['user_cancel_notify'])) {
        _user_mail_notify('status_canceled', $account);
      }
      user_delete($account->uid);
      drupal_set_message(t('%name has been deleted.', array('%name' => $account->name)));
      watchdog('user', 'Deleted user: %name %email.', array('%name' => $account->name, '%email' => '<' . $account->mail . '>'), WATCHDOG_NOTICE);
      break;
  }

  // After cancelling account, ensure that user is logged out. We can't destroy
  // their session though, as we might have information in it, and we can't
  // regenerate it because batch API uses the session ID, we will regenerate it
  // in _user_cancel_session_regenerate().
  if ($account->uid == $user->uid) {
    $user = drupal_anonymous_user();
  }

  // Clear the cache for anonymous users.
  cache_clear_all();
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
