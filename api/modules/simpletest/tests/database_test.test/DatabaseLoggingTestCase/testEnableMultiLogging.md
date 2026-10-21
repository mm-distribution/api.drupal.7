# DatabaseLoggingTestCase::testEnableMultiLogging()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 3169–3183 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L3169-L3183)
- **Class:** [DatabaseLoggingTestCase](../DatabaseLoggingTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testEnableMultiLogging()
```

## Documentation

```text
Test that we can run two logs in parallel.
```

## Code

```php
  function testEnableMultiLogging() {
    Database::startLog('testing1');

    db_query('SELECT name FROM {test} WHERE age > :age', array(':age' => 25))->fetchCol();

    Database::startLog('testing2');

    db_query('SELECT age FROM {test} WHERE name = :name', array(':name' => 'Ringo'))->fetchCol();

    $queries1 = Database::getLog('testing1');
    $queries2 = Database::getLog('testing2');

    $this->assertEqual(count($queries1), 2, 'Correct number of queries recorded for log 1.');
    $this->assertEqual(count($queries2), 1, 'Correct number of queries recorded for log 2.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
