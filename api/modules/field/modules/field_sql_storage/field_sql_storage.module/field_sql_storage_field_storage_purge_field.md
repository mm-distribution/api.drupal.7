# field_sql_storage_field_storage_purge_field()

- **Type:** Function
- **File:** [`modules/field/modules/field_sql_storage/field_sql_storage.module`](_file.md), lines 904–909 · [local source](../../../../../../source/modules/field/modules/field_sql_storage/field_sql_storage.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.module#L904-L909)
- **Module/theme:** field_sql_storage
- **Implements:** [hook_field_storage_purge_field()](../../../field.api.php/hook_field_storage_purge_field.md)

## Signature

```php
function field_sql_storage_field_storage_purge_field($field)
```

## Documentation

```text
Implements hook_field_storage_purge_field().

All field data items and instances have already been purged, so all
that is left is to delete the table.
```

## Code

```php
function field_sql_storage_field_storage_purge_field($field) {
  $table_name = _field_sql_storage_tablename($field);
  $revision_name = _field_sql_storage_revision_tablename($field);
  db_drop_table($table_name);
  db_drop_table($revision_name);
}
```

---
_Drupal 7.103 · [modules/field/modules/field_sql_storage/field_sql_storage.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.module) · Licensed GPL-2.0-or-later (see LICENSE)._
