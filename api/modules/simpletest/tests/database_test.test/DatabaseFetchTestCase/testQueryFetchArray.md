# DatabaseFetchTestCase::testQueryFetchArray()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 422–433 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L422-L433)
- **Class:** [DatabaseFetchTestCase](../DatabaseFetchTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testQueryFetchArray()
```

## Documentation

```text
Confirm that we can fetch a record to an array associative explicitly.
```

## Code

```php
  function testQueryFetchArray() {
    $records = array();
    $result = db_query('SELECT name FROM {test} WHERE age = :age', array(':age' => 25), array('fetch' => PDO::FETCH_ASSOC));
    foreach ($result as $record) {
      $records[] = $record;
      if ($this->assertTrue(is_array($record), 'Record is an array.')) {
        $this->assertIdentical($record['name'], 'John', 'Record can be accessed associatively.');
      }
    }

    $this->assertIdentical(count($records), 1, 'There is only one record.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
