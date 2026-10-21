# field_update_field()

- **Type:** Function
- **File:** [`modules/field/field.crud.inc`](_file.md), lines 238–311 · [local source](../../../../source/modules/field/field.crud.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.crud.inc#L238-L311)
- **Module/theme:** field
- **Topics:** [field_crud](../../../topics/field_crud.md)

## Signature

```php
function field_update_field($field)
```

## Documentation

```text
Updates a field.

Any module may forbid any update for any reason. For example, the
field's storage module might forbid an update if it would change
the storage schema while data for the field exists. A field type
module might forbid an update if it would change existing data's
semantics, or if there are external dependencies on field settings
that cannot be updated.

@param $field
  A field structure. $field['field_name'] must provided; it
  identifies the field that will be updated to match this
  structure. Any other properties of the field that are not
  specified in $field will be left unchanged, so it is not
  necessary to pass in a fully populated $field structure.
@return
  Throws a FieldException if the update cannot be performed.
@see field_create_field()
```

## Code

```php
function field_update_field($field) {
  // Check that the specified field exists.
  $prior_field = field_read_field($field['field_name']);
  if (empty($prior_field)) {
    throw new FieldException('Attempt to update a non-existent field.');
  }

  // Use the prior field values for anything not specifically set by the new
  // field to be sure that all values are set.
  $field += $prior_field;
  $field['settings'] += $prior_field['settings'];

  // Some updates are always disallowed.
  if ($field['type'] != $prior_field['type']) {
    throw new FieldException("Cannot change an existing field's type.");
  }
  if ($field['entity_types'] != $prior_field['entity_types']) {
    throw new FieldException("Cannot change an existing field's entity_types property.");
  }
  if ($field['storage']['type'] != $prior_field['storage']['type']) {
    throw new FieldException("Cannot change an existing field's storage type.");
  }

  // Collect the new storage information, since what is in
  // $prior_field may no longer be right.
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

  $has_data = field_has_data($field);

  // See if any module forbids the update by throwing an exception.
  foreach (module_implements('field_update_forbid') as $module) {
    $function = $module . '_field_update_forbid';
    $function($field, $prior_field, $has_data);
  }

  // Tell the storage engine to update the field. Do this before
  // saving the new definition since it still might fail.
  $storage_type = field_info_storage_types($field['storage']['type']);
  module_invoke($storage_type['module'], 'field_storage_update_field', $field, $prior_field, $has_data);

  // Save the new field definition. @todo: refactor with
  // field_create_field.

  // The serialized 'data' column contains everything from $field that does not
  // have its own column and is not automatically populated when the field is
  // read.
  $data = $field;
  unset($data['columns'], $data['field_name'], $data['type'], $data['locked'], $data['module'], $data['cardinality'], $data['active'], $data['deleted']);
  // Additionally, do not save the 'bundles' property populated by
  // field_info_field().
  unset($data['bundles']);

  $field['data'] = $data;

  // Store the field and create the id.
  $primary_key = array('id');
  drupal_write_record('field_config', $field, $primary_key);

  // Clear caches
  field_cache_clear();

  // Invoke external hooks after the cache is cleared for API consistency.
  module_invoke_all('field_update_field', $field, $prior_field, $has_data);
}
```

---
_Drupal 7.103 · [modules/field/field.crud.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.crud.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
