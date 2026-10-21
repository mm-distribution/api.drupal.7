# ConnectionUnitTest::testOpenClose()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 4377–4396 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L4377-L4396)
- **Class:** [ConnectionUnitTest](../ConnectionUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testOpenClose()
```

## Documentation

```text
Tests Database::closeConnection() without query.

@todo getConnectionID() executes a query.
```

## Code

```php
  function testOpenClose() {
    if ($this->skipTest) {
      return;
    }
    // Add and open a new connection.
    $this->addConnection();
    $id = $this->getConnectionID();
    Database::getConnection($this->target, $this->key);

    // Verify that there is a new connection.
    $this->assertConnection($id);

    // Close the connection.
    Database::closeConnection($this->target, $this->key);
    // Wait 20ms to give the database engine sufficient time to react.
    usleep(20000);

    // Verify that we are back to the original connection count.
    $this->assertNoConnection($id);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
