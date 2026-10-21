# DatabaseInsertDefaultsTestCase::testDefaultEmptyInsert()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 794–807 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L794-L807)
- **Class:** [DatabaseInsertDefaultsTestCase](../DatabaseInsertDefaultsTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testDefaultEmptyInsert()
```

## Documentation

```text
Test that no action will be preformed if no fields are specified.
```

## Code

```php
  function testDefaultEmptyInsert() {
    $num_records_before = (int) db_query('SELECT COUNT(*) FROM {test}')->fetchField();

    try {
      $result = db_insert('test')->execute();
      // This is only executed if no exception has been thrown.
      $this->fail('Expected exception NoFieldsException has not been thrown.');
    } catch (NoFieldsException $e) {
      $this->pass('Expected exception NoFieldsException has been thrown.');
    }

    $num_records_after = (int) db_query('SELECT COUNT(*) FROM {test}')->fetchField();
    $this->assertIdentical($num_records_before, $num_records_after, 'Do nothing as no fields are specified.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
