# DatabaseEmptyStatementTestCase::testEmptyIteration()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 4255–4264 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L4255-L4264)
- **Class:** [DatabaseEmptyStatementTestCase](../DatabaseEmptyStatementTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testEmptyIteration()
```

## Documentation

```text
Test that the empty result set iterates safely.
```

## Code

```php
  function testEmptyIteration() {
    $result = new DatabaseStatementEmpty();

    foreach ($result as $record) {
      $this->fail('Iterating empty result set should not iterate.');
      return;
    }

    $this->pass('Iterating empty result set skipped iteration.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
