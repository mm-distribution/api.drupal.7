# ConnectionUnitTest::testOpenSelectQueryClose()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 4455–4494 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L4455-L4494)
- **Class:** [ConnectionUnitTest](../ConnectionUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testOpenSelectQueryClose()
```

## Documentation

```text
Tests Database::closeConnection() with a select query.
```

## Code

```php
  function testOpenSelectQueryClose() {
    if ($this->skipTest) {
      return;
    }
    // Add and open a new connection.
    $this->addConnection();
    $id = $this->getConnectionID();
    Database::getConnection($this->target, $this->key);

    // Verify that there is a new connection.
    $this->assertConnection($id);

    // Create a table.
    $name = 'foo';
    Database::getConnection($this->target, $this->key)->schema()->createTable($name, array(
      'fields' => array(
        'name' => array(
          'type' => 'varchar',
          'length' => 255,
        ),
      ),
    ));

    // Execute a query.
    Database::getConnection($this->target, $this->key)->select('foo', 'f')
      ->fields('f', array('name'))
      ->execute()
      ->fetchAll();

    // Drop the table.
    Database::getConnection($this->target, $this->key)->schema()->dropTable($name);

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
