# DrupalErrorHandlerTestCase::assertNoErrorMessage()

- **Type:** Method
- **File:** [`modules/simpletest/tests/error.test`](../_file.md), lines 120–126 · [local source](../../../../../../source/modules/simpletest/tests/error.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/error.test#L120-L126)
- **Class:** [DrupalErrorHandlerTestCase](../DrupalErrorHandlerTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function assertNoErrorMessage(array $error)
```

## Documentation

```text
Helper function: assert that the error message is not found.
```

## Code

```php
  function assertNoErrorMessage(array $error) {
    $message = t('%type: !message in %function (line ', $error);
    $this->assertNoRaw($message, format_string('Did not find error message: !message.', array('!message' => $message)));

    // Also check that no full path from the error is displayed.
    $this->assertNoRaw($error['%file'], format_string('Full path from error not displayed: %file.', array('%file' => $error['%file'])));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/error.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/error.test) · Licensed GPL-2.0-or-later (see LICENSE)._
