# DatabaseSelectTableSortDefaultTestCase::testTableSortQueryFirst()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 2755–2775 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L2755-L2775)
- **Class:** [DatabaseSelectTableSortDefaultTestCase](../DatabaseSelectTableSortDefaultTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testTableSortQueryFirst()
```

## Documentation

```text
Confirm that if a tablesort's orderByHeader is called before another orderBy, that the header happens first.
```

## Code

```php
  function testTableSortQueryFirst() {
    $sorts = array(
      array('field' => t('Task ID'), 'sort' => 'desc', 'first' => 'perform at superbowl', 'last' => 'eat'),
      array('field' => t('Task ID'), 'sort' => 'asc', 'first' => 'eat', 'last' => 'perform at superbowl'),
      array('field' => t('Task'), 'sort' => 'asc', 'first' => 'code', 'last' => 'sleep'),
      array('field' => t('Task'), 'sort' => 'desc', 'first' => 'sleep', 'last' => 'code'),
      // more elements here

    );

    foreach ($sorts as $sort) {
      $this->drupalGet('database_test/tablesort_first/', array('query' => array('order' => $sort['field'], 'sort' => $sort['sort'])));
      $data = json_decode($this->drupalGetContent());

      $first = array_shift($data->tasks);
      $last = array_pop($data->tasks);

      $this->assertEqual($first->task, $sort['first'], format_string('Items appear in the correct order sorting by @field @sort.', array('@field' => $sort['field'], '@sort' => $sort['sort'])));
      $this->assertEqual($last->task, $sort['last'], format_string('Items appear in the correct order sorting by @field @sort.', array('@field' => $sort['field'], '@sort' => $sort['sort'])));
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
