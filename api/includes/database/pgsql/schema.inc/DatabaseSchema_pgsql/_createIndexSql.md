# DatabaseSchema_pgsql::_createIndexSql()

- **Type:** Method
- **File:** [`includes/database/pgsql/schema.inc`](../_file.md), lines 789–793 · [local source](../../../../../../source/includes/database/pgsql/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc#L789-L793)
- **Class:** [DatabaseSchema_pgsql](../DatabaseSchema_pgsql.md)

## Signature

```php
protected function _createIndexSql($table, $name, $fields)
```

## Documentation

_No docblock in source._

## Code

```php
  protected function _createIndexSql($table, $name, $fields) {
    $query = 'CREATE INDEX "' . $this->ensureIdentifiersLength($table, $name, 'idx') . '" ON {' . $table . '} (';
    $query .= $this->_createKeySql($fields) . ')';
    return $query;
  }
```

---
_Drupal 7.103 · [includes/database/pgsql/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
