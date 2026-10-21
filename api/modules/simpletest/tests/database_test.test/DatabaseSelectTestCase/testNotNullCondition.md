# DatabaseSelectTestCase::testNotNullCondition()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 1658–1670 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L1658-L1670)
- **Class:** [DatabaseSelectTestCase](../DatabaseSelectTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testNotNullCondition()
```

## Documentation

```text
Test that we can find a record without a NULL value.
```

## Code

```php
  function testNotNullCondition() {
    $this->ensureSampleDataNull();

    $names = db_select('test_null', 'tn')
      ->fields('tn', array('name'))
      ->isNotNull('tn.age')
      ->orderBy('name')
      ->execute()->fetchCol();

    $this->assertEqual(count($names), 2, 'Correct number of records found withNOT NULL age.');
    $this->assertEqual($names[0], 'Gonzo', 'Correct record returned for NOT NULL age.');
    $this->assertEqual($names[1], 'Kermit', 'Correct record returned for NOT NULL age.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
