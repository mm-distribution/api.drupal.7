# _field_sql_storage_indexname()

- **Type:** Function
- **File:** [`modules/field/modules/field_sql_storage/field_sql_storage.module`](_file.md), lines 136–138 · [local source](../../../../../../source/modules/field/modules/field_sql_storage/field_sql_storage.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.module#L136-L138)
- **Module/theme:** field_sql_storage

## Signature

```php
function _field_sql_storage_indexname($name, $index)
```

## Documentation

```text
Generate an index name for a field data table.

@param $name
  The name of the field
@param $column
  The name of the index
@return
  A string containing a generated index name for a field data
  table that is unique among all other fields.
```

## Code

```php
function _field_sql_storage_indexname($name, $index) {
  return $name . '_' . $index;
}
```

---
_Drupal 7.103 · [modules/field/modules/field_sql_storage/field_sql_storage.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.module) · Licensed GPL-2.0-or-later (see LICENSE)._
