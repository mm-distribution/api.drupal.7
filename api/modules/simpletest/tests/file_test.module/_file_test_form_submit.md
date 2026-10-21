# _file_test_form_submit()

- **Type:** Function
- **File:** [`modules/simpletest/tests/file_test.module`](_file.md), lines 104–143 · [local source](../../../../../source/modules/simpletest/tests/file_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file_test.module#L104-L143)
- **Module/theme:** batch_test

## Signature

```php
function _file_test_form_submit(&$form, &$form_state)
```

## Documentation

```text
Process the upload.
```

## Code

```php
function _file_test_form_submit(&$form, &$form_state) {
  // Process the upload and perform validation. Note: we're using the
  // form value for the $replace parameter.
  if (!empty($form_state['values']['file_subdir'])) {
    $destination = 'temporary://' . $form_state['values']['file_subdir'];
    file_prepare_directory($destination, FILE_CREATE_DIRECTORY);
  }
  else {
    $destination = FALSE;
  }

  // Setup validators.
  $validators = array();
  if ($form_state['values']['is_image_file']) {
    $validators['file_validate_is_image'] = array();
  }

  $allow = $form_state['values']['allow_all_extensions'];
  if ($allow === 'empty_array') {
    $validators['file_validate_extensions'] = array();
  }
  elseif ($allow === 'empty_string') {
    $validators['file_validate_extensions'] = array('');
  }
  elseif (!empty($form_state['values']['extensions'])) {
    $validators['file_validate_extensions'] = array($form_state['values']['extensions']);
  }

  $file = file_save_upload('file_test_upload', $validators, $destination, $form_state['values']['file_test_replace']);
  if ($file) {
    $form_state['values']['file_test_upload'] = $file;
    drupal_set_message(t('File @filepath was uploaded.', array('@filepath' => $file->uri)));
    drupal_set_message(t('File name is @filename.', array('@filename' => $file->filename)));
    drupal_set_message(t('File MIME type is @mimetype.', array('@mimetype' => $file->filemime)));
    drupal_set_message(t('You WIN!'));
  }
  elseif ($file === FALSE) {
    drupal_set_message(t('Epic upload FAIL!'), 'error');
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/file_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
