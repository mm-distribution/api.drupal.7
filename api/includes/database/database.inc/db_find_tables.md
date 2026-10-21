# db_find_tables()

- **Type:** Function
- **File:** [`includes/database/database.inc`](_file.md), lines 2908–2910 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2908-L2910)
- **Topics:** [schemaapi](../../../topics/schemaapi.md)

## Signature

```php
function db_find_tables($table_expression)
```

## Documentation

```text
Finds all tables that are like the specified base table name.

@param $table_expression
  An SQL expression, for example "simpletest%" (without the quotes).

@return
  Array, both the keys and the values are the matching tables.
```

## Code

```php
function db_find_tables($table_expression) {
  return Database::getConnection()->schema()->findTables($table_expression);
}
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
