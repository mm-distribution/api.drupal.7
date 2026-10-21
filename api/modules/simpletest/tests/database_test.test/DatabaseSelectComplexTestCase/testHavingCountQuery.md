# DatabaseSelectComplexTestCase::testHavingCountQuery()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 2317–2326 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L2317-L2326)
- **Class:** [DatabaseSelectComplexTestCase](../DatabaseSelectComplexTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testHavingCountQuery()
```

## Documentation

_No docblock in source._

## Code

```php
  function testHavingCountQuery() {
    $query = db_select('test')
      ->extend('PagerDefault')
      ->groupBy('age')
      ->having('age + 1 > 0');
    $query->addField('test', 'age');
    $query->addExpression('age + 1');
    $count = count($query->execute()->fetchCol());
    $this->assertEqual($count, 4, 'Counted the correct number of records.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
