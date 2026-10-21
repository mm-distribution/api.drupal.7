# field_delete_instance()

- **Type:** Function
- **File:** [`modules/field/field.crud.inc`](_file.md), lines 784–807 · [local source](../../../../source/modules/field/field.crud.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.crud.inc#L784-L807)
- **Module/theme:** field
- **Topics:** [field_crud](../../../topics/field_crud.md)

## Signature

```php
function field_delete_instance($instance, $field_cleanup = TRUE)
```

## Documentation

```text
Marks a field instance and its data for deletion.

@param $instance
  An instance structure.
@param $field_cleanup
  If TRUE, the field will be deleted as well if its last instance is being
  deleted. If FALSE, it is the caller's responsibility to handle the case of
  fields left without instances. Defaults to TRUE.
```

## Code

```php
function field_delete_instance($instance, $field_cleanup = TRUE) {
  // Mark the field instance for deletion.
  db_update('field_config_instance')
    ->fields(array('deleted' => 1))
    ->condition('field_name', $instance['field_name'])
    ->condition('entity_type', $instance['entity_type'])
    ->condition('bundle', $instance['bundle'])
    ->execute();

  // Clear the cache.
  field_cache_clear();

  // Mark instance data for deletion.
  $field = field_info_field($instance['field_name']);
  module_invoke($field['storage']['module'], 'field_storage_delete_instance', $instance);

  // Let modules react to the deletion of the instance.
  module_invoke_all('field_delete_instance', $instance);

  // Delete the field itself if we just deleted its last instance.
  if ($field_cleanup && count($field['bundles']) == 0) {
    field_delete_field($field['field_name']);
  }
}
```

---
_Drupal 7.103 · [modules/field/field.crud.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.crud.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
