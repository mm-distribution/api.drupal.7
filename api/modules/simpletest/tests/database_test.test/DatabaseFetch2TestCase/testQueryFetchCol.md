# DatabaseFetch2TestCase::testQueryFetchCol()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 528–539 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L528-L539)
- **Class:** [DatabaseFetch2TestCase](../DatabaseFetch2TestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testQueryFetchCol()
```

## Documentation

```text
Confirm that we can fetch an entire column of a result set at once.
```

## Code

```php
  function testQueryFetchCol() {
    $records = array();
    $result = db_query('SELECT name FROM {test} WHERE age > :age', array(':age' => 25));
    $column = $result->fetchCol();
    $this->assertIdentical(count($column), 3, 'fetchCol() returns the right number of records.');

    $result = db_query('SELECT name FROM {test} WHERE age > :age', array(':age' => 25));
    $i = 0;
    foreach ($result as $record) {
      $this->assertIdentical($record->name, $column[$i++], 'Column matches direct accesss.');
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
