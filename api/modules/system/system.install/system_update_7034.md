# system_update_7034()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 2326–2415 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L2326-L2415)
- **Module/theme:** system
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function system_update_7034()
```

## Documentation

```text
Migrate the file path settings and create the new {file_managed} table.
```

## Code

```php
function system_update_7034() {
  $files_directory = variable_get('file_directory_path', NULL);
  if (variable_get('file_downloads', 1) == 1) {
    // Our default is public, so we don't need to set anything.
    if (!empty($files_directory)) {
      variable_set('file_public_path', $files_directory);
    }
  }
  elseif (variable_get('file_downloads', 1) == 2) {
    variable_set('file_default_scheme', 'private');
    if (!empty($files_directory)) {
      variable_set('file_private_path', $files_directory);
    }
  }
  variable_del('file_downloads');

  $schema['file_managed'] = array(
    'description' => 'Stores information for uploaded files.',
    'fields' => array(
      'fid' => array(
        'description' => 'File ID.',
        'type' => 'serial',
        'unsigned' => TRUE,
        'not null' => TRUE,
      ),
      'uid' => array(
        'description' => 'The {user}.uid of the user who is associated with the file.',
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default' => 0,
      ),
      'filename' => array(
        'description' => 'Name of the file with no path components. This may differ from the basename of the filepath if the file is renamed to avoid overwriting an existing file.',
        'type' => 'varchar',
        'length' => 255,
        'not null' => TRUE,
        'default' => '',
        'binary' => TRUE,
      ),
      'uri' => array(
        'description' => 'URI of file.',
        'type' => 'varchar',
        'length' => 255,
        'not null' => TRUE,
        'default' => '',
        'binary' => TRUE,
      ),
      'filemime' => array(
        'description' => "The file's MIME type.",
        'type' => 'varchar',
        'length' => 255,
        'not null' => TRUE,
        'default' => '',
      ),
      'filesize' => array(
        'description' => 'The size of the file in bytes.',
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default' => 0,
      ),
      'status' => array(
        'description' => 'A field indicating the status of the file. Two status are defined in core: temporary (0) and permanent (1). Temporary files older than DRUPAL_MAXIMUM_TEMP_FILE_AGE will be removed during a cron run.',
        'type' => 'int',
        'not null' => TRUE,
        'default' => 0,
        'size' => 'tiny',
      ),
      'timestamp' => array(
        'description' => 'UNIX timestamp for when the file was added.',
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default' => 0,
      ),
    ),
    'indexes' => array(
      'uid' => array('uid'),
      'status' => array('status'),
      'timestamp' => array('timestamp'),
    ),
    'unique keys' => array(
      'uri' => array('uri'),
    ),
    'primary key' => array('fid'),
  );

  db_create_table('file_managed', $schema['file_managed']);
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
