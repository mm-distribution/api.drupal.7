# db_rename_table()

- **Type:** Function
- **File:** [`includes/database/database.inc`](_file.md), lines 2941–2943 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2941-L2943)
- **Topics:** [schemaapi](../../../topics/schemaapi.md)

## Signature

```php
function db_rename_table($table, $new_name)
```

## Documentation

```text
Renames a table.

@param $table
  The current name of the table to be renamed.
@param $new_name
  The new name for the table.
```

## Code

```php
function db_rename_table($table, $new_name) {
  return Database::getConnection()->schema()->renameTable($table, $new_name);
}
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
