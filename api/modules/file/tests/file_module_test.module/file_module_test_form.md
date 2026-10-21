# file_module_test_form()

- **Type:** Function
- **File:** [`modules/file/tests/file_module_test.module`](_file.md), lines 30–56 · [local source](../../../../../source/modules/file/tests/file_module_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file_module_test.module#L30-L56)
- **Module/theme:** file_module_test
- **Topics:** [forms](../../../../topics/forms.md)

## Signature

```php
function file_module_test_form($form, &$form_state, $tree = TRUE, $extended = FALSE, $default_fid = NULL)
```

## Documentation

```text
Form constructor for testing a 'managed_file' element.

@see file_module_test_form_submit()
@ingroup forms
```

## Code

```php
function file_module_test_form($form, &$form_state, $tree = TRUE, $extended = FALSE, $default_fid = NULL) {
  $form['#tree'] = (bool) $tree;

  $form['nested']['file'] = array(
    '#type' => 'managed_file',
    '#title' => t('Managed file'),
    '#upload_location' => 'public://test',
    '#progress_message' => t('Please wait...'),
    '#extended' => (bool) $extended,
    '#size' => 13,
  );
  if ($default_fid) {
    $form['nested']['file']['#default_value'] = $extended ? array('fid' => $default_fid) : $default_fid;
  }

  $form['textfield'] = array(
    '#type' => 'textfield',
    '#title' => t('Type a value and ensure it stays'),
  );

  $form['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Save'),
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/file/tests/file_module_test.module](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file_module_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
