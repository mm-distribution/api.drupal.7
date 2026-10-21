# DatabaseSelectComplexTestCase::testCountQuery()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 2300–2315 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L2300-L2315)
- **Class:** [DatabaseSelectComplexTestCase](../DatabaseSelectComplexTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testCountQuery()
```

## Documentation

```text
Test that we can generate a count query from a built query.
```

## Code

```php
  function testCountQuery() {
    $query = db_select('test');
    $name_field = $query->addField('test', 'name');
    $age_field = $query->addField('test', 'age', 'age');
    $query->orderBy('name');

    $count = $query->countQuery()->execute()->fetchField();

    $this->assertEqual($count, 4, 'Counted the correct number of records.');

    // Now make sure we didn't break the original query!  We should still have
    // all of the fields we asked for.
    $record = $query->execute()->fetch();
    $this->assertEqual($record->$name_field, 'George', 'Correct data retrieved.');
    $this->assertEqual($record->$age_field, 27, 'Correct data retrieved.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
