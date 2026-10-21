# _field_write_instance()

- **Type:** Function
- **File:** [`modules/field/field.crud.inc`](_file.md), lines 601–683 · [local source](../../../../source/modules/field/field.crud.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.crud.inc#L601-L683)
- **Module/theme:** field
- **Topics:** [field_crud](../../../topics/field_crud.md)

## Signature

```php
function _field_write_instance($instance, $update = FALSE)
```

## Documentation

```text
Stores an instance record in the field configuration database.

@param $instance
  An instance structure.
@param $update
  Whether this is a new or existing instance.
```

## Code

```php
function _field_write_instance($instance, $update = FALSE) {
  $field = field_read_field($instance['field_name']);
  $field_type = field_info_field_types($field['type']);

  // Set defaults.
  $instance += array(
    'settings' => array(),
    'display' => array(),
    'widget' => array(),
    'required' => FALSE,
    'label' => $instance['field_name'],
    'description' => '',
    'deleted' => 0,
  );

  // Set default instance settings.
  $instance['settings'] += field_info_instance_settings($field['type']);

  // Set default widget and settings.
  $instance['widget'] += array(
    // TODO: what if no 'default_widget' specified ?
    'type' => $field_type['default_widget'],
    'settings' => array(),
  );
  // If no weight specified, make sure the field sinks at the bottom.
  if (!isset($instance['widget']['weight'])) {
    $max_weight = field_info_max_weight($instance['entity_type'], $instance['bundle'], 'form');
    $instance['widget']['weight'] = isset($max_weight) ? $max_weight + 1 : 0;
  }
  // Check widget module.
  $widget_type = field_info_widget_types($instance['widget']['type']);
  $instance['widget']['module'] = $widget_type['module'];
  $instance['widget']['settings'] += field_info_widget_settings($instance['widget']['type']);

  // Make sure there are at least display settings for the 'default' view mode,
  // and fill in defaults for each view mode specified in the definition.
  $instance['display'] += array(
    'default' => array(),
  );
  foreach ($instance['display'] as $view_mode => $display) {
    $display += array(
      'label' => 'above',
      'type' => isset($field_type['default_formatter']) ? $field_type['default_formatter'] : 'hidden',
      'settings' => array(),
    );
    if ($display['type'] != 'hidden') {
      $formatter_type = field_info_formatter_types($display['type']);
      $display['module'] = $formatter_type['module'];
      $display['settings'] += field_info_formatter_settings($display['type']);
    }
    // If no weight specified, make sure the field sinks at the bottom.
    if (!isset($display['weight'])) {
      $max_weight = field_info_max_weight($instance['entity_type'], $instance['bundle'], $view_mode);
      $display['weight'] = isset($max_weight) ? $max_weight + 1 : 0;
    }
    $instance['display'][$view_mode] = $display;
  }

  // The serialized 'data' column contains everything from $instance that does
  // not have its own column and is not automatically populated when the
  // instance is read.
  $data = $instance;
  unset($data['id'], $data['field_id'], $data['field_name'], $data['entity_type'], $data['bundle'], $data['deleted']);

  $record = array(
    'field_id' => $instance['field_id'],
    'field_name' => $instance['field_name'],
    'entity_type' => $instance['entity_type'],
    'bundle' => $instance['bundle'],
    'data' => $data,
    'deleted' => $instance['deleted'],
  );
  // We need to tell drupal_update_record() the primary keys to trigger an
  // update.
  if ($update) {
    $record['id'] = $instance['id'];
    $primary_key = array('id');
  }
  else {
    $primary_key = array();
  }
  drupal_write_record('field_config_instance', $record, $primary_key);
}
```

---
_Drupal 7.103 · [modules/field/field.crud.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.crud.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
