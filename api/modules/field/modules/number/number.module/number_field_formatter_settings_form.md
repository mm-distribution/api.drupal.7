# number_field_formatter_settings_form()

- **Type:** Function
- **File:** [`modules/field/modules/number/number.module`](_file.md), lines 230–274 · [local source](../../../../../../source/modules/field/modules/number/number.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/number/number.module#L230-L274)
- **Module/theme:** number
- **Implements:** [hook_field_formatter_settings_form()](../../../../field_ui/field_ui.api.php/hook_field_formatter_settings_form.md)

## Signature

```php
function number_field_formatter_settings_form($field, $instance, $view_mode, $form, &$form_state)
```

## Documentation

```text
Implements hook_field_formatter_settings_form().
```

## Code

```php
function number_field_formatter_settings_form($field, $instance, $view_mode, $form, &$form_state) {
  $display = $instance['display'][$view_mode];
  $settings = $display['settings'];

  $element = array();

  if ($display['type'] == 'number_decimal' || $display['type'] == 'number_integer') {
    $options = array(
      ''  => t('<none>'),
      '.' => t('Decimal point'),
      ',' => t('Comma'),
      ' ' => t('Space'),
    );
    $element['thousand_separator'] = array(
      '#type' => 'select',
      '#title' => t('Thousand marker'),
      '#options' => $options,
      '#default_value' => $settings['thousand_separator'],
    );

    if ($display['type'] == 'number_decimal') {
      $element['decimal_separator'] = array(
        '#type' => 'select',
        '#title' => t('Decimal marker'),
        '#options' => array('.' => t('Decimal point'), ',' => t('Comma')),
        '#default_value' => $settings['decimal_separator'],
      );
      $element['scale'] = array(
        '#type' => 'select',
        '#title' => t('Scale'),
        '#options' => drupal_map_assoc(range(0, 10)),
        '#default_value' => $settings['scale'],
        '#description' => t('The number of digits to the right of the decimal.'),
      );
    }

    $element['prefix_suffix'] = array(
      '#type' => 'checkbox',
      '#title' => t('Display prefix and suffix.'),
      '#default_value' => $settings['prefix_suffix'],
    );
  }

  return $element;
}
```

---
_Drupal 7.103 · [modules/field/modules/number/number.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/number/number.module) · Licensed GPL-2.0-or-later (see LICENSE)._
