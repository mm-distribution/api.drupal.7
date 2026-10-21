# system_get_files_database()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 2245–2258 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L2245-L2258)
- **Module/theme:** system

## Signature

```php
function system_get_files_database(&$files, $type)
```

## Documentation

```text
Retrieves the current status of an array of files in the system table.

@param $files
  An array of files to check.
@param $type
  The type of the files.
```

## Code

```php
function system_get_files_database(&$files, $type) {
  // Extract current files from database.
  $result = db_query("SELECT filename, name, type, status, schema_version, weight FROM {system} WHERE type = :type", array(':type' => $type));
  foreach ($result as $file) {
    if (isset($files[$file->name]) && is_object($files[$file->name])) {
      $file->uri = $file->filename;
      foreach ($file as $key => $value) {
        if (!isset($files[$file->name]->$key)) {
          $files[$file->name]->$key = $value;
        }
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
