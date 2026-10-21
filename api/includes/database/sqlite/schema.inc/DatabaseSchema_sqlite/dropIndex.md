# DatabaseSchema_sqlite::dropIndex()

- **Type:** Method
- **File:** [`includes/database/sqlite/schema.inc`](../_file.md), lines 581–590 · [local source](../../../../../../source/includes/database/sqlite/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc#L581-L590)
- **Class:** [DatabaseSchema_sqlite](../DatabaseSchema_sqlite.md)

## Signature

```php
public function dropIndex($table, $name)
```

## Documentation

_No docblock in source._

## Code

```php
  public function dropIndex($table, $name) {
    if (!$this->indexExists($table, $name)) {
      return FALSE;
    }

    $info = $this->getPrefixInfo($table);

    $this->connection->query('DROP INDEX ' . $info['schema'] . '.' . $info['table'] . '_' . $name);
    return TRUE;
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
