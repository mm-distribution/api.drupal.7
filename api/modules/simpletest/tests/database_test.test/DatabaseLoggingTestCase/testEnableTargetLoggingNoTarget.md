# DatabaseLoggingTestCase::testEnableTargetLoggingNoTarget()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 3214–3231 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L3214-L3231)
- **Class:** [DatabaseLoggingTestCase](../DatabaseLoggingTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testEnableTargetLoggingNoTarget()
```

## Documentation

```text
Test that logs to separate targets collapse to the same connection properly.

This test is identical to the one above, except that it doesn't create
a fake target so the query should fall back to running on the default
target.
```

## Code

```php
  function testEnableTargetLoggingNoTarget() {
    Database::startLog('testing1');

    db_query('SELECT name FROM {test} WHERE age > :age', array(':age' => 25))->fetchCol();

    // We use "fake" here as a target because any non-existent target will do.
    // However, because all of the tests in this class share a single page
    // request there is likely to be a target of "slave" from one of the other
    // unit tests, so we use a target here that we know with absolute certainty
    // does not exist.
    db_query('SELECT age FROM {test} WHERE name = :name', array(':name' => 'Ringo'), array('target' => 'fake'))->fetchCol();

    $queries1 = Database::getLog('testing1');

    $this->assertEqual(count($queries1), 2, 'Recorded queries from all targets.');
    $this->assertEqual($queries1[0]['target'], 'default', 'First query used default target.');
    $this->assertEqual($queries1[1]['target'], 'default', 'Second query used default target as fallback.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
