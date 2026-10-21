# DeleteQuery::__toString()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 867–886 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L867-L886)
- **Class:** [DeleteQuery](../DeleteQuery.md)
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

    $query = $comments . 'DELETE FROM {' . $this->connection->escapeTable($this->table) . '} ';

    if (count($this->condition)) {
      try {
        $this->condition->compile($this->connection, $this);
      }
      // PHP does not allow exceptions to be thrown in __toString(), so trigger
      // a fatal error instead.
      catch (InvalidQueryConditionOperatorException $e) {
        drupal_trigger_fatal_error($e->getMessage());
      }
      $query .= "\nWHERE " . $this->condition;
    }

    return $query;
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
