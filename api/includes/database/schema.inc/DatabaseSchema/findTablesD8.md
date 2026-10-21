# DatabaseSchema::findTablesD8()

- **Type:** Method
- **File:** [`includes/database/schema.inc`](../_file.md), lines 367–415 · [local source](../../../../../source/includes/database/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc#L367-L415)
- **Class:** [DatabaseSchema](../DatabaseSchema.md)
- **Topics:** [schemaapi](../../../../topics/schemaapi.md)

## Signature

```php
public function findTablesD8($table_expression)
```

## Documentation

```text
Finds all tables that are like the specified base table name. This is a
backport of the change made to findTables in Drupal 8 to work with virtual,
un-prefixed table names. The original function is retained for Backwards
Compatibility.
@see https://www.drupal.org/node/2552435

@param string $table_expression
  An SQL expression, for example "cache_%" (without the quotes).

@return array
  Both the keys and the values are the matching tables.
```

## Code

```php
  public function findTablesD8($table_expression) {
    // Load all the tables up front in order to take into account per-table
    // prefixes. The actual matching is done at the bottom of the method.
    $condition = $this->buildTableNameCondition('%', 'LIKE');
    $condition->compile($this->connection, $this);

    $individually_prefixed_tables = $this->connection->getUnprefixedTablesMap();
    $default_prefix = $this->connection->tablePrefix();
    $default_prefix_length = strlen($default_prefix);
    $tables = array();
    // Normally, we would heartily discourage the use of string
    // concatenation for conditionals like this however, we
    // couldn't use db_select() here because it would prefix
    // information_schema.tables and the query would fail.
    // Don't use {} around information_schema.tables table.
    $results = $this->connection->query("SELECT table_name AS table_name FROM information_schema.tables WHERE " . (string) $condition, $condition->arguments());
    foreach ($results as $table) {
      // Take into account tables that have an individual prefix.
      if (isset($individually_prefixed_tables[$table->table_name])) {
        $prefix_length = strlen($this->connection->tablePrefix($individually_prefixed_tables[$table->table_name]));
      }
      elseif ($default_prefix && substr($table->table_name, 0, $default_prefix_length) !== $default_prefix) {
        // This table name does not start the default prefix, which means that
        // it is not managed by Drupal so it should be excluded from the result.
        continue;
      }
      else {
        $prefix_length = $default_prefix_length;
      }

      // Remove the prefix from the returned tables.
      $unprefixed_table_name = substr($table->table_name, $prefix_length);

      // The pattern can match a table which is the same as the prefix. That
      // will become an empty string when we remove the prefix, which will
      // probably surprise the caller, besides not being a prefixed table. So
      // remove it.
      if (!empty($unprefixed_table_name)) {
        $tables[$unprefixed_table_name] = $unprefixed_table_name;
      }
    }

    // Convert the table expression from its SQL LIKE syntax to a regular
    // expression and escape the delimiter that will be used for matching.
    $table_expression = str_replace(array('%', '_'), array('.*?', '.'), preg_quote($table_expression, '/'));
    $tables = preg_grep('/^' . $table_expression . '$/i', $tables);

    return $tables;
  }
```

---
_Drupal 7.103 · [includes/database/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
