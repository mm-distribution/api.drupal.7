# field_create_instance()

- **Type:** Function
- **File:** [`modules/field/field.crud.inc`](_file.md), lines 488–536 · [local source](../../../../source/modules/field/field.crud.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.crud.inc#L488-L536)
- **Module/theme:** field
- **Topics:** [field_crud](../../../topics/field_crud.md)

## Signature

```php
function field_create_instance($instance)
```

## Documentation

```text
Creates an instance of a field, binding it to a bundle.

@param $instance
  A field instance definition array. The field_name, entity_type and
  bundle properties are required. Other properties, if omitted,
  will be given the following default values:
  - label: the field name
  - description: empty string
  - required: FALSE
  - default_value_function: empty string
  - settings: each omitted setting is given the default value specified in
    hook_field_info().
  - widget:
    - type: the default widget specified in hook_field_info().
    - settings: each omitted setting is given the default value specified in
      hook_field_widget_info().
  - display:
    Settings for the 'default' view mode will be added if not present, and
    each view mode in the definition will be completed with the following
    default values:
    - label: 'above'
    - type: the default formatter specified in hook_field_info().
    - settings: each omitted setting is given the default value specified in
      hook_field_formatter_info().
    View modes not present in the definition are left empty, and the field
    will not be displayed in this mode.

@return
  The $instance array with the id property filled in.

@throws FieldException

See: @link field Field API data structures @endlink.
@see hook_field_schema_alter()
```

## Code

```php
function field_create_instance($instance) {
  $field = field_read_field($instance['field_name']);
  if (empty($field)) {
    throw new FieldException(t("Attempt to create an instance of a field @field_name that doesn't exist or is currently inactive.", array('@field_name' => $instance['field_name'])));
  }
  // Check that the required properties exists.
  if (empty($instance['entity_type'])) {
    throw new FieldException(t('Attempt to create an instance of field @field_name without an entity type.', array('@field_name' => $instance['field_name'])));
  }
  if (empty($instance['bundle'])) {
    throw new FieldException(t('Attempt to create an instance of field @field_name without a bundle.', array('@field_name' => $instance['field_name'])));
  }
  // Check that the field can be attached to this entity type.
  if (!empty($field['entity_types']) && !in_array($instance['entity_type'], $field['entity_types'])) {
    throw new FieldException(t('Attempt to create an instance of field @field_name on forbidden entity type @entity_type.', array('@field_name' => $instance['field_name'], '@entity_type' => $instance['entity_type'])));
  }

  // Set the field id.
  $instance['field_id'] = $field['id'];

  // Note that we do *not* prevent creating a field on non-existing bundles,
  // because that would break the 'Body as field' upgrade for contrib
  // node types.

  // TODO: Check that the widget type is known and can handle the field type ?
  // TODO: Check that the formatters are known and can handle the field type ?
  // TODO: Check that the display view modes are known for the entity type ?
  // Those checks should probably happen in _field_write_instance() ?
  // Problem : this would mean that a UI module cannot update an instance with a disabled formatter.

  // Ensure the field instance is unique within the bundle.
  // We only check for instances of active fields, since adding an instance of
  // a disabled field is not supported.
  $prior_instance = field_read_instance($instance['entity_type'], $instance['field_name'], $instance['bundle']);
  if (!empty($prior_instance)) {
    $message = t('Attempt to create an instance of field @field_name on bundle @bundle that already has an instance of that field.', array('@field_name' => $instance['field_name'], '@bundle' => $instance['bundle']));
    throw new FieldException($message);
  }

  _field_write_instance($instance);

  // Clear caches
  field_cache_clear();

  // Invoke external hooks after the cache is cleared for API consistency.
  module_invoke_all('field_create_instance', $instance);

  return $instance;
}
```

---
_Drupal 7.103 · [modules/field/field.crud.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.crud.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
