# DatabaseLoggingTestCase::testEnableTargetLogging()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 3188–3205 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L3188-L3205)
- **Class:** [DatabaseLoggingTestCase](../DatabaseLoggingTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testEnableTargetLogging()
```

## Documentation

```text
Test that we can log queries against multiple targets on the same connection.
```

## Code

```php
  function testEnableTargetLogging() {
    // Clone the master credentials to a slave connection and to another fake
    // connection.
    $connection_info = Database::getConnectionInfo('default');
    Database::addConnectionInfo('default', 'slave', $connection_info['default']);

    Database::startLog('testing1');

    db_query('SELECT name FROM {test} WHERE age > :age', array(':age' => 25))->fetchCol();

    db_query('SELECT age FROM {test} WHERE name = :name', array(':name' => 'Ringo'), array('target' => 'slave'));//->fetchCol();

    $queries1 = Database::getLog('testing1');

    $this->assertEqual(count($queries1), 2, 'Recorded queries from all targets.');
    $this->assertEqual($queries1[0]['target'], 'default', 'First query used default target.');
    $this->assertEqual($queries1[1]['target'], 'slave', 'Second query used slave target.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
