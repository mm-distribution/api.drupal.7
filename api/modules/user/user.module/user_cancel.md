# user_cancel()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 2499–2542 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L2499-L2542)
- **Module/theme:** user

## Signature

```php
function user_cancel($edit, $uid, $method)
```

## Documentation

```text
Cancel a user account.

Since the user cancellation process needs to be run in a batch, either
Form API will invoke it, or batch_process() needs to be invoked after calling
this function and should define the path to redirect to.

@param $edit
  An array of submitted form values.
@param $uid
  The user ID of the user account to cancel.
@param $method
  The account cancellation method to use.

@see _user_cancel()
```

## Code

```php
function user_cancel($edit, $uid, $method) {
  global $user;

  $account = user_load($uid);

  if (!$account) {
    drupal_set_message(t('The user account %id does not exist.', array('%id' => $uid)), 'error');
    watchdog('user', 'Attempted to cancel non-existing user account: %id.', array('%id' => $uid), WATCHDOG_ERROR);
    return;
  }

  // Initialize batch (to set title).
  $batch = array(
    'title' => t('Cancelling account'),
    'operations' => array(),
  );
  batch_set($batch);

  // Modules use hook_user_delete() to respond to deletion.
  if ($method != 'user_cancel_delete') {
    // Allow modules to add further sets to this batch.
    module_invoke_all('user_cancel', $edit, $account, $method);
  }

  // Finish the batch and actually cancel the account.
  $batch = array(
    'title' => t('Cancelling user account'),
    'operations' => array(
      array('_user_cancel', array($edit, $account, $method)),
    ),
  );

  // After cancelling account, ensure that user is logged out.
  if ($account->uid == $user->uid) {
    // Batch API stores data in the session, so use the finished operation to
    // manipulate the current user's session id.
    $batch['finished'] = '_user_cancel_session_regenerate';
  }

  batch_set($batch);

  // Batch processing is either handled via Form API or has to be invoked
  // manually.
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
