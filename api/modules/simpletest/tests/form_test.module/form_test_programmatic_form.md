# form_test_programmatic_form()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 1695–1755 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L1695-L1755)
- **Module/theme:** batch_test

## Signature

```php
function form_test_programmatic_form($form, &$form_state)
```

## Documentation

```text
Form builder to test programmatic form submissions.
```

## Code

```php
function form_test_programmatic_form($form, &$form_state) {
  $form['textfield'] = array(
    '#title' => 'Textfield',
    '#type' => 'textfield',
  );

  $form['checkboxes'] = array(
    '#type' => 'checkboxes',
    '#options' => array(
      1 => 'First checkbox',
      2 => 'Second checkbox',
    ),
    // Both checkboxes are selected by default so that we can test the ability
    // of programmatic form submissions to uncheck them.
    '#default_value' => array(1, 2),
  );

  // This is used to test that programmatic form submissions can bypass #access
  // restrictions.
  $form['textfield_no_access'] = array(
    '#type' => 'textfield',
    '#title' => 'Textfield no access',
    '#default_value' => 'default value',
    '#access' => FALSE,
  );

  $form['field_to_validate'] = array(
    '#type' => 'radios',
    '#title' => 'Field to validate (in the case of limited validation)',
    '#description' => 'If the form is submitted by clicking the "Submit with limited validation" button, then validation can be limited based on the value of this radio button.',
    '#options' => array(
      'all' => 'Validate all fields',
      'textfield' => 'Validate the "Textfield" field',
      'field_to_validate' => 'Validate the "Field to validate" field',
    ),
    '#default_value' => 'all',
  );

  // The main submit button for the form.
  $form['submit'] = array(
    '#type' => 'submit',
    '#value' => 'Submit',
  );
  // A secondary submit button that allows validation to be limited based on
  // the value of the above radio selector.
  $form['submit_limit_validation'] = array(
    '#type' => 'submit',
    '#value' => 'Submit with limited validation',
    // Use the same submit handler for this button as for the form itself.
    // (This must be set explicitly or otherwise the form API will ignore the
    // #limit_validation_errors property.)
    '#submit' => array('form_test_programmatic_form_submit'),
  );
  if (!empty($form_state['input']['field_to_validate']) && $form_state['input']['field_to_validate'] != 'all') {
    $form['submit_limit_validation']['#limit_validation_errors'] = array(
      array($form_state['input']['field_to_validate']),
    );
  }

  return $form;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
