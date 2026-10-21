# hook_field_formatter_settings_form()

- **Type:** Hook (documentation function)
- **File:** [`modules/field_ui/field_ui.api.php`](_file.md), lines 154–173 · [local source](../../../../source/modules/field_ui/field_ui.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.api.php#L154-L173)
- **Module/theme:** field_ui
- **Topics:** [field_types](../../../topics/field_types.md)

## Signature

```php
function hook_field_formatter_settings_form($field, $instance, $view_mode, $form, &$form_state)
```

## Documentation

```text
Specify the form elements for a formatter's settings.

This hook is only invoked if hook_field_formatter_settings_summary()
returns a non-empty value.

@param $field
  The field structure being configured.
@param $instance
  The instance structure being configured.
@param $view_mode
  The view mode being configured.
@param $form
  The (entire) configuration form array, which will usually have no use here.
@param $form_state
  The form state of the (entire) configuration form.

@return
  The form elements for the formatter settings.
```

## Code

```php
function hook_field_formatter_settings_form($field, $instance, $view_mode, $form, &$form_state) {
  $display = $instance['display'][$view_mode];
  $settings = $display['settings'];

  $element = array();

  if ($display['type'] == 'text_trimmed' || $display['type'] == 'text_summary_or_trimmed') {
    $element['trim_length'] = array(
      '#title' => t('Length'),
      '#type' => 'textfield',
      '#size' => 20,
      '#default_value' => $settings['trim_length'],
      '#element_validate' => array('element_validate_integer_positive'),
      '#required' => TRUE,
    );
  }

  return $element;

}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_formatter_settings_form()".

- [field_test_field_formatter_settings_form()](../../field/tests/field_test.field.inc/field_test_field_formatter_settings_form.md) — `modules/field/tests/field_test.field.inc`
- [image_field_formatter_settings_form()](../../image/image.field.inc/image_field_formatter_settings_form.md) — `modules/image/image.field.inc`
- [number_field_formatter_settings_form()](../../field/modules/number/number.module/number_field_formatter_settings_form.md) — `modules/field/modules/number/number.module`
- [text_field_formatter_settings_form()](../../field/modules/text/text.module/text_field_formatter_settings_form.md) — `modules/field/modules/text/text.module`

---
_Drupal 7.103 · [modules/field_ui/field_ui.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
