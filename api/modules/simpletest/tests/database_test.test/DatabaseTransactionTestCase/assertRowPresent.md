# DatabaseTransactionTestCase::assertRowPresent()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 4064–4070 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L4064-L4070)
- **Class:** [DatabaseTransactionTestCase](../DatabaseTransactionTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function assertRowPresent($name, $message = NULL)
```

## Documentation

```text
Assert that a given row is present in the test table.

@param $name
  The name of the row.
@param $message
  The message to log for the assertion.
```

## Code

```php
  function assertRowPresent($name, $message = NULL) {
    if (!isset($message)) {
      $message = format_string('Row %name is present.', array('%name' => $name));
    }
    $present = (boolean) db_query('SELECT 1 FROM {test} WHERE name = :name', array(':name' => $name))->fetchField();
    return $this->assertTrue($present, $message);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
