# file_module_test_form_submit()

- **Type:** Function
- **File:** [`modules/file/tests/file_module_test.module`](_file.md), lines 61–69 · [local source](../../../../../source/modules/file/tests/file_module_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file_module_test.module#L61-L69)
- **Module/theme:** file_module_test

## Signature

```php
function file_module_test_form_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for file_module_test_form().
```

## Code

```php
function file_module_test_form_submit($form, &$form_state) {
  if ($form['#tree']) {
    $fid = $form['nested']['file']['#extended'] ? $form_state['values']['nested']['file']['fid'] : $form_state['values']['nested']['file'];
  }
  else {
    $fid = $form['nested']['file']['#extended'] ? $form_state['values']['file']['fid'] : $form_state['values']['file'];
  }
  drupal_set_message(t('The file id is %fid.', array('%fid' => $fid)));
}
```

---
_Drupal 7.103 · [modules/file/tests/file_module_test.module](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file_module_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
