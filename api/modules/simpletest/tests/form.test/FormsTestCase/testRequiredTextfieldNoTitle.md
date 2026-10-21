# FormsTestCase::testRequiredTextfieldNoTitle()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 206–226 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L206-L226)
- **Class:** [FormsTestCase](../FormsTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testRequiredTextfieldNoTitle()
```

## Documentation

```text
Tests validation for required textfield element without title.

Submits a test form containing a textfield form elements without title.
The form is submitted twice, first without value for the required field
and then with value. Each submission is checked for relevant error
messages.

@see form_test_validate_required_form_no_title()
```

## Code

```php
  function testRequiredTextfieldNoTitle() {
    $form = $form_state = array();
    $form = form_test_validate_required_form_no_title($form, $form_state);

    // Attempt to submit the form with no required field set.
    $edit = array();
    $this->drupalPost('form-test/validate-required-no-title', $edit, 'Submit');
    $this->assertNoRaw("The form_test_validate_required_form_no_title form was submitted successfully.", 'Validation form submitted successfully.');

    // Check the page for the error class on the textfield.
    $this->assertFieldByXPath('//input[contains(@class, "error")]', FALSE, 'Error input form element class found.');

    // Submit again with required fields set and verify that there are no
    // error messages.
    $edit = array(
      'textfield' => $this->randomString(),
    );
    $this->drupalPost(NULL, $edit, 'Submit');
    $this->assertNoFieldByXpath('//input[contains(@class, "error")]', FALSE, 'No error input form element class found.');
    $this->assertRaw("The form_test_validate_required_form_no_title form was submitted successfully.", 'Validation form submitted successfully.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
