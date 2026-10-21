# system_update_files_database()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 2268–2345 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L2268-L2345)
- **Module/theme:** system

## Signature

```php
function system_update_files_database(&$files, $type)
```

## Documentation

```text
Updates the records in the system table based on the files array.

@param $files
  An array of files.
@param $type
  The type of the files.
```

## Code

```php
function system_update_files_database(&$files, $type) {
  $result = db_query("SELECT * FROM {system} WHERE type = :type", array(':type' => $type));

  // Add all files that need to be deleted to a DatabaseCondition.
  $delete = db_or();
  foreach ($result as $file) {
    if (isset($files[$file->name]) && is_object($files[$file->name])) {
      // Keep the old filename from the database in case the file has moved.
      $old_filename = $file->filename;

      $updated_fields = array();

      // Handle info specially, compare the serialized value.
      $serialized_info = serialize($files[$file->name]->info);
      if ($serialized_info != $file->info) {
        $updated_fields['info'] = $serialized_info;
      }
      unset($file->info);

      // Scan remaining fields to find only the updated values.
      foreach ($file as $key => $value) {
        if (isset($files[$file->name]->$key) && $files[$file->name]->$key != $value) {
          $updated_fields[$key] = $files[$file->name]->$key;
        }
      }

      // Update the record.
      if (count($updated_fields)) {
        db_update('system')
          ->fields($updated_fields)
          ->condition('filename', $old_filename)
          ->execute();
      }

      // Indicate that the file exists already.
      $files[$file->name]->exists = TRUE;
    }
    else {
      // File is not found in file system, so delete record from the system table.
      $delete->condition('filename', $file->filename);
    }
  }

  if (count($delete) > 0) {
    // Delete all missing files from the system table, but only if the plugin
    // has never been installed.
    db_delete('system')
      ->condition($delete)
      ->condition('schema_version', -1)
      ->execute();
  }

  // All remaining files are not in the system table, so we need to add them.
  $query = db_insert('system')->fields(array('filename', 'name', 'type', 'owner', 'info'));
  foreach ($files as &$file) {
    if (isset($file->exists)) {
      unset($file->exists);
    }
    else {
      $query->values(array(
        'filename' => $file->uri,
        'name' => $file->name,
        'type' => $type,
        'owner' => isset($file->owner) ? $file->owner : '',
        'info' => serialize($file->info),
      ));
      $file->type = $type;
      $file->status = 0;
      $file->schema_version = -1;
    }
  }
  $query->execute();

  // If any module or theme was moved to a new location, we need to reset the
  // system_list() cache or we will continue to load the old copy, look for
  // schema updates in the wrong place, etc.
  system_list_reset();
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
