# form_test_checkboxes_zero()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 1962–1988 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L1962-L1988)
- **Module/theme:** batch_test

## Signature

```php
function form_test_checkboxes_zero($form, &$form_state, $json = TRUE)
```

## Documentation

_No docblock in source._

## Code

```php
function form_test_checkboxes_zero($form, &$form_state, $json = TRUE) {
  $form['checkbox_off'] = array(
    '#type' => 'checkboxes',
    '#options' => array('foo', 'bar', 'baz'),
  );
  $form['checkbox_zero_default'] = array(
    '#type' => 'checkboxes',
    '#options' => array('foo', 'bar', 'baz'),
    '#default_value' => array(0),
  );
  $form['checkbox_string_zero_default'] = array(
    '#type' => 'checkboxes',
    '#options' => array('foo', 'bar', 'baz'),
    '#default_value' => array('0'),
  );
  $form['submit'] = array(
    '#type' => 'submit',
    '#value' => 'Save',
  );
  if ($json) {
    $form['#submit'][] = '_form_test_checkbox_submit';
  }
  else {
    $form['#submit'][] = '_form_test_checkboxes_zero_no_redirect';
  }
  return $form;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
