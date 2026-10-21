# DrupalErrorHandlerTestCase::assertErrorMessage()

- **Type:** Method
- **File:** [`modules/simpletest/tests/error.test`](../_file.md), lines 103–115 · [local source](../../../../../../source/modules/simpletest/tests/error.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/error.test#L103-L115)
- **Class:** [DrupalErrorHandlerTestCase](../DrupalErrorHandlerTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function assertErrorMessage(array $error)
```

## Documentation

```text
Helper function: assert that the error message is found.
```

## Code

```php
  function assertErrorMessage(array $error) {
    $message = t('%type: !message in %function (line ', $error);
    $this->assertRaw($message, format_string('Found error message: !message.', array('!message' => $message)));

    // Also check that no full path from the error is displayed.
    $this->assertNoRaw($error['%file'], format_string('Full path from error not displayed: %file.', array('%file' => $error['%file'])));

    // Check that the path was displayed with the DRUPAL_ROOT hidden.
    $root_length = strlen(DRUPAL_ROOT);
    $stripped_path = substr($error['%file'], $root_length + 1);
    $sanitized_path = t('of %path)', array('%path' => $stripped_path));
    $this->assertRaw($sanitized_path, 'Path in error message was sanitized.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/error.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/error.test) · Licensed GPL-2.0-or-later (see LICENSE)._
