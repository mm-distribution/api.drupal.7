# DatabaseSelectTableSortDefaultTestCase::testTableSortQuery()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 2729–2749 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L2729-L2749)
- **Class:** [DatabaseSelectTableSortDefaultTestCase](../DatabaseSelectTableSortDefaultTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testTableSortQuery()
```

## Documentation

```text
Confirm that a tablesort query returns the correct results.

Note that we have to make an HTTP request to a test page handler
because the pager depends on GET parameters.
```

## Code

```php
  function testTableSortQuery() {
    $sorts = array(
      array('field' => t('Task ID'), 'sort' => 'desc', 'first' => 'perform at superbowl', 'last' => 'eat'),
      array('field' => t('Task ID'), 'sort' => 'asc', 'first' => 'eat', 'last' => 'perform at superbowl'),
      array('field' => t('Task'), 'sort' => 'asc', 'first' => 'code', 'last' => 'sleep'),
      array('field' => t('Task'), 'sort' => 'desc', 'first' => 'sleep', 'last' => 'code'),
      // more elements here

    );

    foreach ($sorts as $sort) {
      $this->drupalGet('database_test/tablesort/', array('query' => array('order' => $sort['field'], 'sort' => $sort['sort'])));
      $data = json_decode($this->drupalGetContent());

      $first = array_shift($data->tasks);
      $last = array_pop($data->tasks);

      $this->assertEqual($first->task, $sort['first'], 'Items appear in the correct order.');
      $this->assertEqual($last->task, $sort['last'], 'Items appear in the correct order.');
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
