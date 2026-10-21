# DatabaseSelectPagerDefaultTestCase::testInnerPagerQuery()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 2638–2652 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L2638-L2652)
- **Class:** [DatabaseSelectPagerDefaultTestCase](../DatabaseSelectPagerDefaultTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testInnerPagerQuery()
```

## Documentation

```text
Confirm that a pager query with inner pager query returns valid results.

This is a regression test for #467984.
```

## Code

```php
  function testInnerPagerQuery() {
    $query = db_select('test', 't')->extend('PagerDefault');
    $query
      ->fields('t', array('age'))
      ->orderBy('age')
      ->limit(5);

    $outer_query = db_select($query);
    $outer_query->addField('subquery', 'age');

    $ages = $outer_query
      ->execute()
      ->fetchCol();
    $this->assertEqual($ages, array(25, 26, 27, 28), 'Inner pager query returned the correct ages.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
