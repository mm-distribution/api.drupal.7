# number_field_widget_validate()

- **Type:** Function
- **File:** [`modules/field/modules/number/number.module`](_file.md), lines 379–423 · [local source](../../../../../../source/modules/field/modules/number/number.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/number/number.module#L379-L423)
- **Module/theme:** number

## Signature

```php
function number_field_widget_validate($element, &$form_state)
```

## Documentation

```text
FAPI validation of an individual number element.
```

## Code

```php
function number_field_widget_validate($element, &$form_state) {
  $field = field_widget_field($element, $form_state);
  $instance = field_widget_instance($element, $form_state);

  $type = $element['#number_type'];
  $value = $element['#value'];

  // Reject invalid characters.
  if (!empty($value)) {
    switch ($type) {
      case 'float':
      case 'decimal':
        $regexp = '@([^-0-9\\' . $field['settings']['decimal_separator'] . '])|(.-)@';
        $message = t('Only numbers and the decimal separator (@separator) allowed in %field.', array('%field' => $instance['label'], '@separator' => $field['settings']['decimal_separator']));
        break;

      case 'integer':
        $regexp = '@([^-0-9])|(.-)@';
        $message = t('Only numbers are allowed in %field.', array('%field' => $instance['label']));
        break;
    }
    if ($value != preg_replace($regexp, '', $value)) {
      form_error($element, $message);
    }
    else {
      if ($type == 'decimal' || $type == 'float') {
        // Verify that only one decimal separator exists in the field.
        if (substr_count($value, $field['settings']['decimal_separator']) > 1) {
          $message = t('%field: There should only be one decimal separator (@separator).',
            array(
              '%field' => t($instance['label']),
              '@separator' => $field['settings']['decimal_separator'],
            )
          );
          form_error($element, $message);
        }
        else {
          // Substitute the decimal separator; things should be fine.
          $value = strtr($value, $field['settings']['decimal_separator'], '.');
        }
      }
      form_set_value($element, $value, $form_state);
    }
  }
}
```

---
_Drupal 7.103 · [modules/field/modules/number/number.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/number/number.module) · Licensed GPL-2.0-or-later (see LICENSE)._
