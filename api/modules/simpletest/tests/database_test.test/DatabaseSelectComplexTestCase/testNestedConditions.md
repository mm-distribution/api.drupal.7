# DatabaseSelectComplexTestCase::testNestedConditions()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 2416–2428 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L2416-L2428)
- **Class:** [DatabaseSelectComplexTestCase](../DatabaseSelectComplexTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testNestedConditions()
```

## Documentation

```text
Confirm that we can properly nest conditional clauses.
```

## Code

```php
  function testNestedConditions() {
    // This query should translate to:
    // "SELECT job FROM {test} WHERE name = 'Paul' AND (age = 26 OR age = 27)"
    // That should find only one record. Yes it's a non-optimal way of writing
    // that query but that's not the point!
    $query = db_select('test');
    $query->addField('test', 'job');
    $query->condition('name', 'Paul');
    $query->condition(db_or()->condition('age', 26)->condition('age', 27));

    $job = $query->execute()->fetchField();
    $this->assertEqual($job, 'Songwriter', 'Correct data retrieved.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
