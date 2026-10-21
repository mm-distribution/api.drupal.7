# DatabaseSelectTestCase::testUnionOrderLimit()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 1753–1777 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L1753-L1777)
- **Class:** [DatabaseSelectTestCase](../DatabaseSelectTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testUnionOrderLimit()
```

## Documentation

```text
Tests that we can UNION multiple Select queries together with a LIMIT.
```

## Code

```php
  function testUnionOrderLimit() {
    // This gives George and Ringo.
    $query_1 = db_select('test', 't')
      ->fields('t', array('name'))
      ->condition('age', array(27, 28), 'IN');

    // This gives Paul.
    $query_2 = db_select('test', 't')
      ->fields('t', array('name'))
      ->condition('age', 26);

    $query_1->union($query_2);
    $query_1->orderBy('name', 'DESC');
    $query_1->range(0, 2);

    $names = $query_1->execute()->fetchCol();

    // Ensure we get only 2 of the 3 records.
    $this->assertEqual(count($names), 2, 'UNION with a limit returned rows from both queries.');

    // Ensure that the names are in the correct reverse alphabetical order,
    // regardless of which query they came from.
    $this->assertEqual($names[0], 'Ringo', 'First query returned correct name.');
    $this->assertEqual($names[1], 'Paul', 'Second query returned correct name.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
