# _field_sql_storage_revision_tablename()

- **Type:** Function
- **File:** [`modules/field/modules/field_sql_storage/field_sql_storage.module`](_file.md), lines 58–65 · [local source](../../../../../../source/modules/field/modules/field_sql_storage/field_sql_storage.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.module#L58-L65)
- **Module/theme:** field_sql_storage

## Signature

```php
function _field_sql_storage_revision_tablename($field)
```

## Documentation

```text
Generate a table name for a field revision archive table.

@param $name
  The field structure.
@return
  A string containing the generated name for the database table
```

## Code

```php
function _field_sql_storage_revision_tablename($field) {
  if ($field['deleted']) {
    return "field_deleted_revision_{$field['id']}";
  }
  else {
    return "field_revision_{$field['field_name']}";
  }
}
```

---
_Drupal 7.103 · [modules/field/modules/field_sql_storage/field_sql_storage.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.module) · Licensed GPL-2.0-or-later (see LICENSE)._
