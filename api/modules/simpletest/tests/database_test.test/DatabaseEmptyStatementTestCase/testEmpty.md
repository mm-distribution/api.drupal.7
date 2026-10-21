# DatabaseEmptyStatementTestCase::testEmpty()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 4245–4250 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L4245-L4250)
- **Class:** [DatabaseEmptyStatementTestCase](../DatabaseEmptyStatementTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testEmpty()
```

## Documentation

```text
Test that the empty result set behaves as empty.
```

## Code

```php
  function testEmpty() {
    $result = new DatabaseStatementEmpty();

    $this->assertTrue($result instanceof DatabaseStatementInterface, 'Class implements expected interface');
    $this->assertNull($result->fetchObject(), 'Null result returned.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
