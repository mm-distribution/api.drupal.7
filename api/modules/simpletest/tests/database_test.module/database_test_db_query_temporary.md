# database_test_db_query_temporary()

- **Type:** Function
- **File:** [`modules/simpletest/tests/database_test.module`](_file.md), lines 83–90 · [local source](../../../../../source/modules/simpletest/tests/database_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.module#L83-L90)
- **Module/theme:** batch_test

## Signature

```php
function database_test_db_query_temporary()
```

## Documentation

```text
Run a db_query_temporary and output the table name and its number of rows.

We need to test that the table created is temporary, so we run it here, in a
separate menu callback request; After this request is done, the temporary
table should automatically dropped.
```

## Code

```php
function database_test_db_query_temporary() {
  $table_name = db_query_temporary('SELECT status FROM {system}', array());
  drupal_json_output(array(
    'table_name' => $table_name,
    'row_count' => db_select($table_name)->countQuery()->execute()->fetchField(),
  ));
  exit;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
