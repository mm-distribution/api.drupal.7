# FormsTestCase::testRequiredCheckboxesRadio()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 137–194 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L137-L194)
- **Class:** [FormsTestCase](../FormsTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testRequiredCheckboxesRadio()
```

## Documentation

```text
Tests validation for required checkbox, select, and radio elements.

Submits a test form containing several types of form elements. The form
is submitted twice, first without values for required fields and then
with values. Each submission is checked for relevant error messages.

@see form_test_validate_required_form()
```

## Code

```php
  function testRequiredCheckboxesRadio() {
    $form = $form_state = array();
    $form = form_test_validate_required_form($form, $form_state);

    // Attempt to submit the form with no required fields set.
    $edit = array();
    $this->drupalPost('form-test/validate-required', $edit, 'Submit');

    // The only error messages that should appear are the relevant 'required'
    // messages for each field.
    $expected = array();
    foreach (array('textfield', 'checkboxes', 'select', 'radios') as $key) {
      $expected[] = t('!name field is required.', array('!name' => $form[$key]['#title']));
    }

    // Check the page for error messages.
    $errors = $this->xpath('//div[contains(@class, "error")]//li');
    foreach ($errors as $error) {
      $expected_key = array_search($error[0], $expected);
      // If the error message is not one of the expected messages, fail.
      if ($expected_key === FALSE) {
        $this->fail(format_string("Unexpected error message: @error", array('@error' => $error[0])));
      }
      // Remove the expected message from the list once it is found.
      else {
        unset($expected[$expected_key]);
      }
    }

    // Fail if any expected messages were not found.
    foreach ($expected as $not_found) {
      $this->fail(format_string("Found error message: @error", array('@error' => $not_found)));
    }

    // Verify that input elements are still empty.
    $this->assertFieldByName('textfield', '');
    $this->assertNoFieldChecked('edit-checkboxes-foo');
    $this->assertNoFieldChecked('edit-checkboxes-bar');
    $this->assertOptionSelected('edit-select', '');
    $this->assertNoFieldChecked('edit-radios-foo');
    $this->assertNoFieldChecked('edit-radios-bar');
    $this->assertNoFieldChecked('edit-radios-optional-foo');
    $this->assertNoFieldChecked('edit-radios-optional-bar');
    $this->assertNoFieldChecked('edit-radios-optional-default-value-false-foo');
    $this->assertNoFieldChecked('edit-radios-optional-default-value-false-bar');

    // Submit again with required fields set and verify that there are no
    // error messages.
    $edit = array(
      'textfield' => $this->randomString(),
      'checkboxes[foo]' => TRUE,
      'select' => 'foo',
      'radios' => 'bar',
    );
    $this->drupalPost(NULL, $edit, 'Submit');
    $this->assertNoFieldByXpath('//div[contains(@class, "error")]', FALSE, 'No error message is displayed when all required fields are filled.');
    $this->assertRaw("The form_test_validate_required_form form was submitted successfully.", 'Validation form submitted successfully.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
