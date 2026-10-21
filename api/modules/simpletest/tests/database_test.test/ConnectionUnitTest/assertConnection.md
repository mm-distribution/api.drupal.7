# ConnectionUnitTest::assertConnection()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 4356–4359 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L4356-L4359)
- **Class:** [ConnectionUnitTest](../ConnectionUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
protected function assertConnection($id)
```

## Documentation

```text
Asserts that a connection ID exists.

@param integer $id
  The connection ID to verify.
```

## Code

```php
  protected function assertConnection($id) {
    $list = $this->monitor->query('SHOW PROCESSLIST')->fetchAllKeyed(0, 0);
    return $this->assertTrue(isset($list[$id]), format_string('Connection ID @id found.', array('@id' => $id)));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
