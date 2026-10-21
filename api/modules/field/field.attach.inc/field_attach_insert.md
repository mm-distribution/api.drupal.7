# field_attach_insert()

- **Type:** Function
- **File:** [`modules/field/field.attach.inc`](_file.md), lines 936–974 · [local source](../../../../source/modules/field/field.attach.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.attach.inc#L936-L974)
- **Module/theme:** field
- **Topics:** [field_attach](../../../topics/field_attach.md)

## Signature

```php
function field_attach_insert($entity_type, $entity)
```

## Documentation

```text
Save field data for a new entity.

The passed-in entity must already contain its id and (if applicable)
revision id attributes.
Default values (if any) will be saved for fields not present in the
$entity.

@param $entity_type
  The type of $entity; e.g. 'node' or 'user'.
@param $entity
  The entity with fields to save.
@return
  Default values (if any) will be added to the $entity parameter for fields
  it leaves unspecified.
```

## Code

```php
function field_attach_insert($entity_type, $entity) {
  _field_invoke_default('insert', $entity_type, $entity);
  _field_invoke('insert', $entity_type, $entity);

  list($id, $vid, $bundle) = entity_extract_ids($entity_type, $entity);

  // Let any module insert field data before the storage engine, accumulating
  // saved fields along the way.
  $skip_fields = array();
  foreach (module_implements('field_storage_pre_insert') as $module) {
    $function = $module . '_field_storage_pre_insert';
    $function($entity_type, $entity, $skip_fields);
  }

  // Collect the storage backends used by the remaining fields in the entities.
  $storages = array();
  foreach (field_info_instances($entity_type, $bundle) as $instance) {
    $field = field_info_field_by_id($instance['field_id']);
    $field_id = $field['id'];
    $field_name = $field['field_name'];
    if (!empty($entity->$field_name)) {
      // Collect the storage backend if the field has not been written yet.
      if (!isset($skip_fields[$field_id])) {
        $storages[$field['storage']['type']][$field_id] = $field_id;
      }
    }
  }

  // Field storage backends save any remaining unsaved fields.
  foreach ($storages as $storage => $fields) {
    $storage_info = field_info_storage_types($storage);
    module_invoke($storage_info['module'], 'field_storage_write', $entity_type, $entity, FIELD_STORAGE_INSERT, $fields);
  }

  // Let other modules act on inserting the entity.
  module_invoke_all('field_attach_insert', $entity_type, $entity);

  $entity_info = entity_get_info($entity_type);
}
```

---
_Drupal 7.103 · [modules/field/field.attach.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.attach.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
