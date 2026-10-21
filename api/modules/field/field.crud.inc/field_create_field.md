# field_create_field()

- **Type:** Function
- **File:** [`modules/field/field.crud.inc`](_file.md), lines 76–216 · [local source](../../../../source/modules/field/field.crud.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.crud.inc#L76-L216)
- **Module/theme:** field
- **Topics:** [field_crud](../../../topics/field_crud.md)

## Signature

```php
function field_create_field($field)
```

## Documentation

```text
Creates a field.

This function does not bind the field to any bundle; use
field_create_instance() for that.

@param $field
  A field definition array. The field_name and type properties are required.
  Other properties, if omitted, will be given the following default values:
  - cardinality: 1
  - locked: FALSE
  - indexes: the field-type indexes, specified by the field type's
    hook_field_schema(). The indexes specified in $field are added
    to those default indexes. It is possible to override the
    definition of a field-type index by providing an index with the
    same name, or to remove it by redefining it as an empty array
    of columns. Overriding field-type indexes should be done
    carefully, for it might seriously affect the site's performance.
  - settings: each omitted setting is given the default value defined in
    hook_field_info().
  - storage:
    - type: the storage backend specified in the 'field_storage_default'
      system variable.
    - settings: each omitted setting is given the default value specified in
      hook_field_storage_info().

@return
  The $field array with the id property filled in.

@throws FieldException

See: @link field Field API data structures @endlink.
```

## Code

```php
function field_create_field($field) {
  // Field name is required.
  if (empty($field['field_name'])) {
    throw new FieldException('Attempt to create an unnamed field.');
  }
  // Field type is required.
  if (empty($field['type'])) {
    throw new FieldException(format_string('Attempt to create field @field_name with no type.', array('@field_name' => $field['field_name'])));
  }
  // Field name cannot contain invalid characters.
  if (!preg_match('/^[_a-z]+[_a-z0-9]*$/', $field['field_name'])) {
    throw new FieldException(format_string('Attempt to create a field @field_name with invalid characters. Only lowercase alphanumeric characters and underscores are allowed, and only lowercase letters and underscore are allowed as the first character', array('@field_name' => $field['field_name'])));
  }

  // Field name cannot be longer than 32 characters. We use drupal_strlen()
  // because the DB layer assumes that column widths are given in characters,
  // not bytes.
  if (drupal_strlen($field['field_name']) > 32) {
    throw new FieldException(t('Attempt to create a field with a name longer than 32 characters: %name',
      array('%name' => $field['field_name'])));
  }

  // Ensure the field name is unique over active and disabled fields.
  // We do not care about deleted fields.
  $prior_field = field_read_field($field['field_name'], array('include_inactive' => TRUE));
  if (!empty($prior_field)) {
    $message = $prior_field['active']?
      t('Attempt to create field name %name which already exists and is active.', array('%name' => $field['field_name'])):
      t('Attempt to create field name %name which already exists, although it is inactive.', array('%name' => $field['field_name']));
    throw new FieldException($message);
  }

  // Disallow reserved field names. This can't prevent all field name
  // collisions with existing entity properties, but some is better
  // than none.
  foreach (entity_get_info() as $type => $info) {
    if (in_array($field['field_name'], $info['entity keys'])) {
      throw new FieldException(t('Attempt to create field name %name which is reserved by entity type %type.', array('%name' => $field['field_name'], '%type' => $type)));
    }
  }

  $field += array(
    'entity_types' => array(),
    'cardinality' => 1,
    'translatable' => FALSE,
    'locked' => FALSE,
    'settings' => array(),
    'storage' => array(),
    'deleted' => 0,
  );

  // Check that the field type is known.
  $field_type = field_info_field_types($field['type']);
  if (!$field_type) {
    throw new FieldException(t('Attempt to create a field of unknown type %type.', array('%type' => $field['type'])));
  }
  // Create all per-field-type properties (needed here as long as we have
  // settings that impact column definitions).
  $field['settings'] += field_info_field_settings($field['type']);
  $field['module'] = $field_type['module'];
  $field['active'] = 1;

  // Provide default storage.
  $field['storage'] += array(
    'type' => variable_get('field_storage_default', 'field_sql_storage'),
    'settings' => array(),
  );
  // Check that the storage type is known.
  $storage_type = field_info_storage_types($field['storage']['type']);
  if (!$storage_type) {
    throw new FieldException(t('Attempt to create a field with unknown storage type %type.', array('%type' => $field['storage']['type'])));
  }
  // Provide default storage settings.
  $field['storage']['settings'] += field_info_storage_settings($field['storage']['type']);
  $field['storage']['module'] = $storage_type['module'];
  $field['storage']['active'] = 1;
  // Collect storage information.
  $schema = field_retrieve_schema($field);
  // 'columns' are hardcoded in the field type.
  $field['columns'] = $schema['columns'];
  // 'foreign keys' are hardcoded in the field type.
  $field['foreign keys'] = $schema['foreign keys'];
  // 'indexes' can be both hardcoded in the field type, and specified in the
  // incoming $field definition.
  $field += array(
    'indexes' => array(),
  );
  $field['indexes'] += $schema['indexes'];

  // The serialized 'data' column contains everything from $field that does not
  // have its own column and is not automatically populated when the field is
  // read.
  $data = $field;
  unset($data['columns'], $data['field_name'], $data['type'], $data['active'], $data['module'], $data['storage_type'], $data['storage_active'], $data['storage_module'], $data['locked'], $data['cardinality'], $data['deleted']);
  // Additionally, do not save the 'bundles' property populated by
  // field_info_field().
  unset($data['bundles']);

  $record = array(
    'field_name' => $field['field_name'],
    'type' => $field['type'],
    'module' => $field['module'],
    'active' => $field['active'],
    'storage_type' => $field['storage']['type'],
    'storage_module' => $field['storage']['module'],
    'storage_active' => $field['storage']['active'],
    'locked' => $field['locked'],
    'data' => $data,
    'cardinality' => $field['cardinality'],
    'translatable' => $field['translatable'],
    'deleted' => $field['deleted'],
  );

  // Store the field and get the id back.
  drupal_write_record('field_config', $record);
  $field['id'] = $record['id'];

  // Invoke hook_field_storage_create_field after the field is
  // complete (e.g. it has its id).
  try {
    // Invoke hook_field_storage_create_field after
    // drupal_write_record() sets the field id.
    module_invoke($storage_type['module'], 'field_storage_create_field', $field);
  }
  catch (Exception $e) {
    // If storage creation failed, remove the field_config record before
    // rethrowing the exception.
    db_delete('field_config')
      ->condition('id', $field['id'])
      ->execute();
    throw $e;
  }

  // Clear caches
  field_cache_clear();

  // Invoke external hooks after the cache is cleared for API consistency.
  module_invoke_all('field_create_field', $field);

  return $field;
}
```

---
_Drupal 7.103 · [modules/field/field.crud.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.crud.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
