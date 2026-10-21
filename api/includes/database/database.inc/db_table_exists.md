# db_table_exists()

- **Type:** Function
- **File:** [`includes/database/database.inc`](_file.md), lines 2880–2882 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2880-L2882)
- **Topics:** [schemaapi](../../../topics/schemaapi.md)

## Signature

```php
function db_table_exists($table)
```

## Documentation

```text
Checks if a table exists.

@param $table
  The name of the table in drupal (no prefixing).

@return
  TRUE if the given table exists, otherwise FALSE.
```

## Code

```php
function db_table_exists($table) {
  return Database::getConnection()->schema()->tableExists($table);
}
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
