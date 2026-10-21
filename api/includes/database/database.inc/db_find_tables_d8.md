# db_find_tables_d8()

- **Type:** Function
- **File:** [`includes/database/database.inc`](_file.md), lines 2925–2927 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2925-L2927)
- **Topics:** [schemaapi](../../../topics/schemaapi.md)

## Signature

```php
function db_find_tables_d8($table_expression)
```

## Documentation

```text
Finds all tables that are like the specified base table name. This is a
backport of the change made to db_find_tables in Drupal 8 to work with
virtual, un-prefixed table names. The original function is retained for
Backwards Compatibility.
@see https://www.drupal.org/node/2552435

@param $table_expression
  An SQL expression, for example "simpletest%" (without the quotes).

@return
  Array, both the keys and the values are the matching tables.
```

## Code

```php
function db_find_tables_d8($table_expression) {
  return Database::getConnection()->schema()->findTablesD8($table_expression);
}
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
