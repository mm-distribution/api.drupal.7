# DatabaseRegressionTestCase::testDBTableExists()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 3110–3113 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L3110-L3113)
- **Class:** [DatabaseRegressionTestCase](../DatabaseRegressionTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testDBTableExists()
```

## Documentation

```text
Test the db_table_exists() function.
```

## Code

```php
  function testDBTableExists() {
    $this->assertIdentical(TRUE, db_table_exists('node'), 'Returns true for existent table.');
    $this->assertIdentical(FALSE, db_table_exists('nosuchtable'), 'Returns false for nonexistent table.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
