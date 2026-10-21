# DatabaseSchema_pgsql::getComment()

- **Type:** Method
- **File:** [`includes/database/pgsql/schema.inc`](../_file.md), lines 814–823 · [local source](../../../../../../source/includes/database/pgsql/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc#L814-L823)
- **Class:** [DatabaseSchema_pgsql](../DatabaseSchema_pgsql.md)

## Signature

```php
public function getComment($table, $column = NULL)
```

## Documentation

```text
Retrieve a table or column comment.
```

## Code

```php
  public function getComment($table, $column = NULL) {
    $info = $this->getPrefixInfo($table);
    // Don't use {} around pg_class, pg_attribute tables.
    if (isset($column)) {
      return $this->connection->query('SELECT col_description(oid, attnum) FROM pg_class, pg_attribute WHERE attrelid = oid AND relname = ? AND attname = ?', array($info['table'], $column))->fetchField();
    }
    else {
      return $this->connection->query('SELECT obj_description(oid, ?) FROM pg_class WHERE relname = ?', array('pg_class', $info['table']))->fetchField();
    }
  }
```

---
_Drupal 7.103 · [includes/database/pgsql/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
