# DatabaseLoggingTestCase::testEnableLogging()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 3148–3164 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L3148-L3164)
- **Class:** [DatabaseLoggingTestCase](../DatabaseLoggingTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testEnableLogging()
```

## Documentation

```text
Test that we can log the existence of a query.
```

## Code

```php
  function testEnableLogging() {
    $log = Database::startLog('testing');

    db_query('SELECT name FROM {test} WHERE age > :age', array(':age' => 25))->fetchCol();
    db_query('SELECT age FROM {test} WHERE name = :name', array(':name' => 'Ringo'))->fetchCol();

    // Trigger a call that does not have file in the backtrace.
    call_user_func_array('db_query', array('SELECT age FROM {test} WHERE name = :name', array(':name' => 'Ringo')))->fetchCol();

    $queries = Database::getLog('testing', 'default');

    $this->assertEqual(count($queries), 3, 'Correct number of queries recorded.');

    foreach ($queries as $query) {
      $this->assertEqual($query['caller']['function'], __FUNCTION__, 'Correct function in query log.');
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
