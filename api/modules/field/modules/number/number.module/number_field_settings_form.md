# number_field_settings_form()

- **Type:** Function
- **File:** [`modules/field/modules/number/number.module`](_file.md), lines 55–88 · [local source](../../../../../../source/modules/field/modules/number/number.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/number/number.module#L55-L88)
- **Module/theme:** number
- **Implements:** [hook_field_settings_form()](../../../../field_ui/field_ui.api.php/hook_field_settings_form.md)

## Signature

```php
function number_field_settings_form($field, $instance, $has_data)
```

## Documentation

```text
Implements hook_field_settings_form().
```

## Code

```php
function number_field_settings_form($field, $instance, $has_data) {
  $settings = $field['settings'];
  $form = array();

  if ($field['type'] == 'number_decimal') {
    $form['precision'] = array(
      '#type' => 'select',
      '#title' => t('Precision'),
      '#options' => drupal_map_assoc(range(10, 32)),
      '#default_value' => $settings['precision'],
      '#description' => t('The total number of digits to store in the database, including those to the right of the decimal.'),
      '#disabled' => $has_data,
    );
    $form['scale'] = array(
      '#type' => 'select',
      '#title' => t('Scale'),
      '#options' => drupal_map_assoc(range(0, 10)),
      '#default_value' => $settings['scale'],
      '#description' => t('The number of digits to the right of the decimal.'),
      '#disabled' => $has_data,
    );
  }
  if ($field['type'] == 'number_decimal' || $field['type'] == 'number_float') {
    $form['decimal_separator'] = array(
      '#type' => 'select',
      '#title' => t('Decimal marker'),
      '#options' => array('.' => t('Decimal point'), ',' => t('Comma')),
      '#default_value' => $settings['decimal_separator'],
      '#description' => t('The character users will input to mark the decimal point in forms.'),
    );
  }

  return $form;
}
```

---
_Drupal 7.103 · [modules/field/modules/number/number.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/number/number.module) · Licensed GPL-2.0-or-later (see LICENSE)._
