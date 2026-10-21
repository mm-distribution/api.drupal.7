# ConnectionUnitTest::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 4298–4325 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L4298-L4325)
- **Class:** [ConnectionUnitTest](../ConnectionUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp();

    $this->key = 'default';
    $this->originalTarget = 'default';
    $this->target = 'DatabaseConnectionUnitTest';

    // Determine whether the database driver is MySQL. If it is not, the test
    // methods will not be executed.
    // @todo Make this test driver-agnostic, or find a proper way to skip it.
    // @see http://drupal.org/node/1273478
    $connection_info = Database::getConnectionInfo('default');
    $this->skipTest = (bool) ($connection_info['default']['driver'] != 'mysql');
    if ($this->skipTest) {
      // Insert an assertion to prevent Simpletest from interpreting the test
      // as failure.
      $this->pass('This test is only compatible with MySQL.');
    }

    // Create an additional connection to monitor the connections being opened
    // and closed in this test.
    // @see TestBase::changeDatabasePrefix()
    $connection_info = Database::getConnectionInfo('default');
    Database::addConnectionInfo('default', 'monitor', $connection_info['default']);
    global $databases;
    $databases['default']['monitor'] = $connection_info['default'];
    $this->monitor = Database::getConnection('monitor');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
