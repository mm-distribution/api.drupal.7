# file_field_widget_settings_form()

- **Type:** Function
- **File:** [`modules/file/file.field.inc`](_file.md), lines 440–458 · [local source](../../../../source/modules/file/file.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc#L440-L458)
- **Module/theme:** file
- **Implements:** [hook_field_widget_settings_form()](../../field_ui/field_ui.api.php/hook_field_widget_settings_form.md)

## Signature

```php
function file_field_widget_settings_form($field, $instance)
```

## Documentation

```text
Implements hook_field_widget_settings_form().
```

## Code

```php
function file_field_widget_settings_form($field, $instance) {
  $widget = $instance['widget'];
  $settings = $widget['settings'];

  $form['progress_indicator'] = array(
    '#type' => 'radios',
    '#title' => t('Progress indicator'),
    '#options' => array(
      'throbber' => t('Throbber'),
      'bar' => t('Bar with progress meter'),
    ),
    '#default_value' => $settings['progress_indicator'],
    '#description' => t('The throbber display does not show the status of uploads but takes up less space. The progress bar is helpful for monitoring progress on large uploads.'),
    '#weight' => 16,
    '#access' => file_progress_implementation(),
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/file/file.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
