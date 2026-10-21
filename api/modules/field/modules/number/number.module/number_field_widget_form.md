# number_field_widget_form()

- **Type:** Function
- **File:** [`modules/field/modules/number/number.module`](_file.md), lines 342–374 · [local source](../../../../../../source/modules/field/modules/number/number.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/number/number.module#L342-L374)
- **Module/theme:** number
- **Implements:** [hook_field_widget_form()](../../../field.api.php/hook_field_widget_form.md)

## Signature

```php
function number_field_widget_form(&$form, &$form_state, $field, $instance, $langcode, $items, $delta, $element)
```

## Documentation

```text
Implements hook_field_widget_form().
```

## Code

```php
function number_field_widget_form(&$form, &$form_state, $field, $instance, $langcode, $items, $delta, $element) {
  $value = isset($items[$delta]['value']) ? $items[$delta]['value'] : '';
  // Substitute the decimal separator.
  if ($field['type'] == 'number_decimal' || $field['type'] == 'number_float') {
    $value = strtr($value, '.', $field['settings']['decimal_separator']);
  }

  $element += array(
    '#type' => 'textfield',
    '#default_value' => $value,
    // Allow a slightly larger size that the field length to allow for some
    // configurations where all characters won't fit in input field.
    '#size' => $field['type'] == 'number_decimal' ? $field['settings']['precision'] + 4 : 12,
    // Allow two extra characters for signed values and decimal separator.
    '#maxlength' => $field['type'] == 'number_decimal' ? $field['settings']['precision'] + 2 : 10,
    // Extract the number type from the field type name for easier validation.
    '#number_type' => str_replace('number_', '', $field['type']),
  );

  // Add prefix and suffix.
  if (!empty($instance['settings']['prefix'])) {
    $prefixes = explode('|', $instance['settings']['prefix']);
    $element['#field_prefix'] = field_filter_xss(array_pop($prefixes));
  }
  if (!empty($instance['settings']['suffix'])) {
    $suffixes = explode('|', $instance['settings']['suffix']);
    $element['#field_suffix'] = field_filter_xss(array_pop($suffixes));
  }

  $element['#element_validate'][] = 'number_field_widget_validate';

  return array('value' => $element);
}
```

---
_Drupal 7.103 · [modules/field/modules/number/number.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/number/number.module) · Licensed GPL-2.0-or-later (see LICENSE)._
