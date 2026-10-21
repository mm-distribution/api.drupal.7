# user_save()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 422–626 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L422-L626)
- **Module/theme:** user

## Signature

```php
function user_save($account, $edit = array(), $category = 'account')
```

## Documentation

```text
Save changes to a user account or add a new user.

@param $account
  (optional) The user object to modify or add. If you want to modify
  an existing user account, you will need to ensure that (a) $account
  is an object, and (b) you have set $account->uid to the numeric
  user ID of the user account you wish to modify. If you
  want to create a new user account, you can set $account->is_new to
  TRUE or omit the $account->uid field.
@param $edit
  An array of fields and values to save. For example array('name'
  => 'My name'). Key / value pairs added to the $edit['data'] will be
  serialized and saved in the {users.data} column.
@param $category
  (optional) The category for storing profile information in.

@return
  A fully-loaded $user object upon successful save or FALSE if the save failed.
```

## Code

```php
function user_save($account, $edit = array(), $category = 'account') {
  $transaction = db_transaction();
  try {
    if (isset($edit['pass']) && strlen(trim($edit['pass'])) > 0) {
      // Allow alternate password hashing schemes.
      require_once DRUPAL_ROOT . '/' . variable_get('password_inc', 'includes/password.inc');
      $edit['pass'] = user_hash_password(trim($edit['pass']));
      // Abort if the hashing failed and returned FALSE.
      if (!$edit['pass']) {
        return FALSE;
      }
    }
    else {
      // Avoid overwriting an existing password with a blank password.
      unset($edit['pass']);
    }
    if (isset($edit['mail'])) {
      $edit['mail'] = trim($edit['mail']);
    }

    // Load the stored entity, if any.
    if (!empty($account->uid) && !isset($account->original)) {
      $account->original = entity_load_unchanged('user', $account->uid);
    }

    if (empty($account)) {
      $account = new stdClass();
    }
    if (!isset($account->is_new)) {
      $account->is_new = empty($account->uid);
    }
    // Prepopulate $edit['data'] with the current value of $account->data.
    // Modules can add to or remove from this array in hook_user_presave().
    if (!empty($account->data)) {
      $edit['data'] = !empty($edit['data']) ? array_merge($account->data, $edit['data']) : $account->data;
    }

    // Invoke hook_user_presave() for all modules.
    user_module_invoke('presave', $edit, $account, $category);

    // Invoke presave operations of Field Attach API and Entity API. Those APIs
    // require a fully-fledged and updated entity object. Therefore, we need to
    // copy any new property values of $edit into it.
    foreach ($edit as $key => $value) {
      $account->$key = $value;
    }
    field_attach_presave('user', $account);
    module_invoke_all('entity_presave', $account, 'user');

    if (is_object($account) && !$account->is_new) {
      // Process picture uploads.
      if (!empty($account->picture->fid) && (!isset($account->original->picture->fid) || $account->picture->fid != $account->original->picture->fid)) {
        $picture = $account->picture;
        // If the picture is a temporary file move it to its final location and
        // make it permanent.
        if (!$picture->status) {
          $info = image_get_info($picture->uri);
          $picture_directory =  file_default_scheme() . '://' . variable_get('user_picture_path', 'pictures');

          // Prepare the pictures directory.
          file_prepare_directory($picture_directory, FILE_CREATE_DIRECTORY);
          $destination = file_stream_wrapper_uri_normalize($picture_directory . '/picture-' . $account->uid . '-' . REQUEST_TIME . '.' . $info['extension']);

          // Move the temporary file into the final location.
          if ($picture = file_move($picture, $destination, FILE_EXISTS_RENAME)) {
            $picture->status = FILE_STATUS_PERMANENT;
            $account->picture = file_save($picture);
            file_usage_add($picture, 'user', 'user', $account->uid);
          }
        }
        // Delete the previous picture if it was deleted or replaced.
        if (!empty($account->original->picture->fid)) {
          file_usage_delete($account->original->picture, 'user', 'user', $account->uid);
          file_delete($account->original->picture);
        }
      }
      elseif (isset($edit['picture_delete']) && $edit['picture_delete']) {
        file_usage_delete($account->original->picture, 'user', 'user', $account->uid);
        file_delete($account->original->picture);
      }
      // Save the picture object, if it is set. drupal_write_record() expects
      // $account->picture to be a FID.
      $picture = empty($account->picture) ? NULL : $account->picture;
      $account->picture = empty($account->picture->fid) ? 0 : $account->picture->fid;

      // Do not allow 'uid' to be changed.
      $account->uid = $account->original->uid;
      // Save current time as last changed time.
      $account->changed = REQUEST_TIME;
      // Save changes to the user table.
      $success = drupal_write_record('users', $account, 'uid');
      // Restore the picture object.
      $account->picture = $picture;
      if ($success === FALSE) {
        // The query failed - better to abort the save than risk further
        // data loss.
        return FALSE;
      }

      // Reload user roles if provided.
      if ($account->roles != $account->original->roles) {
        db_delete('users_roles')
          ->condition('uid', $account->uid)
          ->execute();

        $query = db_insert('users_roles')->fields(array('uid', 'rid'));
        foreach (array_keys($account->roles) as $rid) {
          if (!in_array($rid, array(DRUPAL_ANONYMOUS_RID, DRUPAL_AUTHENTICATED_RID))) {
            $query->values(array(
              'uid' => $account->uid,
              'rid' => $rid,
            ));
          }
        }
        $query->execute();
      }

      // Delete a blocked user's sessions to kick them if they are online.
      if ($account->original->status != $account->status && $account->status == 0) {
        drupal_session_destroy_uid($account->uid);
      }

      // If the password changed, delete all open sessions and recreate
      // the current one.
      if ($account->pass != $account->original->pass) {
        drupal_session_destroy_uid($account->uid);
        if ($account->uid == $GLOBALS['user']->uid) {
          drupal_session_regenerate();
        }
      }

      // Save Field data.
      field_attach_update('user', $account);

      // Send emails after we have the new user object.
      if ($account->status != $account->original->status) {
        // The user's status is changing; conditionally send notification email.
        $op = $account->status == 1 ? 'status_activated' : 'status_blocked';
        _user_mail_notify($op, $account);
      }

      // Update $edit with any interim changes to $account.
      foreach ($account as $key => $value) {
        if (!property_exists($account->original, $key) || $value !== $account->original->$key) {
          $edit[$key] = $value;
        }
      }
      user_module_invoke('update', $edit, $account, $category);
      module_invoke_all('entity_update', $account, 'user');
    }
    else {
      // Allow 'uid' to be set by the caller. There is no danger of writing an
      // existing user as drupal_write_record will do an INSERT.
      if (empty($account->uid)) {
        $account->uid = db_next_id(db_query('SELECT MAX(uid) FROM {users}')->fetchField());
      }
      // Allow 'created' to be set by the caller.
      if (!isset($account->created)) {
        $account->created = REQUEST_TIME;
      }
      // Save current time as last changed time.
      $account->changed = REQUEST_TIME;
      $success = drupal_write_record('users', $account);
      if ($success === FALSE) {
        // On a failed INSERT some other existing user's uid may be returned.
        // We must abort to avoid overwriting their account.
        return FALSE;
      }

      // Make sure $account is properly initialized.
      $account->roles[DRUPAL_AUTHENTICATED_RID] = 'authenticated user';

      field_attach_insert('user', $account);
      $edit = (array) $account;
      user_module_invoke('insert', $edit, $account, $category);
      module_invoke_all('entity_insert', $account, 'user');

      // Save user roles. Skip built-in roles, and ones that were already saved
      // to the database during hook calls.
      $rids_to_skip = array_merge(array(DRUPAL_ANONYMOUS_RID, DRUPAL_AUTHENTICATED_RID), db_query('SELECT rid FROM {users_roles} WHERE uid = :uid', array(':uid' => $account->uid))->fetchCol());
      if ($rids_to_save = array_diff(array_keys($account->roles), $rids_to_skip)) {
        $query = db_insert('users_roles')->fields(array('uid', 'rid'));
        foreach ($rids_to_save as $rid) {
          $query->values(array(
            'uid' => $account->uid,
            'rid' => $rid,
          ));
        }
        $query->execute();
      }
    }
    // Clear internal properties.
    unset($account->is_new);
    unset($account->original);
    // Clear the static loading cache.
    entity_get_controller('user')->resetCache(array($account->uid));

    return $account;
  }
  catch (Exception $e) {
    $transaction->rollback();
    watchdog_exception('user', $e);
    throw $e;
  }
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
