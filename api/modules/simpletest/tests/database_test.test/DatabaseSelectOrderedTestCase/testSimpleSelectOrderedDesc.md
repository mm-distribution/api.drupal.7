# DatabaseSelectOrderedTestCase::testSimpleSelectOrderedDesc()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 2101–2117 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L2101-L2117)
- **Class:** [DatabaseSelectOrderedTestCase](../DatabaseSelectOrderedTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testSimpleSelectOrderedDesc()
```

## Documentation

```text
Test order by descending.
```

## Code

```php
  function testSimpleSelectOrderedDesc() {
    $query = db_select('test');
    $name_field = $query->addField('test', 'name');
    $age_field = $query->addField('test', 'age', 'age');
    $query->orderBy($age_field, 'DESC');
    $result = $query->execute();

    $num_records = 0;
    $last_age = 100000000;
    foreach ($result as $record) {
      $num_records++;
      $this->assertTrue($record->age <= $last_age, 'Results returned in correct order.');
      $last_age = $record->age;
    }

    $this->assertEqual($num_records, 4, 'Returned the correct number of rows.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
