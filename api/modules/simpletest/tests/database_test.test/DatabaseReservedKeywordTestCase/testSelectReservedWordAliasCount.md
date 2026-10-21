# DatabaseReservedKeywordTestCase::testSelectReservedWordAliasCount()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 4565–4571 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L4565-L4571)
- **Class:** [DatabaseReservedKeywordTestCase](../DatabaseReservedKeywordTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testSelectReservedWordAliasCount()
```

## Documentation

_No docblock in source._

## Code

```php
  public function testSelectReservedWordAliasCount() {
    $rows = db_select('test', 'character')
      ->countQuery()
      ->execute()
      ->fetchField();
    $this->assertEqual($rows, 4, 'Successful count query using an alias which is a reserved word.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
