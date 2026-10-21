# DatabaseSchema_sqlite::dropTable()

- **Type:** Method
- **File:** [`includes/database/sqlite/schema.inc`](../_file.md), lines 270–277 · [local source](../../../../../../source/includes/database/sqlite/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc#L270-L277)
- **Class:** [DatabaseSchema_sqlite](../DatabaseSchema_sqlite.md)

## Signature

```php
public function dropTable($table)
```

## Documentation

_No docblock in source._

## Code

```php
  public function dropTable($table) {
    if (!$this->tableExists($table)) {
      return FALSE;
    }
    $this->connection->tableDropped = TRUE;
    $this->connection->query('DROP TABLE {' . $table . '}');
    return TRUE;
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
