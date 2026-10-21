# field_sql_storage_field_storage_update_field()

- **Type:** Function
- **File:** [`modules/field/modules/field_sql_storage/field_sql_storage.module`](_file.md), lines 301–375 · [local source](../../../../../../source/modules/field/modules/field_sql_storage/field_sql_storage.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.module#L301-L375)
- **Module/theme:** field_sql_storage
- **Implements:** [hook_field_storage_update_field()](../../../field.api.php/hook_field_storage_update_field.md)

## Signature

```php
function field_sql_storage_field_storage_update_field($field, $prior_field, $has_data)
```

## Documentation

```text
Implements hook_field_storage_update_field().
```

## Code

```php
function field_sql_storage_field_storage_update_field($field, $prior_field, $has_data) {
  if (! $has_data) {
    // There is no data. Re-create the tables completely.

    if (Database::getConnection()->supportsTransactionalDDL()) {
      // If the database supports transactional DDL, we can go ahead and rely
      // on it. If not, we will have to rollback manually if something fails.
      $transaction = db_transaction();
    }

    try {
      $prior_schema = _field_sql_storage_schema($prior_field);
      foreach ($prior_schema as $name => $table) {
        db_drop_table($name, $table);
      }
      $schema = _field_sql_storage_schema($field);
      foreach ($schema as $name => $table) {
        db_create_table($name, $table);
      }
    }
    catch (Exception $e) {
      if (Database::getConnection()->supportsTransactionalDDL()) {
        $transaction->rollback();
      }
      else {
        // Recreate tables.
        $prior_schema = _field_sql_storage_schema($prior_field);
        foreach ($prior_schema as $name => $table) {
          if (!db_table_exists($name)) {
            db_create_table($name, $table);
          }
        }
      }
      throw $e;
    }
  }
  else {
    // There is data, so there are no column changes. Drop all the
    // prior indexes and create all the new ones, except for all the
    // priors that exist unchanged.
    $table = _field_sql_storage_tablename($prior_field);
    $revision_table = _field_sql_storage_revision_tablename($prior_field);
    foreach ($prior_field['indexes'] as $name => $columns) {
      if (!isset($field['indexes'][$name]) || $columns != $field['indexes'][$name]) {
        $real_name = _field_sql_storage_indexname($field['field_name'], $name);
        db_drop_index($table, $real_name);
        db_drop_index($revision_table, $real_name);
      }
    }
    $table = _field_sql_storage_tablename($field);
    $revision_table = _field_sql_storage_revision_tablename($field);
    foreach ($field['indexes'] as $name => $columns) {
      if (!isset($prior_field['indexes'][$name]) || $columns != $prior_field['indexes'][$name]) {
        $real_name = _field_sql_storage_indexname($field['field_name'], $name);
        $real_columns = array();
        foreach ($columns as $column_name) {
          // Indexes can be specified as either a column name or an array with
          // column name and length. Allow for either case.
          if (is_array($column_name)) {
            $real_columns[] = array(
              _field_sql_storage_columnname($field['field_name'], $column_name[0]),
              $column_name[1],
            );
          }
          else {
            $real_columns[] = _field_sql_storage_columnname($field['field_name'], $column_name);
          }
        }
        db_add_index($table, $real_name, $real_columns);
        db_add_index($revision_table, $real_name, $real_columns);
      }
    }
  }
  drupal_get_schema(NULL, TRUE);
}
```

---
_Drupal 7.103 · [modules/field/modules/field_sql_storage/field_sql_storage.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.module) · Licensed GPL-2.0-or-later (see LICENSE)._
