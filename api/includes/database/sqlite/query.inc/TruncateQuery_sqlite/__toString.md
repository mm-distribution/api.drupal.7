# TruncateQuery_sqlite::__toString()

- **Type:** Method
- **File:** [`includes/database/sqlite/query.inc`](../_file.md), lines 132–137 · [local source](../../../../../../source/includes/database/sqlite/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/query.inc#L132-L137)
- **Class:** [TruncateQuery_sqlite](../TruncateQuery_sqlite.md)
- **Topics:** [database](../../../../../topics/database.md)

## Signature

```php
public function __toString()
```

## Documentation

_No docblock in source._

## Code

```php
  public function __toString() {
    // Create a sanitized comment string to prepend to the query.
    $comments = $this->connection->makeComment($this->comments);

    return $comments . 'DELETE FROM {' . $this->connection->escapeTable($this->table) . '} ';
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
