# field_sql_storage_field_storage_query()

- **Type:** Function
- **File:** [`modules/field/modules/field_sql_storage/field_sql_storage.module`](_file.md), lines 668–761 · [local source](../../../../../../source/modules/field/modules/field_sql_storage/field_sql_storage.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.module#L668-L761)
- **Module/theme:** field_sql_storage
- **Implements:** [hook_field_storage_query()](../../../field.api.php/hook_field_storage_query.md)

## Signature

```php
function field_sql_storage_field_storage_query(EntityFieldQuery $query)
```

## Documentation

```text
Implements hook_field_storage_query().
```

## Code

```php
function field_sql_storage_field_storage_query(EntityFieldQuery $query) {
  if ($query->age == FIELD_LOAD_CURRENT) {
    $tablename_function = '_field_sql_storage_tablename';
    $id_key = 'entity_id';
  }
  else {
    $tablename_function = '_field_sql_storage_revision_tablename';
    $id_key = 'revision_id';
  }
  $table_aliases = array();
  $query_tables = NULL;
  // Add tables for the fields used.
  foreach ($query->fields as $key => $field) {
    $tablename = $tablename_function($field);
    $table_alias = _field_sql_storage_tablealias($tablename, $key, $query);
    $table_aliases[$key] = $table_alias;
    if ($key) {
      if (!isset($query_tables[$table_alias])) {
        $select_query->join($tablename, $table_alias, "$table_alias.entity_type = $field_base_table.entity_type AND $table_alias.$id_key = $field_base_table.$id_key");
      }
    }
    else {
      $select_query = db_select($tablename, $table_alias);
      // Store a reference to the list of joined tables.
      $query_tables =& $select_query->getTables();
      // Allow queries internal to the Field API to opt out of the access
      // check, for situations where the query's results should not depend on
      // the access grants for the current user.
      if (!isset($query->tags['DANGEROUS_ACCESS_CHECK_OPT_OUT'])) {
        $select_query->addTag('entity_field_access');
      }
      $select_query->addMetaData('base_table', $tablename);
      $select_query->fields($table_alias, array('entity_type', 'entity_id', 'revision_id', 'bundle'));
      $field_base_table = $table_alias;
    }
    if ($field['cardinality'] != 1 || $field['translatable']) {
      $select_query->distinct();
    }
  }

  // Add field conditions. We need a fresh grouping cache.
  drupal_static_reset('_field_sql_storage_query_field_conditions');
  _field_sql_storage_query_field_conditions($query, $select_query, $query->fieldConditions, $table_aliases, '_field_sql_storage_columnname');

  // Add field meta conditions.
  _field_sql_storage_query_field_conditions($query, $select_query, $query->fieldMetaConditions, $table_aliases, '_field_sql_storage_query_columnname');

  if (isset($query->deleted)) {
    $select_query->condition("$field_base_table.deleted", (int) $query->deleted);
  }

  // Is there a need to sort the query by property?
  $has_property_order = FALSE;
  foreach ($query->order as $order) {
    if ($order['type'] == 'property') {
      $has_property_order = TRUE;
    }
  }

  if ($query->propertyConditions || $has_property_order) {
    if (empty($query->entityConditions['entity_type']['value'])) {
      throw new EntityFieldQueryException('Property conditions and orders must have an entity type defined.');
    }
    $entity_type = $query->entityConditions['entity_type']['value'];
    $entity_base_table = _field_sql_storage_query_join_entity($select_query, $entity_type, $field_base_table);
    $query->entityConditions['entity_type']['operator'] = '=';
    foreach ($query->propertyConditions as $property_condition) {
      $query->addCondition($select_query, "$entity_base_table." . $property_condition['column'], $property_condition);
    }
  }
  foreach ($query->entityConditions as $key => $condition) {
    $query->addCondition($select_query, "$field_base_table.$key", $condition);
  }

  // Order the query.
  foreach ($query->order as $order) {
    if ($order['type'] == 'entity') {
      $key = $order['specifier'];
      $select_query->orderBy("$field_base_table.$key", $order['direction']);
    }
    elseif ($order['type'] == 'field') {
      $specifier = $order['specifier'];
      $field = $specifier['field'];
      $table_alias = $table_aliases[$specifier['index']];
      $sql_field = "$table_alias." . _field_sql_storage_columnname($field['field_name'], $specifier['column']);
      $select_query->orderBy($sql_field, $order['direction']);
    }
    elseif ($order['type'] == 'property') {
      $select_query->orderBy("$entity_base_table." . $order['specifier'], $order['direction']);
    }
  }

  return $query->finishQuery($select_query, $id_key);
}
```

---
_Drupal 7.103 · [modules/field/modules/field_sql_storage/field_sql_storage.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.module) · Licensed GPL-2.0-or-later (see LICENSE)._
