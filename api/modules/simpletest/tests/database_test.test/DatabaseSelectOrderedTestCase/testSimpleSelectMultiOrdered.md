# DatabaseSelectOrderedTestCase::testSimpleSelectMultiOrdered()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 2070–2096 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L2070-L2096)
- **Class:** [DatabaseSelectOrderedTestCase](../DatabaseSelectOrderedTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testSimpleSelectMultiOrdered()
```

## Documentation

```text
Test multiple order by.
```

## Code

```php
  function testSimpleSelectMultiOrdered() {
    $query = db_select('test');
    $name_field = $query->addField('test', 'name');
    $age_field = $query->addField('test', 'age', 'age');
    $job_field = $query->addField('test', 'job');
    $query->orderBy($job_field);
    $query->orderBy($age_field);
    $result = $query->execute();

    $num_records = 0;
    $expected = array(
      array('Ringo', 28, 'Drummer'),
      array('John', 25, 'Singer'),
      array('George', 27, 'Singer'),
      array('Paul', 26, 'Songwriter'),
    );
    $results = $result->fetchAll(PDO::FETCH_NUM);
    foreach ($expected as $k => $record) {
      $num_records++;
      foreach ($record as $kk => $col) {
        if ($expected[$k][$kk] != $results[$k][$kk]) {
          $this->assertTrue(FALSE, 'Results returned in correct order.');
        }
      }
    }
    $this->assertEqual($num_records, 4, 'Returned the correct number of rows.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
