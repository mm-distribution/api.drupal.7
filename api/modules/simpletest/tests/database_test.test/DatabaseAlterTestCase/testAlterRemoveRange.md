# DatabaseAlterTestCase::testAlterRemoveRange()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 3036–3046 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L3036-L3046)
- **Class:** [DatabaseAlterTestCase](../DatabaseAlterTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testAlterRemoveRange()
```

## Documentation

```text
Test that we can remove a range() value from a query. This also tests hook_query_TAG_alter().
```

## Code

```php
  function testAlterRemoveRange() {
    $query = db_select('test');
    $query->addField('test', 'name');
    $query->addField('test', 'age', 'age');
    $query->range(0, 2);
    $query->addTag('database_test_alter_remove_range');

    $num_records = count($query->execute()->fetchAll());

    $this->assertEqual($num_records, 4, 'Returned the correct number of rows.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
