# _field_sql_storage_query_join_entity()

- **Type:** Function
- **File:** [`modules/field/modules/field_sql_storage/field_sql_storage.module`](_file.md), lines 778–784 · [local source](../../../../../../source/modules/field/modules/field_sql_storage/field_sql_storage.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.module#L778-L784)
- **Module/theme:** field_sql_storage

## Signature

```php
function _field_sql_storage_query_join_entity(SelectQuery $select_query, $entity_type, $field_base_table)
```

## Documentation

```text
Adds the base entity table to a field query object.

@param SelectQuery $select_query
  A SelectQuery containing at least one table as specified by
  _field_sql_storage_tablename().
@param $entity_type
  The entity type for which the base table should be joined.
@param $field_base_table
  Name of a table in $select_query. As only INNER JOINs are used, it does
  not matter which.

@return
  The name of the entity base table joined in.
```

## Code

```php
function _field_sql_storage_query_join_entity(SelectQuery $select_query, $entity_type, $field_base_table) {
  $entity_info = entity_get_info($entity_type);
  $entity_base_table = $entity_info['base table'];
  $entity_field = $entity_info['entity keys']['id'];
  $select_query->join($entity_base_table, $entity_base_table, "$entity_base_table.$entity_field = $field_base_table.entity_id");
  return $entity_base_table;
}
```

---
_Drupal 7.103 · [modules/field/modules/field_sql_storage/field_sql_storage.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.module) · Licensed GPL-2.0-or-later (see LICENSE)._
