# file_field_settings_form()

- **Type:** Function
- **File:** [`modules/file/file.field.inc`](_file.md), lines 36–69 · [local source](../../../../source/modules/file/file.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc#L36-L69)
- **Module/theme:** file
- **Implements:** [hook_field_settings_form()](../../field_ui/field_ui.api.php/hook_field_settings_form.md)

## Signature

```php
function file_field_settings_form($field, $instance, $has_data)
```

## Documentation

```text
Implements hook_field_settings_form().
```

## Code

```php
function file_field_settings_form($field, $instance, $has_data) {
  $defaults = field_info_field_settings($field['type']);
  $settings = array_merge($defaults, $field['settings']);

  $form['#attached']['js'][] = drupal_get_path('module', 'file') . '/file.js';

  $form['display_field'] = array(
    '#type' => 'checkbox',
    '#title' => t('Enable <em>Display</em> field'),
    '#default_value' => $settings['display_field'],
    '#description' => t('The display option allows users to choose if a file should be shown when viewing the content.'),
  );
  $form['display_default'] = array(
    '#type' => 'checkbox',
    '#title' => t('Files displayed by default'),
    '#default_value' => $settings['display_default'],
    '#description' => t('This setting only has an effect if the display option is enabled.'),
  );

  $scheme_options = array();
  foreach (file_get_stream_wrappers(STREAM_WRAPPERS_WRITE_VISIBLE) as $scheme => $stream_wrapper) {
    $scheme_options[$scheme] = $stream_wrapper['name'];
  }
  $form['uri_scheme'] = array(
    '#type' => 'radios',
    '#title' => t('Upload destination'),
    '#options' => $scheme_options,
    '#default_value' => $settings['uri_scheme'],
    '#description' => t('Select where the final files should be stored. Private file storage has significantly more overhead than public files, but allows restricted access to files within this field.'),
    '#disabled' => $has_data,
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/file/file.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
