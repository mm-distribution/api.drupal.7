# db_field_exists()

- **Type:** Function
- **File:** [`includes/database/database.inc`](_file.md), lines 2895–2897 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2895-L2897)
- **Topics:** [schemaapi](../../../topics/schemaapi.md)

## Signature

```php
function db_field_exists($table, $field)
```

## Documentation

```text
Checks if a column exists in the given table.

@param $table
  The name of the table in drupal (no prefixing).
@param $field
  The name of the field.

@return
  TRUE if the given column exists, otherwise FALSE.
```

## Code

```php
function db_field_exists($table, $field) {
  return Database::getConnection()->schema()->fieldExists($table, $field);
}
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
