# DatabaseConnectionTestCase::testConnectionClosing()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 255–265 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L255-L265)
- **Class:** [DatabaseConnectionTestCase](../DatabaseConnectionTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testConnectionClosing()
```

## Documentation

```text
Tests the closing of a database connection.
```

## Code

```php
  function testConnectionClosing() {
    // Open the default target so we have an object to compare.
    $db1 = Database::getConnection('default', 'default');

    // Try to close the default connection, then open a new one.
    Database::closeConnection('default', 'default');
    $db2 = Database::getConnection('default', 'default');

    // Opening a connection after closing it should yield an object different than the original.
    $this->assertNotIdentical($db1, $db2, 'Opening the default connection after it is closed returns a new object.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
