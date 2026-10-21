# system_check_directory()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 2206–2235 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L2206-L2235)
- **Module/theme:** system

## Signature

```php
function system_check_directory($form_element)
```

## Documentation

```text
Checks the existence of the directory specified in $form_element.

This function is called from the system_settings form to check all core
file directories (file_public_path, file_private_path, file_temporary_path).

@param $form_element
  The form element containing the name of the directory to check.
```

## Code

```php
function system_check_directory($form_element) {
  $directory = $form_element['#value'];
  if (strlen($directory) == 0) {
    return $form_element;
  }

  if (!is_dir($directory) && !drupal_mkdir($directory, NULL, TRUE)) {
    // If the directory does not exists and cannot be created.
    form_set_error($form_element['#parents'][0], t('The directory %directory does not exist and could not be created.', array('%directory' => $directory)));
    watchdog('file system', 'The directory %directory does not exist and could not be created.', array('%directory' => $directory), WATCHDOG_ERROR);
  }

  if (is_dir($directory) && !is_writable($directory) && !drupal_chmod($directory)) {
    // If the directory is not writable and cannot be made so.
    form_set_error($form_element['#parents'][0], t('The directory %directory exists but is not writable and could not be made writable.', array('%directory' => $directory)));
    watchdog('file system', 'The directory %directory exists but is not writable and could not be made writable.', array('%directory' => $directory), WATCHDOG_ERROR);
  }
  elseif (is_dir($directory)) {
    if ($form_element['#name'] == 'file_public_path') {
      // Create public .htaccess file.
      file_create_htaccess($directory, FALSE);
    }
    else {
      // Create private .htaccess file.
      file_create_htaccess($directory);
    }
  }

  return $form_element;
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
