# DatabaseLoggingTestCase::testEnableMultiConnectionLogging()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 3236–3258 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L3236-L3258)
- **Class:** [DatabaseLoggingTestCase](../DatabaseLoggingTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testEnableMultiConnectionLogging()
```

## Documentation

```text
Test that we can log queries separately on different connections.
```

## Code

```php
  function testEnableMultiConnectionLogging() {
    // Clone the master credentials to a fake connection.
    // That both connections point to the same physical database is irrelevant.
    $connection_info = Database::getConnectionInfo('default');
    Database::addConnectionInfo('test2', 'default', $connection_info['default']);

    Database::startLog('testing1');
    Database::startLog('testing1', 'test2');

    db_query('SELECT name FROM {test} WHERE age > :age', array(':age' => 25))->fetchCol();

    $old_key = db_set_active('test2');

    db_query('SELECT age FROM {test} WHERE name = :name', array(':name' => 'Ringo'), array('target' => 'slave'))->fetchCol();

    db_set_active($old_key);

    $queries1 = Database::getLog('testing1');
    $queries2 = Database::getLog('testing1', 'test2');

    $this->assertEqual(count($queries1), 1, 'Correct number of queries recorded for first connection.');
    $this->assertEqual(count($queries2), 1, 'Correct number of queries recorded for second connection.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
