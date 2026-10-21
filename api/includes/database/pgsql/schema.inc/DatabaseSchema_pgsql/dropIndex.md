# DatabaseSchema_pgsql::dropIndex()

- **Type:** Method
- **File:** [`includes/database/pgsql/schema.inc`](../_file.md), lines 694–701 · [local source](../../../../../../source/includes/database/pgsql/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc#L694-L701)
- **Class:** [DatabaseSchema_pgsql](../DatabaseSchema_pgsql.md)

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

    $this->connection->query('DROP INDEX ' . $this->ensureIdentifiersLength($table, $name, 'idx'));
    return TRUE;
  }
```

---
_Drupal 7.103 · [includes/database/pgsql/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
