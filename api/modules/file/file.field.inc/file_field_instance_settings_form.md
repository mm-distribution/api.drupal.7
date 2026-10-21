# file_field_instance_settings_form()

- **Type:** Function
- **File:** [`modules/file/file.field.inc`](_file.md), lines 74–121 · [local source](../../../../source/modules/file/file.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc#L74-L121)
- **Module/theme:** file
- **Implements:** [hook_field_instance_settings_form()](../../field_ui/field_ui.api.php/hook_field_instance_settings_form.md)

## Signature

```php
function file_field_instance_settings_form($field, $instance)
```

## Documentation

```text
Implements hook_field_instance_settings_form().
```

## Code

```php
function file_field_instance_settings_form($field, $instance) {
  $settings = $instance['settings'];

  $form['file_directory'] = array(
    '#type' => 'textfield',
    '#title' => t('File directory'),
    '#default_value' => $settings['file_directory'],
    '#description' => t('Optional subdirectory within the upload destination where files will be stored. Do not include preceding or trailing slashes.'),
    '#element_validate' => array('_file_generic_settings_file_directory_validate'),
    '#weight' => 3,
  );

  // Make the extension list a little more human-friendly by comma-separation.
  $extensions = str_replace(' ', ', ', $settings['file_extensions']);
  $form['file_extensions'] = array(
    '#type' => 'textfield',
    '#title' => t('Allowed file extensions'),
    '#default_value' => $extensions,
    '#description' => t('Separate extensions with a space or comma and do not include the leading dot.'),
    '#element_validate' => array('_file_generic_settings_extensions'),
    '#weight' => 1,
    '#maxlength' => 256,
    // By making this field required, we prevent a potential security issue
    // that would allow files of any type to be uploaded.
    '#required' => TRUE,
  );

  $form['max_filesize'] = array(
    '#type' => 'textfield',
    '#title' => t('Maximum upload size'),
    '#default_value' => $settings['max_filesize'],
    '#description' => t('Enter a value like "512" (bytes), "80 KB" (kilobytes) or "50 MB" (megabytes) in order to restrict the allowed file size. If left empty the file sizes will be limited only by PHP\'s maximum post and file upload sizes (current limit <strong>%limit</strong>).', array('%limit' => format_size(file_upload_max_size()))),
    '#size' => 10,
    '#element_validate' => array('_file_generic_settings_max_filesize'),
    '#weight' => 5,
  );

  $form['description_field'] = array(
    '#type' => 'checkbox',
    '#title' => t('Enable <em>Description</em> field'),
    '#default_value' => isset($settings['description_field']) ? $settings['description_field'] : '',
    '#description' => t('The description field allows users to enter a description about the uploaded file.'),
    '#parents' => array('instance', 'settings', 'description_field'),
    '#weight' => 11,
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/file/file.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
