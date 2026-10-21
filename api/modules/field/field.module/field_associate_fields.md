# field_associate_fields()

- **Type:** Function
- **File:** [`modules/field/field.module`](_file.md), lines 450–467 · [local source](../../../../source/modules/field/field.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module#L450-L467)
- **Module/theme:** field
- **Topics:** [field](../../../topics/field.md)

## Signature

```php
function field_associate_fields($module)
```

## Documentation

```text
Allows a module to update the database for fields and columns it controls.

@param $module
  The name of the module to update on.
```

## Code

```php
function field_associate_fields($module) {
  // Associate field types.
  $field_types = (array) module_invoke($module, 'field_info');
  if ($field_types) {
    db_update('field_config')
      ->fields(array('module' => $module, 'active' => 1))
      ->condition('type', array_keys($field_types))
      ->execute();
  }
  // Associate storage backends.
  $storage_types = (array) module_invoke($module, 'field_storage_info');
  if ($storage_types) {
    db_update('field_config')
      ->fields(array('storage_module' => $module, 'storage_active' => 1))
      ->condition('storage_type', array_keys($storage_types))
      ->execute();
  }
}
```

---
_Drupal 7.103 · [modules/field/field.module](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module) · Licensed GPL-2.0-or-later (see LICENSE)._
