# ConnectionUnitTest::getConnectionID()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 4346–4348 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L4346-L4348)
- **Class:** [ConnectionUnitTest](../ConnectionUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
protected function getConnectionID()
```

## Documentation

```text
Returns the connection ID of the current test connection.

@return integer
```

## Code

```php
  protected function getConnectionID() {
    return (int) Database::getConnection($this->target, $this->key)->query('SELECT CONNECTION_ID()')->fetchField();
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
