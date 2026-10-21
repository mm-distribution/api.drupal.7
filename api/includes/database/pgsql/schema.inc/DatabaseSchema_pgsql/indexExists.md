# DatabaseSchema_pgsql::indexExists()

- **Type:** Method
- **File:** [`includes/database/pgsql/schema.inc`](../_file.md), lines 613–617 · [local source](../../../../../../source/includes/database/pgsql/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc#L613-L617)
- **Class:** [DatabaseSchema_pgsql](../DatabaseSchema_pgsql.md)

## Signature

```php
public function indexExists($table, $name)
```

## Documentation

_No docblock in source._

## Code

```php
  public function indexExists($table, $name) {
    // Details https://www.postgresql.org/docs/10/view-pg-indexes.html
    $index_name = $this->ensureIdentifiersLength($table, $name, 'idx');
    return (bool) $this->connection->query("SELECT 1 FROM pg_indexes WHERE indexname = '$index_name'")->fetchField();
  }
```

---
_Drupal 7.103 · [includes/database/pgsql/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
