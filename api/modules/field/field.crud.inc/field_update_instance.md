# field_update_instance()

- **Type:** Function
- **File:** [`modules/field/field.crud.inc`](_file.md), lines 568–591 · [local source](../../../../source/modules/field/field.crud.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.crud.inc#L568-L591)
- **Module/theme:** field
- **Topics:** [field_crud](../../../topics/field_crud.md)

## Signature

```php
function field_update_instance($instance)
```

## Documentation

```text
Updates an instance of a field.

@param $instance
  An associative array representing an instance structure. The following
  required array elements specify which field instance is being updated:
  - entity_type: The type of the entity the field is attached to.
  - bundle: The bundle this field belongs to.
  - field_name: The name of an existing field.
  The other array elements represent properties of the instance, and all
  properties must be specified or their default values will be used (except
  internal-use properties, which are assigned automatically). To avoid
  losing the previously stored properties of the instance when making a
  change, first load the instance with field_info_instance(), then override
  the values you want to override, and finally save using this function.
  Example:
  @code
  // Fetch an instance info array.
  $instance_info = field_info_instance($entity_type, $field_name, $bundle_name);
  // Change a single property in the instance definition.
  $instance_info['required'] = TRUE;
  // Write the changed definition back.
  field_update_instance($instance_info);
  @endcode

@throws FieldException

@see field_info_instance()
@see field_create_instance()
```

## Code

```php
function field_update_instance($instance) {
  // Check that the specified field exists.
  $field = field_read_field($instance['field_name']);
  if (empty($field)) {
    throw new FieldException(t('Attempt to update an instance of a nonexistent field @field.', array('@field' => $instance['field_name'])));
  }

  // Check that the field instance exists (even if it is inactive, since we
  // want to be able to replace inactive widgets with new ones).
  $prior_instance = field_read_instance($instance['entity_type'], $instance['field_name'], $instance['bundle'], array('include_inactive' => TRUE));
  if (empty($prior_instance)) {
    throw new FieldException(t("Attempt to update an instance of field @field on bundle @bundle that doesn't exist.", array('@field' => $instance['field_name'], '@bundle' => $instance['bundle'])));
  }

  $instance['id'] = $prior_instance['id'];
  $instance['field_id'] = $prior_instance['field_id'];

  _field_write_instance($instance, TRUE);

  // Clear caches.
  field_cache_clear();

  module_invoke_all('field_update_instance', $instance, $prior_instance);
}
```

---
_Drupal 7.103 · [modules/field/field.crud.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.crud.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
