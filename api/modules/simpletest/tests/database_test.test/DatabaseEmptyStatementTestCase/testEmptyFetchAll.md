# DatabaseEmptyStatementTestCase::testEmptyFetchAll()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 4269–4273 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L4269-L4273)
- **Class:** [DatabaseEmptyStatementTestCase](../DatabaseEmptyStatementTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testEmptyFetchAll()
```

## Documentation

```text
Test that the empty result set mass-fetches in an expected way.
```

## Code

```php
  function testEmptyFetchAll() {
    $result = new DatabaseStatementEmpty();

    $this->assertEqual($result->fetchAll(), array(), 'Empty array returned from empty result set.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
