# _field_sql_storage_query_field_conditions()

- **Type:** Function
- **File:** [`modules/field/modules/field_sql_storage/field_sql_storage.module`](_file.md), lines 801–822 · [local source](../../../../../../source/modules/field/modules/field_sql_storage/field_sql_storage.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.module#L801-L822)
- **Module/theme:** field_sql_storage

## Signature

```php
function _field_sql_storage_query_field_conditions(EntityFieldQuery $query, SelectQuery $select_query, $conditions, $table_aliases, $column_callback)
```

## Documentation

```text
Adds field (meta) conditions to the given query objects respecting groupings.

@param EntityFieldQuery $query
  The field query object to be processed.
@param SelectQuery $select_query
  The SelectQuery that should get grouping conditions.
@param condtions
  The conditions to be added.
@param $table_aliases
  An associative array of table aliases keyed by field index.
@param $column_callback
  A callback that should return the column name to be used for the field
  conditions. Accepts a field name and a field column name as parameters.
```

## Code

```php
function _field_sql_storage_query_field_conditions(EntityFieldQuery $query, SelectQuery $select_query, $conditions, $table_aliases, $column_callback) {
  $groups = &drupal_static(__FUNCTION__, array());
  foreach ($conditions as $key => $condition) {
    $table_alias = $table_aliases[$key];
    $field = $condition['field'];
    // Add the specified condition.
    $sql_field = "$table_alias." . $column_callback($field['field_name'], $condition['column']);
    $query->addCondition($select_query, $sql_field, $condition);
    // Add delta / language group conditions.
    foreach (array('delta', 'language') as $column) {
      if (isset($condition[$column . '_group'])) {
        $group_name = $condition[$column . '_group'];
        if (!isset($groups[$column][$group_name])) {
          $groups[$column][$group_name] = $table_alias;
        }
        else {
          $select_query->where("$table_alias.$column = " . $groups[$column][$group_name] . ".$column");
        }
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/field/modules/field_sql_storage/field_sql_storage.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.module) · Licensed GPL-2.0-or-later (see LICENSE)._
