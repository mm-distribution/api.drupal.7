# field_delete_field()

- **Type:** Function
- **File:** [`modules/field/field.crud.inc`](_file.md), lines 425–450 · [local source](../../../../source/modules/field/field.crud.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.crud.inc#L425-L450)
- **Module/theme:** field
- **Topics:** [field_crud](../../../topics/field_crud.md)

## Signature

```php
function field_delete_field($field_name)
```

## Documentation

```text
Marks a field and its instances and data for deletion.

@param $field_name
  The field name to delete.
```

## Code

```php
function field_delete_field($field_name) {
  // Delete all non-deleted instances.
  $field = field_info_field($field_name);
  if (isset($field['bundles'])) {
    foreach ($field['bundles'] as $entity_type => $bundles) {
      foreach ($bundles as $bundle) {
        $instance = field_info_instance($entity_type, $field_name, $bundle);
        field_delete_instance($instance, FALSE);
      }
    }
  }

  // Mark field data for deletion.
  module_invoke($field['storage']['module'], 'field_storage_delete_field', $field);

  // Mark the field for deletion.
  db_update('field_config')
    ->fields(array('deleted' => 1))
    ->condition('field_name', $field_name)
    ->execute();

  // Clear the cache.
  field_cache_clear();

  module_invoke_all('field_delete_field', $field);
}
```

---
_Drupal 7.103 · [modules/field/field.crud.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.crud.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
