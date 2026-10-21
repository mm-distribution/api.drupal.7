# FormsTestCase::checkFormValue()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 508–533 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L508-L533)
- **Class:** [FormsTestCase](../FormsTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
protected function checkFormValue($element_type, $input_value, $expected_value)
```

## Documentation

```text
Checks that a given form input value is sanitized to the expected result.

@param string $element_type
  The form element type. Example: textfield.
@param mixed $input_value
  The submitted user input value for the form element.
@param mixed $expected_value
  The sanitized result value in the form state after calling
  form_builder().
```

## Code

```php
  protected function checkFormValue($element_type, $input_value, $expected_value) {
    $form_id = $this->randomName();
    $form = array();
    $form_state = form_state_defaults();
    $form['op'] = array('#type' => 'submit', '#value' => t('Submit'));
    $form[$element_type] = array(
      '#type' => $element_type,
      '#title' => 'test',
    );

    $form_state['input'][$element_type] = $input_value;
    $form_state['input']['form_id'] = $form_id;
    $form_state['method'] = 'post';
    $form_state['values'] = array();
    drupal_prepare_form($form_id, $form, $form_state);

    // Set the CSRF token in the user-provided input.
    $form_state['input']['form_token'] = $form['form_token']['#default_value'];

    // This is the main function we want to test: it is responsible for
    // populating user supplied $form_state['input'] to sanitized
    // $form_state['values'].
    form_builder($form_id, $form, $form_state);

    $this->assertIdentical($form_state['values'][$element_type], $expected_value, format_string('Form submission for the "@element_type" element type has been correctly sanitized.', array('@element_type' => $element_type)));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
