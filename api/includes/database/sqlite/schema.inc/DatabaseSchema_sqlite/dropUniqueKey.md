# DatabaseSchema_sqlite::dropUniqueKey()

- **Type:** Method
- **File:** [`includes/database/sqlite/schema.inc`](../_file.md), lines 607–616 · [local source](../../../../../../source/includes/database/sqlite/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc#L607-L616)
- **Class:** [DatabaseSchema_sqlite](../DatabaseSchema_sqlite.md)

## Signature

```php
public function dropUniqueKey($table, $name)
```

## Documentation

_No docblock in source._

## Code

```php
  public function dropUniqueKey($table, $name) {
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
