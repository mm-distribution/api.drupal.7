# db_drop_primary_key()

- **Type:** Function
- **File:** [`includes/database/database.inc`](_file.md), lines 3036–3038 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L3036-L3038)
- **Topics:** [schemaapi](../../../topics/schemaapi.md)

## Signature

```php
function db_drop_primary_key($table)
```

## Documentation

```text
Drops the primary key of a database table.

@param $table
  Name of the table to be altered.
```

## Code

```php
function db_drop_primary_key($table) {
  return Database::getConnection()->schema()->dropPrimaryKey($table);
}
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
