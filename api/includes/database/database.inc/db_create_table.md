# db_create_table()

- **Type:** Function
- **File:** [`includes/database/database.inc`](_file.md), lines 2836–2838 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2836-L2838)
- **Topics:** [schemaapi](../../../topics/schemaapi.md)

## Signature

```php
function db_create_table($name, $table)
```

## Documentation

```text
Creates a new table from a Drupal table definition.

@param $name
  The name of the table to create.
@param $table
  A Schema API table definition array.
```

## Code

```php
function db_create_table($name, $table) {
  return Database::getConnection()->schema()->createTable($name, $table);
}
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
