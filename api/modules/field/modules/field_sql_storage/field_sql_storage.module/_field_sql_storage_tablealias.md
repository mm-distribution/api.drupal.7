# _field_sql_storage_tablealias()

- **Type:** Function
- **File:** [`modules/field/modules/field_sql_storage/field_sql_storage.module`](_file.md), lines 83–108 · [local source](../../../../../../source/modules/field/modules/field_sql_storage/field_sql_storage.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.module#L83-L108)
- **Module/theme:** field_sql_storage

## Signature

```php
function _field_sql_storage_tablealias($tablename, $field_key, EntityFieldQuery $query)
```

## Documentation

```text
Generates a table alias for a field data table.

The table alias is unique for each unique combination of field name
(represented by $tablename), delta_group and language_group.

@param $tablename
  The name of the data table for this field.
@param $field_key
  The numeric key of this field in this query.
@param $query
  The EntityFieldQuery that is executed.

@return
  A string containing the generated table alias.
```

## Code

```php
function _field_sql_storage_tablealias($tablename, $field_key, EntityFieldQuery $query) {
  // No conditions present: use a unique alias.
  if (empty($query->fieldConditions[$field_key])) {
    return $tablename . $field_key;
  }

  // Find the delta and language condition values and append them to the alias.
  $condition = $query->fieldConditions[$field_key];
  $alias = $tablename;
  $has_group_conditions = FALSE;

  foreach (array('delta', 'language') as $column) {
    if (isset($condition[$column . '_group'])) {
      $alias .= '_' . $column . '_' . $condition[$column . '_group'];
      $has_group_conditions = TRUE;
    }
  }

  // Return the alias when it has delta/language group conditions.
  if ($has_group_conditions) {
    return $alias;
  }

  // Return a unique alias in other cases.
  return $tablename . $field_key;
}
```

---
_Drupal 7.103 · [modules/field/modules/field_sql_storage/field_sql_storage.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.module) · Licensed GPL-2.0-or-later (see LICENSE)._
