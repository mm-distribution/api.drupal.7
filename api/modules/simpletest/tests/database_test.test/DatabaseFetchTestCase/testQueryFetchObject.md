# DatabaseFetchTestCase::testQueryFetchObject()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 407–417 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L407-L417)
- **Class:** [DatabaseFetchTestCase](../DatabaseFetchTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testQueryFetchObject()
```

## Documentation

```text
Confirm that we can fetch a record to an object explicitly.
```

## Code

```php
  function testQueryFetchObject() {
    $records = array();
    $result = db_query('SELECT name FROM {test} WHERE age = :age', array(':age' => 25), array('fetch' => PDO::FETCH_OBJ));
    foreach ($result as $record) {
      $records[] = $record;
      $this->assertTrue(is_object($record), 'Record is an object.');
      $this->assertIdentical($record->name, 'John', '25 year old is John.');
    }

    $this->assertIdentical(count($records), 1, 'There is only one record.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
