# hook_field_widget_settings_form()

- **Type:** Hook (documentation function)
- **File:** [`modules/field_ui/field_ui.api.php`](_file.md), lines 107–131 · [local source](../../../../source/modules/field_ui/field_ui.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.api.php#L107-L131)
- **Module/theme:** field_ui
- **Topics:** [field_types](../../../topics/field_types.md)

## Signature

```php
function hook_field_widget_settings_form($field, $instance)
```

## Documentation

```text
Add settings to a widget settings form.

Invoked from field_ui_field_edit_form() to allow the module defining the
widget to add settings for a widget instance.

@param $field
  The field structure being configured.
@param $instance
  The instance structure being configured.

@return
  The form definition for the widget settings.
```

## Code

```php
function hook_field_widget_settings_form($field, $instance) {
  $widget = $instance['widget'];
  $settings = $widget['settings'];

  if ($widget['type'] == 'text_textfield') {
    $form['size'] = array(
      '#type' => 'textfield',
      '#title' => t('Size of textfield'),
      '#default_value' => $settings['size'],
      '#element_validate' => array('element_validate_integer_positive'),
      '#required' => TRUE,
    );
  }
  else {
    $form['rows'] = array(
      '#type' => 'textfield',
      '#title' => t('Rows'),
      '#default_value' => $settings['rows'],
      '#element_validate' => array('element_validate_integer_positive'),
      '#required' => TRUE,
    );
  }

  return $form;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_widget_settings_form()".

- [field_test_field_widget_settings_form()](../../field/tests/field_test.field.inc/field_test_field_widget_settings_form.md) — `modules/field/tests/field_test.field.inc`
- [file_field_widget_settings_form()](../../file/file.field.inc/file_field_widget_settings_form.md) — `modules/file/file.field.inc`
- [image_field_widget_settings_form()](../../image/image.field.inc/image_field_widget_settings_form.md) — `modules/image/image.field.inc`
- [options_field_widget_settings_form()](../../field/modules/options/options.module/options_field_widget_settings_form.md) — `modules/field/modules/options/options.module`
- [text_field_widget_settings_form()](../../field/modules/text/text.module/text_field_widget_settings_form.md) — `modules/field/modules/text/text.module`

---
_Drupal 7.103 · [modules/field_ui/field_ui.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
