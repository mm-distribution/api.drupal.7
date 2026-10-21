# hook_field_instance_settings_form()

- **Type:** Hook (documentation function)
- **File:** [`modules/field_ui/field_ui.api.php`](_file.md), lines 65–91 · [local source](../../../../source/modules/field_ui/field_ui.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.api.php#L65-L91)
- **Module/theme:** field_ui
- **Topics:** [field_types](../../../topics/field_types.md)

## Signature

```php
function hook_field_instance_settings_form($field, $instance)
```

## Documentation

```text
Add settings to an instance field settings form.

Invoked from field_ui_field_edit_form() to allow the module defining the
field to add settings for a field instance.

@param $field
  The field structure being configured.
@param $instance
  The instance structure being configured.

@return
  The form definition for the field instance settings.
```

## Code

```php
function hook_field_instance_settings_form($field, $instance) {
  $settings = $instance['settings'];

  $form['text_processing'] = array(
    '#type' => 'radios',
    '#title' => t('Text processing'),
    '#default_value' => $settings['text_processing'],
    '#options' => array(
      t('Plain text'),
      t('Filtered text (user selects text format)'),
    ),
  );
  if ($field['type'] == 'text_with_summary') {
    $form['display_summary'] = array(
      '#type' => 'select',
      '#title' => t('Display summary'),
      '#options' => array(
        t('No'),
        t('Yes'),
      ),
      '#description' => t('Display the summary to allow the user to input a summary value. Hide the summary to automatically fill it with a trimmed portion from the main post.'),
      '#default_value' => !empty($settings['display_summary']) ? $settings['display_summary'] :  0,
    );
  }

  return $form;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_instance_settings_form()".

- [field_test_field_instance_settings_form()](../../field/tests/field_test.field.inc/field_test_field_instance_settings_form.md) — `modules/field/tests/field_test.field.inc`
- [file_field_instance_settings_form()](../../file/file.field.inc/file_field_instance_settings_form.md) — `modules/file/file.field.inc`
- [image_field_instance_settings_form()](../../image/image.field.inc/image_field_instance_settings_form.md) — `modules/image/image.field.inc`
- [number_field_instance_settings_form()](../../field/modules/number/number.module/number_field_instance_settings_form.md) — `modules/field/modules/number/number.module`
- [text_field_instance_settings_form()](../../field/modules/text/text.module/text_field_instance_settings_form.md) — `modules/field/modules/text/text.module`

---
_Drupal 7.103 · [modules/field_ui/field_ui.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
