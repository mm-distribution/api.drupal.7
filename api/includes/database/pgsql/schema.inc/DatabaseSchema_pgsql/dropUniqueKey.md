# DatabaseSchema_pgsql::dropUniqueKey()

- **Type:** Method
- **File:** [`includes/database/pgsql/schema.inc`](../_file.md), lines 674–681 · [local source](../../../../../../source/includes/database/pgsql/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc#L674-L681)
- **Class:** [DatabaseSchema_pgsql](../DatabaseSchema_pgsql.md)

## Signature

```php
public function dropUniqueKey($table, $name)
```

## Documentation

_No docblock in source._

## Code

```php
  public function dropUniqueKey($table, $name) {
    if (!$this->constraintExists($table, $name . '_key')) {
      return FALSE;
    }

    $this->connection->query('ALTER TABLE {' . $table . '} DROP CONSTRAINT "' . $this->ensureIdentifiersLength($table, $name, 'key') . '"');
    return TRUE;
  }
```

---
_Drupal 7.103 · [includes/database/pgsql/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
