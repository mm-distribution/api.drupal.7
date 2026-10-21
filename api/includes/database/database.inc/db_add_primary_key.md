# db_add_primary_key()

- **Type:** Function
- **File:** [`includes/database/database.inc`](_file.md), lines 3026–3028 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L3026-L3028)
- **Topics:** [schemaapi](../../../topics/schemaapi.md)

## Signature

```php
function db_add_primary_key($table, $fields)
```

## Documentation

```text
Adds a primary key to a database table.

@param $table
  Name of the table to be altered.
@param $fields
  Array of fields for the primary key.
```

## Code

```php
function db_add_primary_key($table, $fields) {
  return Database::getConnection()->schema()->addPrimaryKey($table, $fields);
}
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
