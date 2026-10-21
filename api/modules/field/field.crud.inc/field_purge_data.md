# field_purge_data()

- **Type:** Function
- **File:** [`modules/field/field.crud.inc`](_file.md), lines 954–968 · [local source](../../../../source/modules/field/field.crud.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.crud.inc#L954-L968)
- **Module/theme:** field
- **Topics:** [field_purge](../../../topics/field_purge.md)

## Signature

```php
function field_purge_data($entity_type, $entity, $field, $instance)
```

## Documentation

```text
Purges the field data for a single field on a single pseudo-entity.

This is basically the same as field_attach_delete() except it only applies
to a single field. The entity itself is not being deleted, and it is quite
possible that other field data will remain attached to it.

@param $entity_type
  The type of $entity; e.g. 'node' or 'user'.
@param $entity
  The pseudo-entity whose field data is being purged.
@param $field
  The (possibly deleted) field whose data is being purged.
@param $instance
  The deleted field instance whose data is being purged.
```

## Code

```php
function field_purge_data($entity_type, $entity, $field, $instance) {
  // Each field type's hook_field_delete() only expects to operate on a single
  // field at a time, so we can use it as-is for purging.
  $options = array('field_id' => $instance['field_id'], 'deleted' => TRUE);
  _field_invoke('delete', $entity_type, $entity, $dummy, $dummy, $options);

  // Tell the field storage system to purge the data.
  module_invoke($field['storage']['module'], 'field_storage_purge', $entity_type, $entity, $field, $instance);

  // Let other modules act on purging the data.
  foreach (module_implements('field_attach_purge') as $module) {
    $function = $module . '_field_attach_purge';
    $function($entity_type, $entity, $field, $instance);
  }
}
```

---
_Drupal 7.103 · [modules/field/field.crud.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.crud.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
