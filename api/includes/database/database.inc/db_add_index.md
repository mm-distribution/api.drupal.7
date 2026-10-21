# db_add_index()

- **Type:** Function
- **File:** [`includes/database/database.inc`](_file.md), lines 3076–3078 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L3076-L3078)
- **Topics:** [schemaapi](../../../topics/schemaapi.md)

## Signature

```php
function db_add_index($table, $name, $fields)
```

## Documentation

```text
Adds an index.

@param $table
  The table to be altered.
@param $name
  The name of the index.
@param $fields
  An array of field names.
```

## Code

```php
function db_add_index($table, $name, $fields) {
  return Database::getConnection()->schema()->addIndex($table, $name, $fields);
}
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
