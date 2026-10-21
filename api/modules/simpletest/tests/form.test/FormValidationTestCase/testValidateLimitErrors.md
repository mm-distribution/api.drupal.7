# FormValidationTestCase::testValidateLimitErrors()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 720–757 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L720-L757)
- **Class:** [FormValidationTestCase](../FormValidationTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testValidateLimitErrors()
```

## Documentation

```text
Tests partial form validation through #limit_validation_errors.
```

## Code

```php
  function testValidateLimitErrors() {
    $edit = array(
      'test' => 'invalid',
      'test_numeric_index[0]' => 'invalid',
      'test_substring[foo]' => 'invalid',
    );
    $path = 'form-test/limit-validation-errors';

    // Submit the form by pressing the 'Partial validate' button (uses
    // #limit_validation_errors) and ensure that the title field is not
    // validated, but the #element_validate handler for the 'test' field
    // is triggered.
    $this->drupalPost($path, $edit, t('Partial validate'));
    $this->assertNoText(t('!name field is required.', array('!name' => 'Title')));
    $this->assertText('Test element is invalid');

    // Edge case of #limit_validation_errors containing numeric indexes: same
    // thing with the 'Partial validate (numeric index)' button and the
    // 'test_numeric_index' field.
    $this->drupalPost($path, $edit, t('Partial validate (numeric index)'));
    $this->assertNoText(t('!name field is required.', array('!name' => 'Title')));
    $this->assertText('Test (numeric index) element is invalid');

    // Ensure something like 'foobar' isn't considered "inside" 'foo'.
    $this->drupalPost($path, $edit, t('Partial validate (substring)'));
    $this->assertNoText(t('!name field is required.', array('!name' => 'Title')));
    $this->assertText('Test (substring) foo element is invalid');

    // Ensure not validated values are not available to submit handlers.
    $this->drupalPost($path, array('title' => '', 'test' => 'valid'), t('Partial validate'));
    $this->assertText('Only validated values appear in the form values.');

    // Now test full form validation and ensure that the #element_validate
    // handler is still triggered.
    $this->drupalPost($path, $edit, t('Full validate'));
    $this->assertText(t('!name field is required.', array('!name' => 'Title')));
    $this->assertText('Test element is invalid');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
