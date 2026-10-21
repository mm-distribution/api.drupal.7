# file_field_schema()

- **Type:** Function
- **File:** [`modules/file/file.install`](_file.md), lines 11–44 · [local source](../../../../source/modules/file/file.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.install#L11-L44)
- **Module/theme:** file
- **Implements:** [hook_field_schema()](../../field/field.api.php/hook_field_schema.md)

## Signature

```php
function file_field_schema($field)
```

## Documentation

```text
Implements hook_field_schema().
```

## Code

```php
function file_field_schema($field) {
  return array(
    'columns' => array(
      'fid' => array(
        'description' => 'The {file_managed}.fid being referenced in this field.',
        'type' => 'int',
        'not null' => FALSE,
        'unsigned' => TRUE,
      ),
      'display' => array(
        'description' => 'Flag to control whether this file should be displayed when viewing content.',
        'type' => 'int',
        'size' => 'tiny',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default' => 1,
      ),
      'description' => array(
        'description' => 'A description of the file.',
        'type' => 'text',
        'not null' => FALSE,
      ),
    ),
    'indexes' => array(
      'fid' => array('fid'),
    ),
    'foreign keys' => array(
      'fid' => array(
        'table' => 'file_managed',
        'columns' => array('fid' => 'fid'),
      ),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/file/file.install](https://github.com/drupal/drupal/blob/7.103/modules/file/file.install) · Licensed GPL-2.0-or-later (see LICENSE)._
