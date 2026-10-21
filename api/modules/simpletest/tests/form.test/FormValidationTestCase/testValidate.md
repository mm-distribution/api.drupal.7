# FormValidationTestCase::testValidate()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 662–707 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L662-L707)
- **Class:** [FormValidationTestCase](../FormValidationTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testValidate()
```

## Documentation

```text
Tests form alterations by #element_validate, #validate, and form_set_value().
```

## Code

```php
  function testValidate() {
    $this->drupalGet('form-test/validate');
    // Verify that #element_validate handlers can alter the form and submitted
    // form values.
    $edit = array(
      'name' => 'element_validate',
    );
    $this->drupalPost(NULL, $edit, 'Save');
    $this->assertFieldByName('name', '#value changed by #element_validate', 'Form element #value was altered.');
    $this->assertText('Name value: value changed by form_set_value() in #element_validate', 'Form element value in $form_state was altered.');

    // Verify that #validate handlers can alter the form and submitted
    // form values.
    $edit = array(
      'name' => 'validate',
    );
    $this->drupalPost(NULL, $edit, 'Save');
    $this->assertFieldByName('name', '#value changed by #validate', 'Form element #value was altered.');
    $this->assertText('Name value: value changed by form_set_value() in #validate', 'Form element value in $form_state was altered.');

    // Verify that #element_validate handlers can make form elements
    // inaccessible, but values persist.
    $edit = array(
      'name' => 'element_validate_access',
    );
    $this->drupalPost(NULL, $edit, 'Save');
    $this->assertNoFieldByName('name', 'Form element was hidden.');
    $this->assertText('Name value: element_validate_access', 'Value for inaccessible form element exists.');

    // Verify that value for inaccessible form element persists.
    $this->drupalPost(NULL, array(), 'Save');
    $this->assertNoFieldByName('name', 'Form element was hidden.');
    $this->assertText('Name value: element_validate_access', 'Value for inaccessible form element exists.');

    // Verify that #validate handlers don't run if the CSRF token is invalid.
    $this->drupalLogin($this->drupalCreateUser());
    $this->drupalGet('form-test/validate');
    $edit = array(
      'name' => 'validate',
      'form_token' => 'invalid token'
    );
    $this->drupalPost(NULL, $edit, 'Save');
    $this->assertNoFieldByName('name', '#value changed by #validate', 'Form element #value was not altered.');
    $this->assertNoText('Name value: value changed by form_set_value() in #validate', 'Form element value in $form_state was not altered.');
    $this->assertText('The form has become outdated.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
