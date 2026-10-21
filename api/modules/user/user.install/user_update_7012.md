# user_update_7012()

- **Type:** Function
- **File:** [`modules/user/user.install`](_file.md), lines 722–790 · [local source](../../../../source/modules/user/user.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.install#L722-L790)
- **Module/theme:** user
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function user_update_7012(&$sandbox)
```

## Documentation

```text
Add the user's pictures to the {file_managed} table and make them managed
files.
```

## Code

```php
function user_update_7012(&$sandbox) {

  $picture_field = array(
    'type' => 'int',
    'not null' => TRUE,
    'default' => 0,
    'description' => "Foreign key: {file_managed}.fid of user's picture.",
  );

  if (!isset($sandbox['progress'])) {
    // Check that the field hasn't been updated in an aborted run of this
    // update.
    if (!db_field_exists('users', 'picture_fid')) {
      // Add a new field for the fid.
      db_add_field('users', 'picture_fid', $picture_field);
    }

    // Initialize batch update information.
    $sandbox['progress'] = 0;
    $sandbox['last_user_processed'] = -1;
    $sandbox['max'] = db_query("SELECT COUNT(*) FROM {users} WHERE picture <> ''")->fetchField();
  }

  // As a batch operation move the photos into the {file_managed} table and
  // update the {users} records.
  $limit = 500;
  $result = db_query_range("SELECT uid, picture FROM {users} WHERE picture <> '' AND uid > :uid ORDER BY uid", 0, $limit, array(':uid' => $sandbox['last_user_processed']));
  foreach ($result as $user) {
    // Don't bother adding files that don't exist.
    if (file_exists($user->picture)) {

      // Check if the file already exists.
      $files = file_load_multiple(array(), array('uri' => $user->picture));
      if (count($files)) {
        $file = reset($files);
      }
      else {
        // Create a file object.
        $file = new stdClass();
        $file->uri      = $user->picture;
        $file->filename = drupal_basename($file->uri);
        $file->filemime = file_get_mimetype($file->uri);
        $file->uid      = $user->uid;
        $file->status   = FILE_STATUS_PERMANENT;
        $file = file_save($file);
      }

      db_update('users')
        ->fields(array('picture_fid' => $file->fid))
        ->condition('uid', $user->uid)
        ->execute();
    }

    // Update our progress information for the batch update.
    $sandbox['progress']++;
    $sandbox['last_user_processed'] = $user->uid;
  }

  // Indicate our current progress to the batch update system. If there's no
  // max value then there's nothing to update and we're finished.
  $sandbox['#finished'] = empty($sandbox['max']) ? 1 : ($sandbox['progress'] / $sandbox['max']);

  // When we're finished, drop the old picture field and rename the new one to
  // replace it.
  if (isset($sandbox['#finished']) && $sandbox['#finished'] == 1) {
    db_drop_field('users', 'picture');
    db_change_field('users', 'picture_fid', 'picture', $picture_field);
  }
}
```

---
_Drupal 7.103 · [modules/user/user.install](https://github.com/drupal/drupal/blob/7.103/modules/user/user.install) · Licensed GPL-2.0-or-later (see LICENSE)._
