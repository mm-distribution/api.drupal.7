# DrupalErrorHandlerTestCase::testExceptionHandler()

- **Type:** Method
- **File:** [`modules/simpletest/tests/error.test`](../_file.md), lines 70–98 · [local source](../../../../../../source/modules/simpletest/tests/error.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/error.test#L70-L98)
- **Class:** [DrupalErrorHandlerTestCase](../DrupalErrorHandlerTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testExceptionHandler()
```

## Documentation

```text
Test the exception handler.
```

## Code

```php
  function testExceptionHandler() {
    $error_exception = array(
      '%type' => 'Exception',
      '!message' => 'Drupal is awesome',
      '%function' => 'error_test_trigger_exception()',
      '%line' => 57,
      '%file' => drupal_realpath('modules/simpletest/tests/error_test.module'),
    );
    $error_pdo_exception = array(
      '%type' => 'PDOException',
      '!message' => 'SELECT * FROM bananas_are_awesome',
      '%function' => 'error_test_trigger_pdo_exception()',
      '%line' => 65,
      '%file' => drupal_realpath('modules/simpletest/tests/error_test.module'),
    );

    $this->drupalGet('error-test/trigger-exception');
    $this->assertTrue(strpos($this->drupalGetHeader(':status'), '500 Service unavailable (with message)'), 'Received expected HTTP status line.');
    $this->assertErrorMessage($error_exception);

    $this->drupalGet('error-test/trigger-pdo-exception');
    $this->assertTrue(strpos($this->drupalGetHeader(':status'), '500 Service unavailable (with message)'), 'Received expected HTTP status line.');
    // We cannot use assertErrorMessage() since the extact error reported
    // varies from database to database. Check that the SQL string is displayed.
    $this->assertText($error_pdo_exception['%type'], format_string('Found %type in error page.', $error_pdo_exception));
    $this->assertText($error_pdo_exception['!message'], format_string('Found !message in error page.', $error_pdo_exception));
    $error_details = format_string('in %function (line ', $error_pdo_exception);
    $this->assertRaw($error_details, format_string("Found '!message' in error page.", array('!message' => $error_details)));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/error.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/error.test) · Licensed GPL-2.0-or-later (see LICENSE)._
