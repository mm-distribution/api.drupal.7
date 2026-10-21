# system_file_system_settings()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 1815–1859 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L1815-L1859)
- **Module/theme:** system
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function system_file_system_settings()
```

## Documentation

```text
Form builder; Configure the site file handling.

@ingroup forms
@see system_settings_form()
```

## Code

```php
function system_file_system_settings() {
  $form['file_public_path'] = array(
    '#type' => 'textfield',
    '#title' => t('Public file system path'),
    '#default_value' => variable_get('file_public_path', conf_path() . '/files'),
    '#maxlength' => 255,
    '#description' => t('A local file system path where public files will be stored. This directory must exist and be writable by Drupal. This directory must be relative to the Drupal installation directory and be accessible over the web.'),
    '#after_build' => array('system_check_directory'),
  );

  $form['file_private_path'] = array(
    '#type' => 'textfield',
    '#title' => t('Private file system path'),
    '#default_value' => variable_get('file_private_path', ''),
    '#maxlength' => 255,
    '#description' => t('An existing local file system path for storing private files. It should be writable by Drupal and not accessible over the web. See the online handbook for <a href="@handbook">more information about securing private files</a>.', array('@handbook' => 'https://www.drupal.org/docs/7/core/modules/file/overview')),
    '#after_build' => array('system_check_directory'),
  );

  $form['file_temporary_path'] = array(
    '#type' => 'textfield',
    '#title' => t('Temporary directory'),
    '#default_value' => variable_get('file_temporary_path', file_directory_temp()),
    '#maxlength' => 255,
    '#description' => t('A local file system path where temporary files will be stored. This directory should not be accessible over the web.'),
    '#after_build' => array('system_check_directory'),
  );
  // Any visible, writeable wrapper can potentially be used for the files
  // directory, including a remote file system that integrates with a CDN.
  foreach (file_get_stream_wrappers(STREAM_WRAPPERS_WRITE_VISIBLE) as $scheme => $info) {
    $options[$scheme] = check_plain($info['description']);
  }

  if (!empty($options)) {
    $form['file_default_scheme'] = array(
      '#type' => 'radios',
      '#title' => t('Default download method'),
      '#default_value' => variable_get('file_default_scheme', isset($options['public']) ? 'public' : key($options)),
      '#options' => $options,
      '#description' => t('This setting is used as the preferred download method. The use of public files is more efficient, but does not provide any access control.'),
    );
  }

  return system_settings_form($form);
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
