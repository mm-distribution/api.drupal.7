# BootstrapGetFilenameTestCase::fileNotFoundErrorHandler()

- **Type:** Method
- **File:** [`modules/simpletest/tests/bootstrap.test`](../_file.md), lines 488–495 · [local source](../../../../../../source/modules/simpletest/tests/bootstrap.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test#L488-L495)
- **Class:** [BootstrapGetFilenameTestCase](../BootstrapGetFilenameTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function fileNotFoundErrorHandler($error_level, $message, $filename, $line)
```

## Documentation

```text
Skips handling of "file not found" errors.
```

## Code

```php
  public function fileNotFoundErrorHandler($error_level, $message, $filename, $line) {
    // Skip error handling if this is a "file not found" error.
    if (strpos($message, 'is missing from the file system:') !== FALSE || strpos($message, 'has moved within the file system:') !== FALSE) {
      $this->getFilenameTestTriggeredError = $message;
      return;
    }
    _drupal_error_handler($error_level, $message, $filename, $line);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/bootstrap.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test) · Licensed GPL-2.0-or-later (see LICENSE)._
