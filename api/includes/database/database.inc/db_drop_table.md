# db_drop_table()

- **Type:** Function
- **File:** [`includes/database/database.inc`](_file.md), lines 2951–2953 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2951-L2953)
- **Topics:** [schemaapi](../../../topics/schemaapi.md)

## Signature

```php
function db_drop_table($table)
```

## Documentation

```text
Drops a table.

@param $table
  The table to be dropped.
```

## Code

```php
function db_drop_table($table) {
  return Database::getConnection()->schema()->dropTable($table);
}
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
