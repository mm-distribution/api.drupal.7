# DatabaseSchema_pgsql::dropPrimaryKey()

- **Type:** Method
- **File:** [`includes/database/pgsql/schema.inc`](../_file.md), lines 654–661 · [local source](../../../../../../source/includes/database/pgsql/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc#L654-L661)
- **Class:** [DatabaseSchema_pgsql](../DatabaseSchema_pgsql.md)

## Signature

```php
public function dropPrimaryKey($table)
```

## Documentation

_No docblock in source._

## Code

```php
  public function dropPrimaryKey($table) {
    if (!$this->constraintExists($table, 'pkey')) {
      return FALSE;
    }

    $this->connection->query('ALTER TABLE {' . $table . '} DROP CONSTRAINT ' . $this->ensureIdentifiersLength($table, '', 'pkey'));
    return TRUE;
  }
```

---
_Drupal 7.103 · [includes/database/pgsql/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
