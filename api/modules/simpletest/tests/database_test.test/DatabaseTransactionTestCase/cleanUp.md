# DatabaseTransactionTestCase::cleanUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 4051–4054 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L4051-L4054)
- **Class:** [DatabaseTransactionTestCase](../DatabaseTransactionTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
protected function cleanUp()
```

## Documentation

```text
Start over for a new test.
```

## Code

```php
  protected function cleanUp() {
    db_truncate('test')
      ->execute();
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
