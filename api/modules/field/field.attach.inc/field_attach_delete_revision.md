# field_attach_delete_revision()

- **Type:** Function
- **File:** [`modules/field/field.attach.inc`](_file.md), lines 1082–1103 · [local source](../../../../source/modules/field/field.attach.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.attach.inc#L1082-L1103)
- **Module/theme:** field
- **Topics:** [field_attach](../../../topics/field_attach.md)

## Signature

```php
function field_attach_delete_revision($entity_type, $entity)
```

## Documentation

```text
Delete field data for a single revision of an existing entity. The
passed entity must have a revision id attribute.

@param $entity_type
  The type of $entity; e.g. 'node' or 'user'.
@param $entity
  The entity with fields to save.
```

## Code

```php
function field_attach_delete_revision($entity_type, $entity) {
  _field_invoke('delete_revision', $entity_type, $entity);

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
    module_invoke($storage_info['module'], 'field_storage_delete_revision', $entity_type, $entity, $fields);
  }

  // Let other modules act on deleting the revision.
  module_invoke_all('field_attach_delete_revision', $entity_type, $entity);
}
```

---
_Drupal 7.103 · [modules/field/field.attach.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.attach.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
