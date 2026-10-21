# DrupalErrorHandlerTestCase::testErrorHandler()

- **Type:** Method
- **File:** [`modules/simpletest/tests/error.test`](../_file.md), lines 22–65 · [local source](../../../../../../source/modules/simpletest/tests/error.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/error.test#L22-L65)
- **Class:** [DrupalErrorHandlerTestCase](../DrupalErrorHandlerTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testErrorHandler()
```

## Documentation

```text
Test the error handler.
```

## Code

```php
  function testErrorHandler() {
    $error_notice = array(
      '%type' => 'Notice',
      '!message' => 'Object of class stdClass could not be converted to int',
      '%function' => 'error_test_generate_warnings()',
      '%file' => drupal_realpath('modules/simpletest/tests/error_test.module'),
    );
    $error_warning = array(
      '%type' => 'Warning',
      '!message' => \PHP_VERSION_ID < 80000 ? 'Invalid argument supplied for foreach()' : 'foreach() argument must be of type array|object, string given',
      '%function' => 'error_test_generate_warnings()',
      '%file' => drupal_realpath('modules/simpletest/tests/error_test.module'),
    );
    $error_user_notice = array(
      '%type' => 'User warning',
      '!message' => 'Drupal is awesome',
      '%function' => 'error_test_generate_warnings()',
      '%file' => drupal_realpath('modules/simpletest/tests/error_test.module'),
    );

    // Set error reporting to collect notices.
    variable_set('error_level', ERROR_REPORTING_DISPLAY_ALL);
    $this->drupalGet('error-test/generate-warnings');
    $this->assertResponse(200, 'Received expected HTTP status code.');
    $this->assertErrorMessage($error_notice);
    $this->assertErrorMessage($error_warning);
    $this->assertErrorMessage($error_user_notice);

    // Set error reporting to not collect notices.
    variable_set('error_level', ERROR_REPORTING_DISPLAY_SOME);
    $this->drupalGet('error-test/generate-warnings');
    $this->assertResponse(200, 'Received expected HTTP status code.');
    $this->assertNoErrorMessage($error_notice);
    $this->assertErrorMessage($error_warning);
    $this->assertErrorMessage($error_user_notice);

    // Set error reporting to not show any errors.
    variable_set('error_level', ERROR_REPORTING_HIDE);
    $this->drupalGet('error-test/generate-warnings');
    $this->assertResponse(200, 'Received expected HTTP status code.');
    $this->assertNoErrorMessage($error_notice);
    $this->assertNoErrorMessage($error_warning);
    $this->assertNoErrorMessage($error_user_notice);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/error.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/error.test) · Licensed GPL-2.0-or-later (see LICENSE)._
