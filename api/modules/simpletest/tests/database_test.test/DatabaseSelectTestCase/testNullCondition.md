# DatabaseSelectTestCase::testNullCondition()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 1643–1653 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L1643-L1653)
- **Class:** [DatabaseSelectTestCase](../DatabaseSelectTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testNullCondition()
```

## Documentation

```text
Test that we can find a record with a NULL value.
```

## Code

```php
  function testNullCondition() {
    $this->ensureSampleDataNull();

    $names = db_select('test_null', 'tn')
      ->fields('tn', array('name'))
      ->isNull('age')
      ->execute()->fetchCol();

    $this->assertEqual(count($names), 1, 'Correct number of records found with NULL age.');
    $this->assertEqual($names[0], 'Fozzie', 'Correct record returned for NULL age.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
