# _update_7000_field_create_field()

- **Type:** Function
- **File:** [`modules/field/field.install`](_file.md), lines 178–241 · [local source](../../../../source/modules/field/field.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.install#L178-L241)
- **Module/theme:** field
- **Topics:** [update_api](../../../topics/update_api.md)

## Signature

```php
function _update_7000_field_create_field(&$field)
```

## Documentation

```text
Utility function: create a field by writing directly to the database.

This function can be used for databases whose schema is at field module
version 7000 or higher.

@ingroup update_api
```

## Code

```php
function _update_7000_field_create_field(&$field) {
  // Merge in default values.`
  $field += array(
    'entity_types' => array(),
    'cardinality' => 1,
    'translatable' => FALSE,
    'locked' => FALSE,
    'settings' => array(),
    'indexes' => array(),
    'deleted' => 0,
    'active' => 1,
  );

  // Set storage.
  $field['storage'] = array(
    'type' => 'field_sql_storage',
    'settings' => array(),
    'module' => 'field_sql_storage',
    'active' => 1,
  );

  // Fetch the field schema to initialize columns and indexes. The field module
  // is not guaranteed to be loaded at this point.
  module_load_install($field['module']);
  $schema = (array) module_invoke($field['module'], 'field_schema', $field);
  $schema += array('columns' => array(), 'indexes' => array());
  // 'columns' are hardcoded in the field type.
  $field['columns'] = $schema['columns'];
  // 'indexes' can be both hardcoded in the field type, and specified in the
  // incoming $field definition.
  $field['indexes'] += $schema['indexes'];

  // The serialized 'data' column contains everything from $field that does not
  // have its own column and is not automatically populated when the field is
  // read.
  $data = $field;
  unset($data['columns'], $data['field_name'], $data['type'], $data['active'], $data['module'], $data['storage_type'], $data['storage_active'], $data['storage_module'], $data['locked'], $data['cardinality'], $data['deleted']);
  // Additionally, do not save the 'bundles' property populated by
  // field_info_field().
  unset($data['bundles']);

  // Write the field to the database.
  $record = array(
    'field_name' => $field['field_name'],
    'type' => $field['type'],
    'module' => $field['module'],
    'active' => (int) $field['active'],
    'storage_type' => $field['storage']['type'],
    'storage_module' => $field['storage']['module'],
    'storage_active' => (int) $field['storage']['active'],
    'locked' => (int) $field['locked'],
    'data' => serialize($data),
    'cardinality' => $field['cardinality'],
    'translatable' => (int) $field['translatable'],
    'deleted' => (int) $field['deleted'],
  );
  // We don't use drupal_write_record() here because it depends on the schema.
  $field['id'] = db_insert('field_config')
    ->fields($record)
    ->execute();

  // Create storage for the field.
  field_sql_storage_field_storage_create_field($field);
}
```

---
_Drupal 7.103 · [modules/field/field.install](https://github.com/drupal/drupal/blob/7.103/modules/field/field.install) · Licensed GPL-2.0-or-later (see LICENSE)._
