# db_add_unique_key()

- **Type:** Function
- **File:** [`includes/database/database.inc`](_file.md), lines 3050–3052 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L3050-L3052)
- **Topics:** [schemaapi](../../../topics/schemaapi.md)

## Signature

```php
function db_add_unique_key($table, $name, $fields)
```

## Documentation

```text
Adds a unique key.

@param $table
  The table to be altered.
@param $name
  The name of the key.
@param $fields
  An array of field names.
```

## Code

```php
function db_add_unique_key($table, $name, $fields) {
  return Database::getConnection()->schema()->addUniqueKey($table, $name, $fields);
}
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
