# ConnectionUnitTest::assertNoConnection()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 4367–4370 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L4367-L4370)
- **Class:** [ConnectionUnitTest](../ConnectionUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
protected function assertNoConnection($id)
```

## Documentation

```text
Asserts that a connection ID does not exist.

@param integer $id
  The connection ID to verify.
```

## Code

```php
  protected function assertNoConnection($id) {
    $list = $this->monitor->query('SHOW PROCESSLIST')->fetchAllKeyed(0, 0);
    return $this->assertFalse(isset($list[$id]), format_string('Connection ID @id not found.', array('@id' => $id)));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
