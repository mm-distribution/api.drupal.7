# DatabaseRegressionTestCase::testDBFieldExists()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 3118–3121 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L3118-L3121)
- **Class:** [DatabaseRegressionTestCase](../DatabaseRegressionTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testDBFieldExists()
```

## Documentation

```text
Test the db_field_exists() function.
```

## Code

```php
  function testDBFieldExists() {
    $this->assertIdentical(TRUE, db_field_exists('node', 'nid'), 'Returns true for existent column.');
    $this->assertIdentical(FALSE, db_field_exists('node', 'nosuchcolumn'), 'Returns false for nonexistent column.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
