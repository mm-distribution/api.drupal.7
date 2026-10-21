# user_validate_picture()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 691–712 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L691-L712)
- **Module/theme:** user

## Signature

```php
function user_validate_picture(&$form, &$form_state)
```

## Documentation

```text
Validates an image uploaded by a user.

@see user_account_form()
```

## Code

```php
function user_validate_picture(&$form, &$form_state) {
  // If required, validate the uploaded picture.
  $validators = array(
    'file_validate_is_image' => array(),
    'file_validate_image_resolution' => array(variable_get('user_picture_dimensions', '85x85')),
    'file_validate_size' => array((int) variable_get('user_picture_file_size', '30') * 1024),
    // file_validate_is_image() uses the image toolkit to validate whether the
    // file is a valid image type, so set file_validate_extensions to an empty
    // array in order to signal to file_save_upload() that there is no need to
    // validate the upload against a default list of file extensions.
    'file_validate_extensions' => array(),
  );

  // Save the file as a temporary file.
  $file = file_save_upload('picture_upload', $validators);
  if ($file === FALSE) {
    form_set_error('picture_upload', t("Failed to upload the picture image; the %directory directory doesn't exist or is not writable.", array('%directory' => variable_get('user_picture_path', 'pictures'))));
  }
  elseif ($file !== NULL) {
    $form_state['values']['picture_upload'] = $file;
  }
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
