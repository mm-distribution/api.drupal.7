# DatabaseSelectOrderedTestCase::testSimpleSelectOrdered()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 2049–2065 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L2049-L2065)
- **Class:** [DatabaseSelectOrderedTestCase](../DatabaseSelectOrderedTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testSimpleSelectOrdered()
```

## Documentation

```text
Test basic order by.
```

## Code

```php
  function testSimpleSelectOrdered() {
    $query = db_select('test');
    $name_field = $query->addField('test', 'name');
    $age_field = $query->addField('test', 'age', 'age');
    $query->orderBy($age_field);
    $result = $query->execute();

    $num_records = 0;
    $last_age = 0;
    foreach ($result as $record) {
      $num_records++;
      $this->assertTrue($record->age >= $last_age, 'Results returned in correct order.');
      $last_age = $record->age;
    }

    $this->assertEqual($num_records, 4, 'Returned the correct number of rows.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
