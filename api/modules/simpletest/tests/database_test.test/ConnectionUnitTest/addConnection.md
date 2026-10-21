# ConnectionUnitTest::addConnection()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 4330–4339 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L4330-L4339)
- **Class:** [ConnectionUnitTest](../ConnectionUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
protected function addConnection()
```

## Documentation

```text
Adds a new database connection info to Database.
```

## Code

```php
  protected function addConnection() {
    // Add a new target to the connection, by cloning the current connection.
    $connection_info = Database::getConnectionInfo($this->key);
    Database::addConnectionInfo($this->key, $this->target, $connection_info[$this->originalTarget]);

    // Verify that the new target exists.
    $info = Database::getConnectionInfo($this->key);
    // Note: Custom assertion message to not expose database credentials.
    $this->assertIdentical($info[$this->target], $connection_info[$this->key], 'New connection info found.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
