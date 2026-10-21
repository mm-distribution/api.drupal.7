# DatabaseTransactionTestCase::rollBackWithoutTransactionErrorHandler()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 4011–4017 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L4011-L4017)
- **Class:** [DatabaseTransactionTestCase](../DatabaseTransactionTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function rollBackWithoutTransactionErrorHandler($error_level, $message, $filename, $line)
```

## Documentation

```text
Special handling of "rollback without transaction" errors.
```

## Code

```php
  public function rollBackWithoutTransactionErrorHandler($error_level, $message, $filename, $line) {
    // Throw an exception if this is a "rollback without transaction" error.
    if (strpos($message, 'Rollback attempted when there is no active transaction.') !== FALSE ) {
      throw new Exception('Rollback attempted when there is no active transaction.');
    }
    _drupal_error_handler($error_level, $message, $filename, $line);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
