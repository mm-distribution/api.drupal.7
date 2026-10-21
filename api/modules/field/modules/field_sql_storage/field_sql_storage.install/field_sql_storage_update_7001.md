# field_sql_storage_update_7001()

- **Type:** Function
- **File:** [`modules/field/modules/field_sql_storage/field_sql_storage.install`](_file.md), lines 105–192 · [local source](../../../../../../source/modules/field/modules/field_sql_storage/field_sql_storage.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.install#L105-L192)
- **Module/theme:** field_sql_storage
- **Topics:** [updates-6.x-to-7.x](../../../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function field_sql_storage_update_7001(&$sandbox)
```

## Documentation

```text
Remove the field_config_entity_type table and store 'entity_type' strings.
```

## Code

```php
function field_sql_storage_update_7001(&$sandbox) {
  if (!isset($sandbox['progress'])) {
    // Collect current etids.
    $sandbox['etids'] = db_query('SELECT etid, type FROM {field_config_entity_type}')->fetchAllKeyed();

    // Collect affected tables: field data, field revision data, 'deleted'
    // tables.
    $sandbox['tables'] = array();
    $results = db_select('field_config', 'fc', array('fetch' => PDO::FETCH_ASSOC))
      ->fields('fc')
      ->condition('storage_module', 'field_sql_storage')
      ->execute();
    foreach ($results as $field) {
      if ($field['deleted']) {
        $sandbox['tables']["field_deleted_data_{$field['id']}"] = 'data';
        $sandbox['tables']["field_deleted_revision_{$field['id']}"] = 'revision';
      }
      else {
        $sandbox['tables']["field_data_{$field['field_name']}"] = 'data';
        $sandbox['tables']["field_revision_{$field['field_name']}"] = 'revision';
      }
    }
    reset($sandbox['tables']);

    $sandbox['total'] = count($sandbox['tables']);
    $sandbox['progress'] = 0;
  }

  if ($sandbox['tables']) {
    // Grab the next table to process.
    $table = key($sandbox['tables']);
    $type = array_shift($sandbox['tables']);

    if (db_table_exists($table)) {
      // Add the 'entity_type' column.
      if (!db_field_exists($table, 'entity_type')) {
        $column = array(
          'type' => 'varchar',
          'length' => 128,
          'not null' => TRUE,
          'default' => '',
          'description' => 'The entity type this data is attached to.',
        );
        db_add_field($table, 'entity_type', $column);

        // Populate the 'entity_type' column based on the 'etid' column.
        foreach ($sandbox['etids'] as $etid => $entity_type) {
          db_update($table)
            ->fields(array('entity_type' => $entity_type))
            ->condition('etid', $etid)
            ->execute();
        }

        // Index the new column.
        db_add_index($table, 'entity_type', array('entity_type'));
      }

      // Use the 'entity_type' column in the primary key.
      db_drop_primary_key($table);
      $primary_keys = array(
        'data' => array('entity_type', 'entity_id', 'deleted', 'delta', 'language'),
        'revision' => array('entity_type', 'entity_id', 'revision_id', 'deleted', 'delta', 'language'),
      );
      db_add_primary_key($table, $primary_keys[$type]);

      // Drop the 'etid' column.
      if (db_field_exists($table, 'etid')) {
        db_drop_field($table, 'etid');
      }
    }

    // Report progress.
    $sandbox['progress']++;
    $sandbox['#finished'] = min(0.99, $sandbox['progress'] / $sandbox['total']);
  }
  else {
    // No more tables left: drop the field_config_entity_type table.
    db_drop_table('field_config_entity_type');

    // Drop the previous 'field_sql_storage_ENTITYTYPE_etid' system variables.
    foreach ($sandbox['etids'] as $etid => $entity_type) {
      variable_del('field_sql_storage_' . $entity_type . '_etid');
    }

    // We're done.
    $sandbox['#finished'] = 1;
  }
}
```

---
_Drupal 7.103 · [modules/field/modules/field_sql_storage/field_sql_storage.install](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.install) · Licensed GPL-2.0-or-later (see LICENSE)._
