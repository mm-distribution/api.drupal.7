# field_default_form_errors()

- **Type:** Function
- **File:** [`modules/field/field.form.inc`](_file.md), lines 400–432 · [local source](../../../../source/modules/field/field.form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.form.inc#L400-L432)
- **Module/theme:** field

## Signature

```php
function field_default_form_errors($entity_type, $entity, $field, $instance, $langcode, $items, $form, &$form_state)
```

## Documentation

```text
Transfer field-level validation errors to widgets.
```

## Code

```php
function field_default_form_errors($entity_type, $entity, $field, $instance, $langcode, $items, $form, &$form_state) {
  $field_state = field_form_get_state($form['#parents'], $field['field_name'], $langcode, $form_state);

  if (!empty($field_state['errors'])) {
    // Locate the correct element in the form.
    $element = drupal_array_get_nested_value($form_state['complete form'], $field_state['array_parents']);
    // Only set errors if the element is accessible.
    if (!isset($element['#access']) || $element['#access']) {
      $function = $instance['widget']['module'] . '_field_widget_error';
      $function_exists = function_exists($function);

      $multiple_widget = field_behaviors_widget('multiple values', $instance) != FIELD_BEHAVIOR_DEFAULT;
      foreach ($field_state['errors'] as $delta => $delta_errors) {
        // For multiple single-value widgets, pass errors by delta.
        // For a multiple-value widget, pass all errors to the main widget.
        $error_element = $multiple_widget ? $element : $element[$delta];
        foreach ($delta_errors as $error) {
          if ($function_exists) {
            $function($error_element, $error, $form, $form_state);
          }
          else {
            // Make sure that errors are reported (even incorrectly flagged) if
            // the widget module fails to implement hook_field_widget_error().
            form_error($error_element, $error['message']);
          }
        }
      }
      // Reinitialize the errors list for the next submit.
      $field_state['errors'] = array();
      field_form_set_state($form['#parents'], $field['field_name'], $langcode, $form_state, $field_state);
    }
  }
}
```

---
_Drupal 7.103 · [modules/field/field.form.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
