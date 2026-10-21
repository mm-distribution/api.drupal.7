# DatabaseSchema_sqlite::tableExists()

- **Type:** Method
- **File:** [`includes/database/sqlite/schema.inc`](../_file.md), lines 21–26 · [local source](../../../../../../source/includes/database/sqlite/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc#L21-L26)
- **Class:** [DatabaseSchema_sqlite](../DatabaseSchema_sqlite.md)

## Signature

```php
public function tableExists($table)
```

## Documentation

_No docblock in source._

## Code

```php
  public function tableExists($table) {
    $info = $this->getPrefixInfo($table);

    // Don't use {} around sqlite_master table.
    return (bool) $this->connection->query('SELECT 1 FROM ' . $info['schema'] . '.sqlite_master WHERE type = :type AND name = :name', array(':type' => 'table', ':name' => $info['table']))->fetchField();
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
