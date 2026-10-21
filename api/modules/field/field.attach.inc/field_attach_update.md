# field_attach_update()

- **Type:** Function
- **File:** [`modules/field/field.attach.inc`](_file.md), lines 990–1034 · [local source](../../../../source/modules/field/field.attach.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.attach.inc#L990-L1034)
- **Module/theme:** field
- **Topics:** [field_attach](../../../topics/field_attach.md)

## Signature

```php
function field_attach_update($entity_type, $entity)
```

## Documentation

```text
Save field data for an existing entity.

When calling this function outside an entity save operation be sure to
clear caches for the entity:
@code
entity_get_controller($entity_type)->resetCache(array($entity_id))
@endcode

@param $entity_type
  The type of $entity; e.g. 'node' or 'user'.
@param $entity
  The entity with fields to save.
```

## Code

```php
function field_attach_update($entity_type, $entity) {
  _field_invoke('update', $entity_type, $entity);

  list($id, $vid, $bundle) = entity_extract_ids($entity_type, $entity);

  // Let any module update field data before the storage engine, accumulating
  // saved fields along the way.
  $skip_fields = array();
  foreach (module_implements('field_storage_pre_update') as $module) {
    $function = $module . '_field_storage_pre_update';
    $function($entity_type, $entity, $skip_fields);
  }

  // Collect the storage backends used by the remaining fields in the entities.
  $storages = array();
  foreach (field_info_instances($entity_type, $bundle) as $instance) {
    $field = field_info_field_by_id($instance['field_id']);
    $field_id = $field['id'];
    $field_name = $field['field_name'];
    // Leave the field untouched if $entity comes with no $field_name property,
    // but empty the field if it comes as a NULL value or an empty array.
    // Function property_exists() is slower, so we catch the more frequent
    // cases where it's an empty array with the faster isset().
    if (isset($entity->$field_name) || property_exists($entity, $field_name)) {
      // Collect the storage backend if the field has not been written yet.
      if (!isset($skip_fields[$field_id])) {
        $storages[$field['storage']['type']][$field_id] = $field_id;
      }
    }
  }

  // Field storage backends save any remaining unsaved fields.
  foreach ($storages as $storage => $fields) {
    $storage_info = field_info_storage_types($storage);
    module_invoke($storage_info['module'], 'field_storage_write', $entity_type, $entity, FIELD_STORAGE_UPDATE, $fields);
  }

  // Let other modules act on updating the entity.
  module_invoke_all('field_attach_update', $entity_type, $entity);

  $entity_info = entity_get_info($entity_type);
  if ($entity_info['field cache']) {
    cache_clear_all("field:$entity_type:$id", 'cache_field');
  }
}
```

---
_Drupal 7.103 · [modules/field/field.attach.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.attach.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
