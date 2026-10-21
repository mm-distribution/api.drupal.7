# field_get_default_value()

- **Type:** Function
- **File:** [`modules/field/field.module`](_file.md), lines 483–495 · [local source](../../../../source/modules/field/field.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module#L483-L495)
- **Module/theme:** field
- **Topics:** [field](../../../topics/field.md)

## Signature

```php
function field_get_default_value($entity_type, $entity, $field, $instance, $langcode = NULL)
```

## Documentation

```text
Helper function to get the default value for a field on an entity.

@param $entity_type
  The type of $entity; e.g., 'node' or 'user'.
@param $entity
  The entity for the operation.
@param $field
  The field structure.
@param $instance
  The instance structure.
@param $langcode
  The field language to fill-in with the default value.
```

## Code

```php
function field_get_default_value($entity_type, $entity, $field, $instance, $langcode = NULL) {
  $items = array();
  if (!empty($instance['default_value_function'])) {
    $function = $instance['default_value_function'];
    if (function_exists($function)) {
      $items = $function($entity_type, $entity, $field, $instance, $langcode);
    }
  }
  elseif (!empty($instance['default_value'])) {
    $items = $instance['default_value'];
  }
  return $items;
}
```

---
_Drupal 7.103 · [modules/field/field.module](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module) · Licensed GPL-2.0-or-later (see LICENSE)._
