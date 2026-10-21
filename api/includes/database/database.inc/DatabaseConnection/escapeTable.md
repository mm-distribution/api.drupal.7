# DatabaseConnection::escapeTable()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 986–991 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L986-L991)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function escapeTable($table)
```

## Documentation

```text
Escapes a table name string.

Force all table names to be strictly alphanumeric-plus-underscore.
For some database drivers, it may also wrap the table name in
database-specific escape characters.

@return string
  The sanitized table name string.
```

## Code

```php
  public function escapeTable($table) {
    if (!isset($this->escapedNames[$table])) {
      $this->escapedNames[$table] = preg_replace('/[^A-Za-z0-9_.]+/', '', $table);
    }
    return $this->escapedNames[$table];
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
