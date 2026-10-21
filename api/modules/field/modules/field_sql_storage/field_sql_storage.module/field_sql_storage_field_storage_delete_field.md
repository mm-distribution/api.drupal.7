# field_sql_storage_field_storage_delete_field()

- **Type:** Function
- **File:** [`modules/field/modules/field_sql_storage/field_sql_storage.module`](_file.md), lines 380–396 · [local source](../../../../../../source/modules/field/modules/field_sql_storage/field_sql_storage.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.module#L380-L396)
- **Module/theme:** field_sql_storage
- **Implements:** [hook_field_storage_delete_field()](../../../field.api.php/hook_field_storage_delete_field.md)

## Signature

```php
function field_sql_storage_field_storage_delete_field($field)
```

## Documentation

```text
Implements hook_field_storage_delete_field().
```

## Code

```php
function field_sql_storage_field_storage_delete_field($field) {
  // Mark all data associated with the field for deletion.
  $field['deleted'] = 0;
  $table = _field_sql_storage_tablename($field);
  $revision_table = _field_sql_storage_revision_tablename($field);
  db_update($table)
    ->fields(array('deleted' => 1))
    ->execute();

  // Move the table to a unique name while the table contents are being deleted.
  $field['deleted'] = 1;
  $new_table = _field_sql_storage_tablename($field);
  $revision_new_table = _field_sql_storage_revision_tablename($field);
  db_rename_table($table, $new_table);
  db_rename_table($revision_table, $revision_new_table);
  drupal_get_schema(NULL, TRUE);
}
```

---
_Drupal 7.103 · [modules/field/modules/field_sql_storage/field_sql_storage.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.module) · Licensed GPL-2.0-or-later (see LICENSE)._
