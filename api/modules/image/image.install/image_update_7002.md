# image_update_7002()

- **Type:** Function
- **File:** [`modules/image/image.install`](_file.md), lines 356–411 · [local source](../../../../source/modules/image/image.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.install#L356-L411)
- **Module/theme:** image
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function image_update_7002(array &$sandbox)
```

## Documentation

```text
Add width and height columns to image field schema and populate.
```

## Code

```php
function image_update_7002(array &$sandbox) {
  if (empty($sandbox)) {
    // Setup the sandbox.
    $sandbox = array(
      'tables' => array(),
      'total' => 0,
      'processed' => 0,
      'last_fid' => NULL,
    );

    $fields = _update_7000_field_read_fields(array(
      'module' => 'image',
      'storage_type' => 'field_sql_storage',
      'deleted' => 0,
    ));

    foreach ($fields as $field) {
      $tables = array(
        _field_sql_storage_tablename($field),
        _field_sql_storage_revision_tablename($field),
      );
      foreach ($tables as $table) {
        // Add the width and height columns to the table.
        _image_update_7002_add_columns($table, $field['field_name']);

        // How many rows need dimensions populated?
        $count = db_select($table)->countQuery()->execute()->fetchField();

        if (!$count) {
          continue;
        }

        $sandbox['total'] += $count;
        $sandbox['tables'][$table] = $field['field_name'];
      }
    }

    // If no tables need rows populated with dimensions then we are done.
    if (empty($sandbox['tables'])) {
      $sandbox = array();
      return;
    }
  }

  // Process the table at the top of the list.
  $keys = array_keys($sandbox['tables']);
  $table = reset($keys);
  $sandbox['processed'] += _image_update_7002_populate_dimensions($table, $sandbox['tables'][$table], $sandbox['last_fid']);

  // Has the table been fully processed?
  if (!$sandbox['last_fid']) {
    unset($sandbox['tables'][$table]);
  }

  $sandbox['#finished'] = count($sandbox['tables']) ? ($sandbox['processed'] / $sandbox['total']) : 1;
}
```

---
_Drupal 7.103 · [modules/image/image.install](https://github.com/drupal/drupal/blob/7.103/modules/image/image.install) · Licensed GPL-2.0-or-later (see LICENSE)._
