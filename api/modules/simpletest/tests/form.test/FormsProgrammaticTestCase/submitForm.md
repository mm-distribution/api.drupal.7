# FormsProgrammaticTestCase::submitForm()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 1973–1999 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L1973-L1999)
- **Class:** [FormsProgrammaticTestCase](../FormsProgrammaticTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
private function submitForm($values, $valid_input, $expected_values = NULL, $form_state = array())
```

## Documentation

```text
Helper function used to programmatically submit the form defined in
form_test.module with the given values.

@param $values
  An array of field values to be submitted.
@param $valid_input
  A boolean indicating whether or not the form submission is expected to
  be valid.
@param $expected_values
  (Optional) An array of field values that are expected to be stored by
  the form submit handler. If not set, the submitted $values are assumed
  to also be the expected stored values.
@param $form_state
  (Optional) A keyed array containing the state of the form, to be sent in
  the call to drupal_form_submit(). The $values parameter is added to
  $form_state['values'] by default, if it is not already set.
```

## Code

```php
  private function submitForm($values, $valid_input, $expected_values = NULL, $form_state = array()) {
    // Programmatically submit the given values.
    $form_state += array('values' => $values);
    drupal_form_submit('form_test_programmatic_form', $form_state);

    // Check that the form returns an error when expected, and vice versa.
    $errors = form_get_errors();
    $valid_form = empty($errors);
    $args = array(
      '%values' => print_r($values, TRUE),
      '%errors' => $valid_form ? t('None') : implode(' ', $errors),
    );
    $this->assertTrue($valid_input == $valid_form, format_string('Input values: %values<br/>Validation handler errors: %errors', $args));

    // We check submitted values only if we have a valid input.
    if ($valid_input) {
      // By fetching the values from $form_state['storage'] we ensure that the
      // submission handler was properly executed.
      $stored_values = $form_state['storage']['programmatic_form_submit'];
      if (!isset($expected_values)) {
        $expected_values = $values;
      }
      foreach ($expected_values as $key => $value) {
        $this->assertTrue(isset($stored_values[$key]) && $stored_values[$key] == $value, format_string('Submission handler correctly executed: %stored_key is %stored_value', array('%stored_key' => $key, '%stored_value' => print_r($value, TRUE))));
      }
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
