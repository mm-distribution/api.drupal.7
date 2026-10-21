# DeleteQuery_sqlite::execute()

- **Type:** Method
- **File:** [`includes/database/sqlite/query.inc`](../_file.md), lines 107–122 · [local source](../../../../../../source/includes/database/sqlite/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/query.inc#L107-L122)
- **Class:** [DeleteQuery_sqlite](../DeleteQuery_sqlite.md)
- **Topics:** [database](../../../../../topics/database.md)

## Signature

```php
public function execute()
```

## Documentation

_No docblock in source._

## Code

```php
  public function execute() {
    // When the WHERE is omitted from a DELETE statement and the table being
    // deleted has no triggers, SQLite uses an optimization to erase the entire
    // table content without having to visit each row of the table individually.
    // Prior to SQLite 3.6.5, SQLite does not return the actual number of rows
    // deleted by that optimized "truncate" optimization. But we want to return
    // the number of rows affected, so we calculate it directly.
    if (!count($this->condition)) {
      $total_rows = $this->connection->query('SELECT COUNT(*) FROM {' . $this->connection->escapeTable($this->table) . '}')->fetchField();
      parent::execute();
      return $total_rows;
    }
    else {
      return parent::execute();
    }
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
