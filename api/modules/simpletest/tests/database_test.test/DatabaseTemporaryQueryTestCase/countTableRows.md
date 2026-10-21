# DatabaseTemporaryQueryTestCase::countTableRows()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 3338–3340 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L3338-L3340)
- **Class:** [DatabaseTemporaryQueryTestCase](../DatabaseTemporaryQueryTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function countTableRows($table_name)
```

## Documentation

```text
Return the number of rows of a table.
```

## Code

```php
  function countTableRows($table_name) {
    return db_select($table_name)->countQuery()->execute()->fetchField();
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
