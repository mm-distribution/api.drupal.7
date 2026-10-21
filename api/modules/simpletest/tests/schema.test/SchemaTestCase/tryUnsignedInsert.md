# SchemaTestCase::tryUnsignedInsert()

- **Type:** Method
- **File:** [`modules/simpletest/tests/schema.test`](../_file.md), lines 211–221 · [local source](../../../../../../source/modules/simpletest/tests/schema.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/schema.test#L211-L221)
- **Class:** [SchemaTestCase](../SchemaTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function tryUnsignedInsert($table_name, $column_name)
```

## Documentation

```text
Tries to insert a negative value into columns defined as unsigned.

@param $table_name
  The table to insert
@param $column_name
  The column to insert
@return
  TRUE if the insert succeeded, FALSE otherwise
```

## Code

```php
  function tryUnsignedInsert($table_name, $column_name) {
    try {
      db_insert($table_name)
         ->fields(array($column_name => -1))
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
