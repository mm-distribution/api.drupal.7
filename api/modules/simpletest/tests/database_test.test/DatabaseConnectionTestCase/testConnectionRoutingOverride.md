# DatabaseConnectionTestCase::testConnectionRoutingOverride()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 237–250 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L237-L250)
- **Class:** [DatabaseConnectionTestCase](../DatabaseConnectionTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testConnectionRoutingOverride()
```

## Documentation

```text
Test that connections return appropriate connection objects.
```

## Code

```php
  function testConnectionRoutingOverride() {
    // Clone the master credentials to a slave connection.
    // Note this will result in two independent connection objects that happen
    // to point to the same place.
    $connection_info = Database::getConnectionInfo('default');
    Database::addConnectionInfo('default', 'slave', $connection_info['default']);

    Database::ignoreTarget('default', 'slave');

    $db1 = Database::getConnection('default', 'default');
    $db2 = Database::getConnection('slave', 'default');

    $this->assertIdentical($db1, $db2, 'Both targets refer to the same connection.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
