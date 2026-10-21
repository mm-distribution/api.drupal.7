# _field_sql_storage_query_columnname()

- **Type:** Function
- **File:** [`modules/field/modules/field_sql_storage/field_sql_storage.module`](_file.md), lines 827–829 · [local source](../../../../../../source/modules/field/modules/field_sql_storage/field_sql_storage.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.module#L827-L829)
- **Module/theme:** field_sql_storage

## Signature

```php
function _field_sql_storage_query_columnname($field_name, $column)
```

## Documentation

```text
Field meta condition column callback.
```

## Code

```php
function _field_sql_storage_query_columnname($field_name, $column) {
  return $column;
}
```

---
_Drupal 7.103 · [modules/field/modules/field_sql_storage/field_sql_storage.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.module) · Licensed GPL-2.0-or-later (see LICENSE)._
