# options_field_widget_form()

- **Type:** Function
- **File:** [`modules/field/modules/options/options.module`](_file.md), lines 71–150 · [local source](../../../../../../source/modules/field/modules/options/options.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/options/options.module#L71-L150)
- **Module/theme:** options
- **Implements:** [hook_field_widget_form()](../../../field.api.php/hook_field_widget_form.md)

## Signature

```php
function options_field_widget_form(&$form, &$form_state, $field, $instance, $langcode, $items, $delta, $element)
```

## Documentation

```text
Implements hook_field_widget_form().
```

## Code

```php
function options_field_widget_form(&$form, &$form_state, $field, $instance, $langcode, $items, $delta, $element) {
  // Abstract over the actual field columns, to allow different field types to
  // reuse those widgets.
  $value_key = key($field['columns']);

  $type = str_replace('options_', '', $instance['widget']['type']);
  $multiple = $field['cardinality'] > 1 || $field['cardinality'] == FIELD_CARDINALITY_UNLIMITED;
  $required = $element['#required'];
  $has_value = isset($items[0][$value_key]);
  $properties = _options_properties($type, $multiple, $required, $has_value);

  $entity_type = $element['#entity_type'];
  $entity = $element['#entity'];

  // Prepare the list of options.
  $options = _options_get_options($field, $instance, $properties, $entity_type, $entity);

  // Put current field values in shape.
  $default_value = _options_storage_to_form($items, $options, $value_key, $properties);

  switch ($type) {
    case 'select':
      $element += array(
        '#type' => 'select',
        '#default_value' => $default_value,
        // Do not display a 'multiple' select box if there is only one option.
        '#multiple' => $multiple && count($options) > 1,
        '#options' => $options,
      );
      break;

    case 'buttons':
      // If required and there is one single option, preselect it.
      if ($required && count($options) == 1) {
        reset($options);
        $default_value = array(key($options));
      }

      // If this is a single-value field, take the first default value, or
      // default to NULL so that the form element is properly recognized as
      // not having a default value.
      if (!$multiple) {
        $default_value = $default_value ? reset($default_value) : NULL;
      }

      $element += array(
        '#type' => $multiple ? 'checkboxes' : 'radios',
        // Radio buttons need a scalar value.
        '#default_value' => $default_value,
        '#options' => $options,
      );
      break;

    case 'onoff':
      $keys = array_keys($options);
      $off_value = array_shift($keys);
      $on_value = array_shift($keys);
      $element += array(
        '#type' => 'checkbox',
        '#default_value' => (isset($default_value[0]) && $default_value[0] == $on_value) ? 1 : 0,
        '#on_value' => $on_value,
        '#off_value' => $off_value,
      );
      // Override the title from the incoming $element.
      $element['#title'] = isset($options[$on_value]) ? $options[$on_value] : '';

      if ($instance['widget']['settings']['display_label']) {
        $element['#title'] = $instance['label'];
      }
      break;
  }

  $element += array(
    '#value_key' => $value_key,
    '#element_validate' => array('options_field_widget_validate'),
    '#properties' => $properties,
  );

  return $element;
}
```

---
_Drupal 7.103 · [modules/field/modules/options/options.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/options/options.module) · Licensed GPL-2.0-or-later (see LICENSE)._
