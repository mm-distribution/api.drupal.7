# UpdateQuery::__toString()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 1192–1235 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L1192-L1235)
- **Class:** [UpdateQuery](../UpdateQuery.md)
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
    if (!is_array($this->expressionFields) || !is_array($this->fields)) {
      if (version_compare(PHP_VERSION, '7.4', '>=')) {
        throw new UnexpectedValueException();
      }
      else {
        drupal_trigger_fatal_error('Unexpected Value');
      }
    }

    // Create a sanitized comment string to prepend to the query.
    $comments = $this->connection->makeComment($this->comments);

    // Expressions take priority over literal fields, so we process those first
    // and remove any literal fields that conflict.
    $fields = $this->fields;
    $update_fields = array();
    foreach ($this->expressionFields as $field => $data) {
      $update_fields[] = $field . '=' . $data['expression'];
      unset($fields[$field]);
    }

    $max_placeholder = 0;
    foreach ($fields as $field => $value) {
      $update_fields[] = $field . '=:db_update_placeholder_' . ($max_placeholder++);
    }

    $query = $comments . 'UPDATE {' . $this->connection->escapeTable($this->table) . '} SET ' . implode(', ', $update_fields);

    if (count($this->condition)) {
      try {
        $this->condition->compile($this->connection, $this);
      }
      // PHP does not allow exceptions to be thrown in __toString(), so trigger
      // a fatal error instead.
      catch (InvalidQueryConditionOperatorException $e) {
        drupal_trigger_fatal_error($e->getMessage());
      }
      // There is an implicit string cast on $this->condition.
      $query .= "\nWHERE " . $this->condition;
    }

    return $query;
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
