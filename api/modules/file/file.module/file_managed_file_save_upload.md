# file_managed_file_save_upload()

- **Type:** Function
- **File:** [`modules/file/file.module`](_file.md), lines 703–723 · [local source](../../../../source/modules/file/file.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.module#L703-L723)
- **Module/theme:** file

## Signature

```php
function file_managed_file_save_upload($element)
```

## Documentation

```text
Saves any files that have been uploaded into a managed_file element.

@param $element
  The FAPI element whose values are being saved.

@return
  The file object representing the file that was saved, or FALSE if no file
  was saved.
```

## Code

```php
function file_managed_file_save_upload($element) {
  $upload_name = implode('_', $element['#parents']);
  if (empty($_FILES['files']['name'][$upload_name])) {
    return FALSE;
  }

  $destination = isset($element['#upload_location']) ? $element['#upload_location'] : NULL;
  if (isset($destination) && !file_prepare_directory($destination, FILE_CREATE_DIRECTORY)) {
    watchdog('file', 'The upload directory %directory for the file field !name could not be created or is not accessible. A newly uploaded file could not be saved in this directory as a consequence, and the upload was canceled.', array('%directory' => $destination, '!name' => $element['#field_name']));
    form_set_error($upload_name, t('The file could not be uploaded.'));
    return FALSE;
  }

  if (!$file = file_save_upload($upload_name, $element['#upload_validators'], $destination)) {
    watchdog('file', 'The file upload failed. %upload', array('%upload' => $upload_name));
    form_set_error($upload_name, t('The file in the !name field was unable to be uploaded.', array('!name' => $element['#title'])));
    return FALSE;
  }

  return $file;
}
```

---
_Drupal 7.103 · [modules/file/file.module](https://github.com/drupal/drupal/blob/7.103/modules/file/file.module) · Licensed GPL-2.0-or-later (see LICENSE)._
