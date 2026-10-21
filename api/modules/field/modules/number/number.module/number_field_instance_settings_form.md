# number_field_instance_settings_form()

- **Type:** Function
- **File:** [`modules/field/modules/number/number.module`](_file.md), lines 93–126 · [local source](../../../../../../source/modules/field/modules/number/number.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/number/number.module#L93-L126)
- **Module/theme:** number
- **Implements:** [hook_field_instance_settings_form()](../../../../field_ui/field_ui.api.php/hook_field_instance_settings_form.md)

## Signature

```php
function number_field_instance_settings_form($field, $instance)
```

## Documentation

```text
Implements hook_field_instance_settings_form().
```

## Code

```php
function number_field_instance_settings_form($field, $instance) {
  $settings = $instance['settings'];

  $form['min'] = array(
    '#type' => 'textfield',
    '#title' => t('Minimum'),
    '#default_value' => $settings['min'],
    '#description' => t('The minimum value that should be allowed in this field. Leave blank for no minimum.'),
    '#element_validate' => array('element_validate_number'),
  );
  $form['max'] = array(
    '#type' => 'textfield',
    '#title' => t('Maximum'),
    '#default_value' => $settings['max'],
    '#description' => t('The maximum value that should be allowed in this field. Leave blank for no maximum.'),
    '#element_validate' => array('element_validate_number'),
  );
  $form['prefix'] = array(
    '#type' => 'textfield',
    '#title' => t('Prefix'),
    '#default_value' => $settings['prefix'],
    '#size' => 60,
    '#description' => t("Define a string that should be prefixed to the value, like '$ ' or '&euro; '. Leave blank for none. Separate singular and plural values with a pipe ('pound|pounds')."),
  );
  $form['suffix'] = array(
    '#type' => 'textfield',
    '#title' => t('Suffix'),
    '#default_value' => $settings['suffix'],
    '#size' => 60,
    '#description' => t("Define a string that should be suffixed to the value, like ' m', ' kb/s'. Leave blank for none. Separate singular and plural values with a pipe ('pound|pounds')."),
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/field/modules/number/number.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/number/number.module) · Licensed GPL-2.0-or-later (see LICENSE)._
