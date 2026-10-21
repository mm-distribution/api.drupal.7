# DatabaseSelectTestCase::testUnionAll()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 1700–1719 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L1700-L1719)
- **Class:** [DatabaseSelectTestCase](../DatabaseSelectTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testUnionAll()
```

## Documentation

```text
Test that we can UNION ALL multiple Select queries together.
```

## Code

```php
  function testUnionAll() {
    $query_1 = db_select('test', 't')
      ->fields('t', array('name'))
      ->condition('age', array(27, 28), 'IN');

    $query_2 = db_select('test', 't')
      ->fields('t', array('name'))
      ->condition('age', 28);

    $query_1->union($query_2, 'ALL');

    $names = $query_1->execute()->fetchCol();

    // Ensure we get all 3 records.
    $this->assertEqual(count($names), 3, 'UNION ALL correctly preserved duplicates.');

    $this->assertEqual($names[0], 'George', 'First query returned correct first name.');
    $this->assertEqual($names[1], 'Ringo', 'Second query returned correct second name.');
    $this->assertEqual($names[2], 'Ringo', 'Third query returned correct name.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
