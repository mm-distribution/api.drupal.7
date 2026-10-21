# DatabaseRegressionTestCase::testDBIndexExists()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 3126–3129 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L3126-L3129)
- **Class:** [DatabaseRegressionTestCase](../DatabaseRegressionTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testDBIndexExists()
```

## Documentation

```text
Test the db_index_exists() function.
```

## Code

```php
  function testDBIndexExists() {
    $this->assertIdentical(TRUE, db_index_exists('node', 'node_created'), 'Returns true for existent index.');
    $this->assertIdentical(FALSE, db_index_exists('node', 'nosuchindex'), 'Returns false for nonexistent index.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
