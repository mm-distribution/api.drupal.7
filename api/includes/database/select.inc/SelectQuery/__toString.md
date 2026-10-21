# SelectQuery::__toString()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 1532–1655 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L1532-L1655)
- **Class:** [SelectQuery](../SelectQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function __toString()
```

## Documentation

_No docblock in source._

## Code

```php
  public function __toString() {
    // For convenience, we compile the query ourselves if the caller forgot
    // to do it. This allows constructs like "(string) $query" to work. When
    // the query will be executed, it will be recompiled using the proper
    // placeholder generator anyway.
    if (!$this->compiled()) {
      try {
        $this->compile($this->connection, $this);
      }
      // PHP does not allow exceptions to be thrown in __toString(), so trigger
      // a fatal error instead.
      catch (InvalidQueryConditionOperatorException $e) {
        drupal_trigger_fatal_error($e->getMessage());
      }
    }

    // Create a sanitized comment string to prepend to the query.
    $comments = $this->connection->makeComment($this->comments);

    // SELECT
    $query = $comments . 'SELECT ';
    if ($this->distinct) {
      $query .= 'DISTINCT ';
    }

    // FIELDS and EXPRESSIONS
    $fields = array();
    foreach ($this->tables as $alias => $table) {
      if (!empty($table['all_fields'])) {
        $fields[] = $this->connection->escapeAlias($alias) . '.*';
      }
    }
    foreach ($this->fields as $alias => $field) {
      // Note that $field['table'] holds the table alias.
      // @see \SelectQuery::addField
      $table = isset($field['table']) ? $this->connection->escapeAlias($field['table']) . '.' : '';
      // Always use the AS keyword for field aliases, as some
      // databases require it (e.g., PostgreSQL).
      $fields[] = $table . $this->connection->escapeField($field['field']) . ' AS ' . $this->connection->escapeAlias($field['alias']);
    }
    foreach ($this->expressions as $alias => $expression) {
      $fields[] = $expression['expression'] . ' AS ' . $this->connection->escapeAlias($expression['alias']);
    }
    $query .= implode(', ', $fields);


    // FROM - We presume all queries have a FROM, as any query that doesn't won't need the query builder anyway.
    $query .= "\nFROM ";
    foreach ($this->tables as $alias => $table) {
      $query .= "\n";
      if (isset($table['join type'])) {
        $query .= $table['join type'] . ' JOIN ';
      }

      // If the table is a subquery, compile it and integrate it into this query.
      if ($table['table'] instanceof SelectQueryInterface) {
        // Run preparation steps on this sub-query before converting to string.
        $subquery = $table['table'];
        $subquery->preExecute();
        $table_string = '(' . (string) $subquery . ')';
      }
      else {
        $table_string = '{' . $this->connection->escapeTable($table['table']) . '}';
      }

      // Don't use the AS keyword for table aliases, as some
      // databases don't support it (e.g., Oracle).
      $query .=  $table_string . ' ' . $this->connection->escapeAlias($table['alias']);

      if (!empty($table['condition'])) {
        $query .= ' ON ' . (string) $table['condition'];
      }
    }

    // WHERE
    if (count($this->where)) {
      // There is an implicit string cast on $this->condition.
      $query .= "\nWHERE " . $this->where;
    }

    // GROUP BY
    if ($this->group) {
      $query .= "\nGROUP BY " . implode(', ', $this->group);
    }

    // HAVING
    if (count($this->having)) {
      // There is an implicit string cast on $this->having.
      $query .= "\nHAVING " . $this->having;
    }

    // UNION is a little odd, as the select queries to combine are passed into
    // this query, but syntactically they all end up on the same level.
    if ($this->union) {
      foreach ($this->union as $union) {
        $query .= ' ' . $union['type'] . ' ' . (string) $union['query'];
      }
    }

    // ORDER BY
    if ($this->order) {
      $query .= "\nORDER BY ";
      $fields = array();
      foreach ($this->order as $field => $direction) {
        $fields[] = $field . ' ' . $direction;
      }
      $query .= implode(', ', $fields);
    }

    // RANGE
    // There is no universal SQL standard for handling range or limit clauses.
    // Fortunately, all core-supported databases use the same range syntax.
    // Databases that need a different syntax can override this method and
    // do whatever alternate logic they need to.
    if (!empty($this->range)) {
      $query .= "\nLIMIT " . (int) $this->range['length'] . " OFFSET " . (int) $this->range['start'];
    }

    if ($this->forUpdate) {
      $query .= ' FOR UPDATE';
    }

    return $query;
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
