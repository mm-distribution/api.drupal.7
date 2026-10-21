# FieldInfo::prepareInstance()

- **Type:** Method
- **File:** [`modules/field/field.info.class.inc`](../_file.md), lines 526–562 · [local source](../../../../../source/modules/field/field.info.class.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.class.inc#L526-L562)
- **Class:** [FieldInfo](../FieldInfo.md)
- **Module/theme:** field

## Signature

```php
public function prepareInstance($instance, $field_type)
```

## Documentation

```text
Prepares an instance definition for the current run-time context.

@param $instance
  The raw instance structure as read from the database.
@param $field_type
  The field type.

@return
  The field instance array completed for the current runtime context.
```

## Code

```php
  public function prepareInstance($instance, $field_type) {
    // Make sure all expected instance settings are present.
    $instance['settings'] += field_info_instance_settings($field_type);

    // Set a default value for the instance.
    if (field_behaviors_widget('default value', $instance) == FIELD_BEHAVIOR_DEFAULT && !isset($instance['default_value'])) {
      $instance['default_value'] = NULL;
    }

    // Prepare widget settings.
    $instance['widget'] = $this->prepareInstanceWidget($instance['widget'], $field_type);

    // Prepare display settings.
    foreach ($instance['display'] as $view_mode => $display) {
      $instance['display'][$view_mode] = $this->prepareInstanceDisplay($display, $field_type);
    }

    // Fall back to 'hidden' for view modes configured to use custom display
    // settings, and for which the instance has no explicit settings.
    $entity_info = entity_get_info($instance['entity_type']);
    $view_modes = array_merge(array('default'), array_keys($entity_info['view modes']));
    $view_mode_settings = field_view_mode_settings($instance['entity_type'], $instance['bundle']);
    foreach ($view_modes as $view_mode) {
      if ($view_mode == 'default' || !empty($view_mode_settings[$view_mode]['custom_settings'])) {
        if (!isset($instance['display'][$view_mode])) {
          $instance['display'][$view_mode] = array(
            'type' => 'hidden',
            'label' => 'above',
            'settings' => array(),
            'weight' => 0,
          );
        }
      }
    }

    return $instance;
  }
```

---
_Drupal 7.103 · [modules/field/field.info.class.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.class.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
