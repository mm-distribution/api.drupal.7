# FormValidationTestCase::testDisabledToken()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 712–715 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L712-L715)
- **Class:** [FormValidationTestCase](../FormValidationTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testDisabledToken()
```

## Documentation

```text
Tests that a form with a disabled CSRF token can be validated.
```

## Code

```php
  function testDisabledToken() {
    $this->drupalPost('form-test/validate-no-token', array(), 'Save');
    $this->assertText('The form_test_validate_no_token form has been submitted successfully.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
