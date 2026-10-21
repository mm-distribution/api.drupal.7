# _field_sql_storage_schema()

- **Type:** Function
- **File:** [`modules/field/modules/field_sql_storage/field_sql_storage.module`](_file.md), lines 151–273 · [local source](../../../../../../source/modules/field/modules/field_sql_storage/field_sql_storage.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.module#L151-L273)
- **Module/theme:** field_sql_storage

## Signature

```php
function _field_sql_storage_schema($field)
```

## Documentation

```text
Return the database schema for a field. This may contain one or
more tables. Each table will contain the columns relevant for the
specified field. Leave the $field's 'columns' and 'indexes' keys
empty to get only the base schema.

@param $field
  The field structure for which to generate a database schema.
@return
  One or more tables representing the schema for the field.
```

## Code

```php
function _field_sql_storage_schema($field) {
  $deleted = $field['deleted'] ? 'deleted ' : '';
  $current = array(
    'description' => "Data storage for {$deleted}field {$field['id']} ({$field['field_name']})",
    'fields' => array(
      'entity_type' => array(
        'type' => 'varchar',
        'length' => 128,
        'not null' => TRUE,
        'default' => '',
        'description' => 'The entity type this data is attached to',
      ),
      'bundle' => array(
        'type' => 'varchar',
        'length' => 128,
        'not null' => TRUE,
        'default' => '',
        'description' => 'The field instance bundle to which this row belongs, used when deleting a field instance',
      ),
      'deleted' => array(
        'type' => 'int',
        'size' => 'tiny',
        'not null' => TRUE,
        'default' => 0,
        'description' => 'A boolean indicating whether this data item has been deleted'
      ),
      'entity_id' => array(
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'description' => 'The entity id this data is attached to',
      ),
      'revision_id' => array(
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => FALSE,
        'description' => 'The entity revision id this data is attached to, or NULL if the entity type is not versioned',
      ),
      // @todo Consider storing language as integer.
      'language' => array(
        'type' => 'varchar',
        'length' => 32,
        'not null' => TRUE,
        'default' => '',
        'description' => 'The language for this data item.',
      ),
      'delta' => array(
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'description' => 'The sequence number for this data item, used for multi-value fields',
      ),
    ),
    'primary key' => array('entity_type', 'entity_id', 'deleted', 'delta', 'language'),
    'indexes' => array(
      'entity_type' => array('entity_type'),
      'bundle' => array('bundle'),
      'deleted' => array('deleted'),
      'entity_id' => array('entity_id'),
      'revision_id' => array('revision_id'),
      'language' => array('language'),
    ),
  );

  // If the target entity type uses a string for its entity ID then update
  // the fields entity_id and revision_id columns from INT to VARCHAR.
  if (!empty($field['entity_id_type']) && $field['entity_id_type'] === 'string') {
    $current['fields']['entity_id']['type'] = 'varchar';
    $current['fields']['entity_id']['length'] = 128;
    unset($current['fields']['entity_id']['unsigned']);

    $current['fields']['revision_id']['type'] = 'varchar';
    $current['fields']['revision_id']['length'] = 128;
    unset($current['fields']['revision_id']['unsigned']);
  }

  $field += array('columns' => array(), 'indexes' => array(), 'foreign keys' => array());
  // Add field columns.
  foreach ($field['columns'] as $column_name => $attributes) {
    $real_name = _field_sql_storage_columnname($field['field_name'], $column_name);
    $current['fields'][$real_name] = $attributes;
  }

  // Add indexes.
  foreach ($field['indexes'] as $index_name => $columns) {
    $real_name = _field_sql_storage_indexname($field['field_name'], $index_name);
    foreach ($columns as $column_name) {
      // Indexes can be specified as either a column name or an array with
      // column name and length. Allow for either case.
      if (is_array($column_name)) {
        $current['indexes'][$real_name][] = array(
          _field_sql_storage_columnname($field['field_name'], $column_name[0]),
          $column_name[1],
        );
      }
      else {
        $current['indexes'][$real_name][] = _field_sql_storage_columnname($field['field_name'], $column_name);
      }
    }
  }

  // Add foreign keys.
  foreach ($field['foreign keys'] as $specifier => $specification) {
    $real_name = _field_sql_storage_indexname($field['field_name'], $specifier);
    $current['foreign keys'][$real_name]['table'] = $specification['table'];
    foreach ($specification['columns'] as $column_name => $referenced) {
      $sql_storage_column = _field_sql_storage_columnname($field['field_name'], $column_name);
      $current['foreign keys'][$real_name]['columns'][$sql_storage_column] = $referenced;
    }
  }

  // Construct the revision table.
  $revision = $current;
  $revision['description'] = "Revision archive storage for {$deleted}field {$field['id']} ({$field['field_name']})";
  $revision['primary key'] = array('entity_type', 'entity_id', 'revision_id', 'deleted', 'delta', 'language');
  $revision['fields']['revision_id']['not null'] = TRUE;
  $revision['fields']['revision_id']['description'] = 'The entity revision id this data is attached to';

  return array(
    _field_sql_storage_tablename($field) => $current,
    _field_sql_storage_revision_tablename($field) => $revision,
  );
}
```

---
_Drupal 7.103 · [modules/field/modules/field_sql_storage/field_sql_storage.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.module) · Licensed GPL-2.0-or-later (see LICENSE)._
