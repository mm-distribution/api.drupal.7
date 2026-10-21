# _field_sql_storage_columnname()

- **Type:** Function
- **File:** [`modules/field/modules/field_sql_storage/field_sql_storage.module`](_file.md), lines 121–123 · [local source](../../../../../../source/modules/field/modules/field_sql_storage/field_sql_storage.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.module#L121-L123)
- **Module/theme:** field_sql_storage

## Signature

```php
function _field_sql_storage_columnname($name, $column)
```

## Documentation

```text
Generate a column name for a field data table.

@param $name
  The name of the field
@param $column
  The name of the column
@return
  A string containing a generated column name for a field data
  table that is unique among all other fields.
```

## Code

```php
function _field_sql_storage_columnname($name, $column) {
  return $name . '_' . $column;
}
```

---
_Drupal 7.103 · [modules/field/modules/field_sql_storage/field_sql_storage.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.module) · Licensed GPL-2.0-or-later (see LICENSE)._
