# DatabaseSelectComplexTestCase::testCountQueryFieldRemovals()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 2360–2373 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L2360-L2373)
- **Class:** [DatabaseSelectComplexTestCase](../DatabaseSelectComplexTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testCountQueryFieldRemovals()
```

## Documentation

```text
Test that countQuery properly removes fields and expressions.
```

## Code

```php
  function testCountQueryFieldRemovals() {
    // countQuery should remove all fields and expressions, so this can be
    // tested by adding a non-existent field and expression: if it ends
    // up in the query, an error will be thrown. If not, it will return the
    // number of records, which in this case happens to be 4 (there are four
    // records in the {test} table).
    $query = db_select('test');
    $query->fields('test', array('fail'));
    $this->assertEqual(4, $query->countQuery()->execute()->fetchField(), 'Count Query removed fields');

    $query = db_select('test');
    $query->addExpression('fail');
    $this->assertEqual(4, $query->countQuery()->execute()->fetchField(), 'Count Query removed expressions');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
