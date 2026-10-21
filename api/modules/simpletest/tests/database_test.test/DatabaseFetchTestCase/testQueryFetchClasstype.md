# DatabaseFetchTestCase::testQueryFetchClasstype()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 459–472 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L459-L472)
- **Class:** [DatabaseFetchTestCase](../DatabaseFetchTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testQueryFetchClasstype()
```

## Documentation

```text
Confirms that we can fetch a record into a new instance of a custom class.
The name of the class is determined from a value of the first column.

@see FakeRecord
```

## Code

```php
  function testQueryFetchClasstype() {
    $records = array();
    $result = db_query('SELECT classname, name, job FROM {test_classtype} WHERE age = :age', array(':age' => 26), array('fetch' => PDO::FETCH_CLASS | PDO::FETCH_CLASSTYPE));
    foreach ($result as $record) {
      $records[] = $record;
      if ($this->assertTrue($record instanceof FakeRecord, 'Record is an object of class FakeRecord.')) {
        $this->assertIdentical($record->name, 'Kay', 'Kay is found.');
        $this->assertIdentical($record->job, 'Web Developer', 'A 26 year old Web Developer.');
      }
      $this->assertFalse(isset($record->classname), 'Classname field not found, as intended.');
    }

    $this->assertIdentical(count($records), 1, 'There is only one record.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
