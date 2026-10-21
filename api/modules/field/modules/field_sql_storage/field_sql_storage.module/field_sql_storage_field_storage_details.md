# field_sql_storage_field_storage_details()

- **Type:** Function
- **File:** [`modules/field/modules/field_sql_storage/field_sql_storage.module`](_file.md), lines 914–933 · [local source](../../../../../../source/modules/field/modules/field_sql_storage/field_sql_storage.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.module#L914-L933)
- **Module/theme:** field_sql_storage
- **Implements:** [hook_field_storage_details()](../../../field.api.php/hook_field_storage_details.md)

## Signature

```php
function field_sql_storage_field_storage_details($field)
```

## Documentation

```text
Implements hook_field_storage_details().
```

## Code

```php
function field_sql_storage_field_storage_details($field) {
  $details = array();
  if (!empty($field['columns'])) {
     // Add field columns.
    foreach ($field['columns'] as $column_name => $attributes) {
      $real_name = _field_sql_storage_columnname($field['field_name'], $column_name);
      $columns[$column_name] = $real_name;
    }
    return array(
      'sql' => array(
        FIELD_LOAD_CURRENT => array(
          _field_sql_storage_tablename($field) => $columns,
        ),
        FIELD_LOAD_REVISION => array(
          _field_sql_storage_revision_tablename($field) => $columns,
        ),
      ),
    );
  }
}
```

---
_Drupal 7.103 · [modules/field/modules/field_sql_storage/field_sql_storage.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.module) · Licensed GPL-2.0-or-later (see LICENSE)._
