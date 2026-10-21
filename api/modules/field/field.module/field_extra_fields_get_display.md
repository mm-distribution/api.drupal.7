# field_extra_fields_get_display()

- **Type:** Function
- **File:** [`modules/field/field.module`](_file.md), lines 688–709 · [local source](../../../../source/modules/field/field.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module#L688-L709)
- **Module/theme:** field
- **Topics:** [field](../../../topics/field.md)

## Signature

```php
function field_extra_fields_get_display($entity_type, $bundle, $view_mode)
```

## Documentation

```text
Returns the display settings to use for pseudo-fields in a given view mode.

@param $entity_type
  The type of $entity; e.g., 'node' or 'user'.
@param $bundle
  The bundle name.
@param $view_mode
  The view mode.

@return
  The display settings to be used when viewing the bundle's pseudo-fields.
```

## Code

```php
function field_extra_fields_get_display($entity_type, $bundle, $view_mode) {
  // Check whether the view mode uses custom display settings or the 'default'
  // mode.
  $view_mode_settings = field_view_mode_settings($entity_type, $bundle);
  $actual_mode = (!empty($view_mode_settings[$view_mode]['custom_settings'])) ? $view_mode : 'default';
  $extra_fields = field_info_extra_fields($entity_type, $bundle, 'display');

  $displays = array();
  foreach ($extra_fields as $name => $value) {
    $displays[$name] = $extra_fields[$name]['display'][$actual_mode];
  }

  // Let modules alter the display settings.
  $context = array(
    'entity_type' => $entity_type,
    'bundle' => $bundle,
    'view_mode' => $view_mode,
  );
  drupal_alter('field_extra_fields_display', $displays, $context);

  return $displays;
}
```

---
_Drupal 7.103 · [modules/field/field.module](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module) · Licensed GPL-2.0-or-later (see LICENSE)._
