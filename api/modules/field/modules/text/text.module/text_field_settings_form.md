# text_field_settings_form()

- **Type:** Function
- **File:** [`modules/field/modules/text/text.module`](_file.md), lines 62–82 · [local source](../../../../../../source/modules/field/modules/text/text.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.module#L62-L82)
- **Module/theme:** text
- **Implements:** [hook_field_settings_form()](../../../../field_ui/field_ui.api.php/hook_field_settings_form.md)

## Signature

```php
function text_field_settings_form($field, $instance, $has_data)
```

## Documentation

```text
Implements hook_field_settings_form().
```

## Code

```php
function text_field_settings_form($field, $instance, $has_data) {
  $settings = $field['settings'];

  $form = array();

  if ($field['type'] == 'text') {
    $form['max_length'] = array(
      '#type' => 'textfield',
      '#title' => t('Maximum length'),
      '#default_value' => $settings['max_length'],
      '#required' => TRUE,
      '#description' => t('The maximum length of the field in characters.'),
      '#element_validate' => array('element_validate_integer_positive'),
      // @todo: If $has_data, add a validate handler that only allows
      // max_length to increase.
      '#disabled' => $has_data,
    );
  }

  return $form;
}
```

---
_Drupal 7.103 · [modules/field/modules/text/text.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.module) · Licensed GPL-2.0-or-later (see LICENSE)._
