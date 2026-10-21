# db_escape_table()

- **Type:** Function
- **File:** [`includes/database/database.inc`](_file.md), lines 2686–2688 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2686-L2688)
- **Topics:** [database](../../../topics/database.md)

## Signature

```php
function db_escape_table($table)
```

## Documentation

```text
Restricts a dynamic table name to safe characters.

Only keeps alphanumeric and underscores.

@param $table
  The table name to escape.

@return
  The escaped table name as a string.
```

## Code

```php
function db_escape_table($table) {
  return Database::getConnection()->escapeTable($table);
}
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
