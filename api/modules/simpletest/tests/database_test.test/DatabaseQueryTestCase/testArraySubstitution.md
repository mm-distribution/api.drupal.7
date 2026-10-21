# DatabaseQueryTestCase::testArraySubstitution()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 3604–3608 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L3604-L3608)
- **Class:** [DatabaseQueryTestCase](../DatabaseQueryTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testArraySubstitution()
```

## Documentation

```text
Test that we can specify an array of values in the query by simply passing in an array.
```

## Code

```php
  function testArraySubstitution() {
    $names = db_query('SELECT name FROM {test} WHERE age IN (:ages) ORDER BY age', array(':ages' => array(25, 26, 27)))->fetchAll();

    $this->assertEqual(count($names), 3, 'Correct number of names returned');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
