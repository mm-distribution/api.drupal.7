# field_get_display()

- **Type:** Function
- **File:** [`modules/field/field.module`](_file.md), lines 655–673 · [local source](../../../../source/modules/field/field.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module#L655-L673)
- **Module/theme:** field
- **Topics:** [field](../../../topics/field.md)

## Signature

```php
function field_get_display($instance, $view_mode, $entity)
```

## Documentation

```text
Returns the display settings to use for an instance in a given view mode.

@param $instance
  The field instance being displayed.
@param $view_mode
  The view mode.
@param $entity
  The entity being displayed.

@return
  The display settings to be used when displaying the field values.
```

## Code

```php
function field_get_display($instance, $view_mode, $entity) {
  // Check whether the view mode uses custom display settings or the 'default'
  // mode.
  $view_mode_settings = field_view_mode_settings($instance['entity_type'], $instance['bundle']);
  $actual_mode = (!empty($view_mode_settings[$view_mode]['custom_settings']) ? $view_mode : 'default');
  $display = $instance['display'][$actual_mode];

  // Let modules alter the display settings.
  $context = array(
    'entity_type' => $instance['entity_type'],
    'field' => field_info_field($instance['field_name']),
    'instance' => $instance,
    'entity' => $entity,
    'view_mode' => $view_mode,
  );
  drupal_alter(array('field_display', 'field_display_' . $instance['entity_type']), $display, $context);

  return $display;
}
```

---
_Drupal 7.103 · [modules/field/field.module](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module) · Licensed GPL-2.0-or-later (see LICENSE)._
