# DatabaseTransactionTestCase::assertRowAbsent()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 4080–4086 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L4080-L4086)
- **Class:** [DatabaseTransactionTestCase](../DatabaseTransactionTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function assertRowAbsent($name, $message = NULL)
```

## Documentation

```text
Assert that a given row is absent from the test table.

@param $name
  The name of the row.
@param $message
  The message to log for the assertion.
```

## Code

```php
  function assertRowAbsent($name, $message = NULL) {
    if (!isset($message)) {
      $message = format_string('Row %name is absent.', array('%name' => $name));
    }
    $present = (boolean) db_query('SELECT 1 FROM {test} WHERE name = :name', array(':name' => $name))->fetchField();
    return $this->assertFalse($present, $message);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
