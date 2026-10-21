# _form_test_checkbox()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 1121–1183 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L1121-L1183)
- **Module/theme:** batch_test

## Signature

```php
function _form_test_checkbox($form, &$form_state)
```

## Documentation

```text
Build a form to test a checkbox.
```

## Code

```php
function _form_test_checkbox($form, &$form_state) {
  // A required checkbox.
  $form['required_checkbox'] = array(
    '#type' => 'checkbox',
    '#required' => TRUE,
    '#title' => 'required_checkbox',
  );

  // A disabled checkbox should get its default value back.
  $form['disabled_checkbox_on'] = array(
    '#type' => 'checkbox',
    '#disabled' => TRUE,
    '#return_value' => 'disabled_checkbox_on',
    '#default_value' => 'disabled_checkbox_on',
    '#title' => 'disabled_checkbox_on',
  );
  $form['disabled_checkbox_off'] = array(
    '#type' => 'checkbox',
    '#disabled' => TRUE,
    '#return_value' => 'disabled_checkbox_off',
    '#default_value' => NULL,
    '#title' => 'disabled_checkbox_off',
  );

  // A checkbox is active when #default_value == #return_value.
  $form['checkbox_on'] = array(
    '#type' => 'checkbox',
    '#return_value' => 'checkbox_on',
    '#default_value' => 'checkbox_on',
    '#title' => 'checkbox_on',
  );

  // But inactive in any other case.
  $form['checkbox_off'] = array(
    '#type' => 'checkbox',
    '#return_value' => 'checkbox_off',
    '#default_value' => 'checkbox_on',
    '#title' => 'checkbox_off',
  );

  // Checkboxes with a #return_value of '0' are supported.
  $form['zero_checkbox_on'] = array(
    '#type' => 'checkbox',
    '#return_value' => '0',
    '#default_value' => '0',
    '#title' => 'zero_checkbox_on',
  );

  // In that case, passing a #default_value != '0' means that the checkbox is off.
  $form['zero_checkbox_off'] = array(
    '#type' => 'checkbox',
    '#return_value' => '0',
    '#default_value' => '1',
    '#title' => 'zero_checkbox_off',
  );

  $form['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Submit')
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
