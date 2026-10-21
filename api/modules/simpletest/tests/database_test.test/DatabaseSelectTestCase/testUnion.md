# DatabaseSelectTestCase::testUnion()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 1676–1695 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L1676-L1695)
- **Class:** [DatabaseSelectTestCase](../DatabaseSelectTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testUnion()
```

## Documentation

```text
Test that we can UNION multiple Select queries together. This is
semantically equal to UNION DISTINCT, so we don't explicitly test that.
```

## Code

```php
  function testUnion() {
    $query_1 = db_select('test', 't')
      ->fields('t', array('name'))
      ->condition('age', array(27, 28), 'IN');

    $query_2 = db_select('test', 't')
      ->fields('t', array('name'))
      ->condition('age', 28)
      ->orderBy('name');

    $query_1->union($query_2);

    $names = $query_1->execute()->fetchCol();

    // Ensure we only get 2 records.
    $this->assertEqual(count($names), 2, 'UNION correctly discarded duplicates.');

    $this->assertEqual($names[0], 'George', 'First query returned correct name.');
    $this->assertEqual($names[1], 'Ringo', 'Second query returned correct name.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
