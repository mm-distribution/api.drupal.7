# DatabaseSelectPagerDefaultTestCase::testEvenPagerQuery()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 2571–2597 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L2571-L2597)
- **Class:** [DatabaseSelectPagerDefaultTestCase](../DatabaseSelectPagerDefaultTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testEvenPagerQuery()
```

## Documentation

```text
Confirm that a pager query returns the correct results.

Note that we have to make an HTTP request to a test page handler
because the pager depends on GET parameters.
```

## Code

```php
  function testEvenPagerQuery() {
    // To keep the test from being too brittle, we determine up front
    // what the page count should be dynamically, and pass the control
    // information forward to the actual query on the other side of the
    // HTTP request.
    $limit = 2;
    $count = db_query('SELECT COUNT(*) FROM {test}')->fetchField();

    $correct_number = $limit;
    $num_pages = floor($count / $limit);

    // If there is no remainder from rounding, subtract 1 since we index from 0.
    if (!($num_pages * $limit < $count)) {
      $num_pages--;
    }

    for ($page = 0; $page <= $num_pages; ++$page) {
      $this->drupalGet('database_test/pager_query_even/' . $limit, array('query' => array('page' => $page)));
      $data = json_decode($this->drupalGetContent());

      if ($page == $num_pages) {
        $correct_number = $count - ($limit * $page);
      }

      $this->assertEqual(count($data->names), $correct_number, format_string('Correct number of records returned by pager: @number', array('@number' => $correct_number)));
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
