# SchemaTestCase::tryInsert()

- **Type:** Method
- **File:** [`modules/simpletest/tests/schema.test`](../_file.md), lines 140–150 · [local source](../../../../../../source/modules/simpletest/tests/schema.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/schema.test#L140-L150)
- **Class:** [SchemaTestCase](../SchemaTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function tryInsert($table = 'test_table')
```

## Documentation

_No docblock in source._

## Code

```php
  function tryInsert($table = 'test_table') {
    try {
       db_insert($table)
         ->fields(array('id' => mt_rand(10, 20)))
         ->execute();
      return TRUE;
    }
    catch (Exception $e) {
      return FALSE;
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/schema.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/schema.test) · Licensed GPL-2.0-or-later (see LICENSE)._
