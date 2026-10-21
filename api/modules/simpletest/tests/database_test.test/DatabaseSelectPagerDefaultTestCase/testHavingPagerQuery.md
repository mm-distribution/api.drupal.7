# DatabaseSelectPagerDefaultTestCase::testHavingPagerQuery()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 2659–2672 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L2659-L2672)
- **Class:** [DatabaseSelectPagerDefaultTestCase](../DatabaseSelectPagerDefaultTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testHavingPagerQuery()
```

## Documentation

```text
Confirm that a paging query with a having expression returns valid results.

This is a regression test for #467984.
```

## Code

```php
  function testHavingPagerQuery() {
    $query = db_select('test', 't')->extend('PagerDefault');
    $query
      ->fields('t', array('name'))
      ->orderBy('name')
      ->groupBy('name')
      ->having('MAX(age) > :count', array(':count' => 26))
      ->limit(5);

    $ages = $query
      ->execute()
      ->fetchCol();
    $this->assertEqual($ages, array('George', 'Ringo'), 'Pager query with having expression returned the correct ages.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
