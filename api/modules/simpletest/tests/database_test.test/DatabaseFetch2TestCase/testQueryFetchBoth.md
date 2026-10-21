# DatabaseFetch2TestCase::testQueryFetchBoth()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 511–523 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L511-L523)
- **Class:** [DatabaseFetch2TestCase](../DatabaseFetch2TestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testQueryFetchBoth()
```

## Documentation

```text
Confirm that we can fetch a record into a doubly-keyed array explicitly.
```

## Code

```php
  function testQueryFetchBoth() {
    $records = array();
    $result = db_query('SELECT name FROM {test} WHERE age = :age', array(':age' => 25), array('fetch' => PDO::FETCH_BOTH));
    foreach ($result as $record) {
      $records[] = $record;
      if ($this->assertTrue(is_array($record), 'Record is an array.')) {
        $this->assertIdentical($record[0], 'John', 'Record can be accessed numerically.');
        $this->assertIdentical($record['name'], 'John', 'Record can be accessed associatively.');
      }
    }

    $this->assertIdentical(count($records), 1, 'There is only one record.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
