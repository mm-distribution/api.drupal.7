# system_update_7059()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 2731–2778 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L2731-L2778)
- **Module/theme:** system
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function system_update_7059()
```

## Documentation

```text
Create the {file_usage} table.
```

## Code

```php
function system_update_7059() {
  $spec = array(
    'description' => 'Track where a file is used.',
    'fields' => array(
      'fid' => array(
        'description' => 'File ID.',
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
      ),
      'module' => array(
        'description' => 'The name of the module that is using the file.',
        'type' => 'varchar',
        'length' => 255,
        'not null' => TRUE,
        'default' => '',
      ),
      'type' => array(
        'description' => 'The name of the object type in which the file is used.',
        'type' => 'varchar',
        'length' => 64,
        'not null' => TRUE,
        'default' => '',
      ),
      'id' => array(
        'description' => 'The primary key of the object using the file.',
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default' => 0,
      ),
      'count' => array(
        'description' => 'The number of times this file is used by this object.',
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default' => 0,
      ),
    ),
    'primary key' => array('fid', 'type', 'id', 'module'),
    'indexes' => array(
      'type_id' => array('type', 'id'),
      'fid_count' => array('fid', 'count'),
      'fid_module' => array('fid', 'module'),
    ),
  );
  db_create_table('file_usage', $spec);
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
