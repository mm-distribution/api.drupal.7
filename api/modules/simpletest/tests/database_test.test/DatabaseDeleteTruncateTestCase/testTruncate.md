# DatabaseDeleteTruncateTestCase::testTruncate()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 1202–1209 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L1202-L1209)
- **Class:** [DatabaseDeleteTruncateTestCase](../DatabaseDeleteTruncateTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testTruncate()
```

## Documentation

```text
Confirm that we can truncate a whole table successfully.
```

## Code

```php
  function testTruncate() {
    $num_records_before = db_query("SELECT COUNT(*) FROM {test}")->fetchField();

    db_truncate('test')->execute();

    $num_records_after = db_query("SELECT COUNT(*) FROM {test}")->fetchField();
    $this->assertEqual(0, $num_records_after, 'Truncate really deletes everything.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
