# DatabaseBasicSyntaxTestCase::testFieldConcat()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 3411–3419 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L3411-L3419)
- **Class:** [DatabaseBasicSyntaxTestCase](../DatabaseBasicSyntaxTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testFieldConcat()
```

## Documentation

```text
Test for string concatenation with field values.
```

## Code

```php
  function testFieldConcat() {
    $result = db_query('SELECT CONCAT(:a1, CONCAT(name, CONCAT(:a2, CONCAT(age, :a3)))) FROM {test} WHERE age = :age', array(
      ':a1' => 'The age of ',
      ':a2' => ' is ',
      ':a3' => '.',
      ':age' => 25,
    ));
    $this->assertIdentical($result->fetchField(), 'The age of John is 25.', 'Field CONCAT works.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
