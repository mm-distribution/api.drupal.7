# DatabaseFetchTestCase::testQueryFetchDefault()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 391–402 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L391-L402)
- **Class:** [DatabaseFetchTestCase](../DatabaseFetchTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testQueryFetchDefault()
```

## Documentation

```text
Confirm that we can fetch a record properly in default object mode.
```

## Code

```php
  function testQueryFetchDefault() {
    $records = array();
    $result = db_query('SELECT name FROM {test} WHERE age = :age', array(':age' => 25));
    $this->assertTrue($result instanceof DatabaseStatementInterface, 'Result set is a Drupal statement object.');
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
