# _file_test_form()

- **Type:** Function
- **File:** [`modules/simpletest/tests/file_test.module`](_file.md), lines 51–99 · [local source](../../../../../source/modules/simpletest/tests/file_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file_test.module#L51-L99)
- **Module/theme:** batch_test

## Signature

```php
function _file_test_form($form, &$form_state)
```

## Documentation

```text
Form to test file uploads.
```

## Code

```php
function _file_test_form($form, &$form_state) {
  $form['file_test_upload'] = array(
    '#type' => 'file',
    '#title' => t('Upload a file'),
  );
  $form['file_test_replace'] = array(
    '#type' => 'select',
    '#title' => t('Replace existing image'),
    '#options' => array(
      FILE_EXISTS_RENAME => t('Appends number until name is unique'),
      FILE_EXISTS_REPLACE => t('Replace the existing file'),
      FILE_EXISTS_ERROR => t('Fail with an error'),
    ),
    '#default_value' => FILE_EXISTS_RENAME,
  );
  $form['file_subdir'] = array(
    '#type' => 'textfield',
    '#title' => t('Subdirectory for test file'),
    '#default_value' => '',
  );

  $form['extensions'] = array(
    '#type' => 'textfield',
    '#title' => t('Allowed extensions.'),
    '#default_value' => '',
  );

  $form['allow_all_extensions'] = array(
    '#type' => 'radios',
    '#options' => array(
      'false' => 'No',
      'empty_array' => 'Empty array',
      'empty_string' => 'Empty string',
    ),
    '#default_value' => 'false',
  );

  $form['is_image_file'] = array(
    '#type' => 'checkbox',
    '#title' => t('Is this an image file?'),
    '#default_value' => TRUE,
  );

  $form['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Submit'),
  );
  return $form;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/file_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
