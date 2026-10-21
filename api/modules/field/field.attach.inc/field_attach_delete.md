# field_attach_delete()

- **Type:** Function
- **File:** [`modules/field/field.attach.inc`](_file.md), lines 1045–1071 · [local source](../../../../source/modules/field/field.attach.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.attach.inc#L1045-L1071)
- **Module/theme:** field
- **Topics:** [field_attach](../../../topics/field_attach.md)

## Signature

```php
function field_attach_delete($entity_type, $entity)
```

## Documentation

```text
Delete field data for an existing entity. This deletes all
revisions of field data for the entity.

@param $entity_type
  The type of $entity; e.g. 'node' or 'user'.
@param $entity
  The entity whose field data to delete.
```

## Code

```php
function field_attach_delete($entity_type, $entity) {
  _field_invoke('delete', $entity_type, $entity);

  list($id, $vid, $bundle) = entity_extract_ids($entity_type, $entity);

  // Collect the storage backends used by the fields in the entities.
  $storages = array();
  foreach (field_info_instances($entity_type, $bundle) as $instance) {
    $field = field_info_field_by_id($instance['field_id']);
    $field_id = $field['id'];
    $storages[$field['storage']['type']][$field_id] = $field_id;
  }

  // Field storage backends delete their data.
  foreach ($storages as $storage => $fields) {
    $storage_info = field_info_storage_types($storage);
    module_invoke($storage_info['module'], 'field_storage_delete', $entity_type, $entity, $fields);
  }

  // Let other modules act on deleting the entity.
  module_invoke_all('field_attach_delete', $entity_type, $entity);

  $entity_info = entity_get_info($entity_type);
  if ($entity_info['field cache']) {
    cache_clear_all("field:$entity_type:$id", 'cache_field');
  }
}
```

---
_Drupal 7.103 · [modules/field/field.attach.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.attach.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
