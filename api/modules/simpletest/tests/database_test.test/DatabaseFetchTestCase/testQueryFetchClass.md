# DatabaseFetchTestCase::testQueryFetchClass()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 440–451 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L440-L451)
- **Class:** [DatabaseFetchTestCase](../DatabaseFetchTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testQueryFetchClass()
```

## Documentation

```text
Confirm that we can fetch a record into a new instance of a custom class.

@see FakeRecord
```

## Code

```php
  function testQueryFetchClass() {
    $records = array();
    $result = db_query('SELECT name FROM {test} WHERE age = :age', array(':age' => 25), array('fetch' => 'FakeRecord'));
    foreach ($result as $record) {
      $records[] = $record;
      if ($this->assertTrue($record instanceof FakeRecord, 'Record is an object of class FakeRecord.')) {
        $this->assertIdentical($record->name, 'John', '25 year old is John.');
      }
    }

    $this->assertIdentical(count($records), 1, 'There is only one record.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
