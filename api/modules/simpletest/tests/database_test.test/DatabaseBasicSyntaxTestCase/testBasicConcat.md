# DatabaseBasicSyntaxTestCase::testBasicConcat()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 3397–3406 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L3397-L3406)
- **Class:** [DatabaseBasicSyntaxTestCase](../DatabaseBasicSyntaxTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testBasicConcat()
```

## Documentation

```text
Test for string concatenation.
```

## Code

```php
  function testBasicConcat() {
    $result = db_query('SELECT CONCAT(:a1, CONCAT(:a2, CONCAT(:a3, CONCAT(:a4, :a5))))', array(
      ':a1' => 'This',
      ':a2' => ' ',
      ':a3' => 'is',
      ':a4' => ' a ',
      ':a5' => 'test.',
    ));
    $this->assertIdentical($result->fetchField(), 'This is a test.', 'Basic CONCAT works.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
