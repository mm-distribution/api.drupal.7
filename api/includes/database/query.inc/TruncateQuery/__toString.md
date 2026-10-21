# TruncateQuery::__toString()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 948–963 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L948-L963)
- **Class:** [TruncateQuery](../TruncateQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function __toString()
```

## Documentation

```text
Implements PHP magic __toString method to convert the query to a string.

@return string
  The prepared statement.
```

## Code

```php
  public function __toString() {
    // Create a sanitized comment string to prepend to the query.
    $comments = $this->connection->makeComment($this->comments);

    // In most cases, TRUNCATE is not a transaction safe statement as it is a
    // DDL statement which results in an implicit COMMIT. When we are in a
    // transaction, fallback to the slower, but transactional, DELETE.
    // PostgreSQL also locks the entire table for a TRUNCATE strongly reducing
    // the concurrency with other transactions.
    if ($this->connection->inTransaction()) {
      return $comments . 'DELETE FROM {' . $this->connection->escapeTable($this->table) . '}';
    }
    else {
      return $comments . 'TRUNCATE {' . $this->connection->escapeTable($this->table) . '} ';
    }
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
