# text_field_formatter_settings_form()

- **Type:** Function
- **File:** [`modules/field/modules/text/text.module`](_file.md), lines 218–238 · [local source](../../../../../../source/modules/field/modules/text/text.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.module#L218-L238)
- **Module/theme:** text
- **Implements:** [hook_field_formatter_settings_form()](../../../../field_ui/field_ui.api.php/hook_field_formatter_settings_form.md)

## Signature

```php
function text_field_formatter_settings_form($field, $instance, $view_mode, $form, &$form_state)
```

## Documentation

```text
Implements hook_field_formatter_settings_form().
```

## Code

```php
function text_field_formatter_settings_form($field, $instance, $view_mode, $form, &$form_state) {
  $display = $instance['display'][$view_mode];
  $settings = $display['settings'];

  $element = array();

  if (strpos($display['type'], '_trimmed') !== FALSE) {
    $element['trim_length'] = array(
      '#title' => t('Trimmed limit'),
      '#type' => 'textfield',
      '#field_suffix' => t('characters'),
      '#size' => 10,
      '#default_value' => $settings['trim_length'],
      '#element_validate' => array('element_validate_integer_positive'),
      '#description' => t('If the summary is not set, the trimmed %label field will be shorter than this character limit.', array('%label' => $instance['label'])),
      '#required' => TRUE,
    );
  }

  return $element;
}
```

---
_Drupal 7.103 · [modules/field/modules/text/text.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.module) · Licensed GPL-2.0-or-later (see LICENSE)._
