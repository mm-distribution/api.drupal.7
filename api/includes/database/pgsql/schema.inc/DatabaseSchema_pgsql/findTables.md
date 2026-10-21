# DatabaseSchema_pgsql::findTables()

- **Type:** Method
- **File:** [`includes/database/pgsql/schema.inc`](../_file.md), lines 431–477 · [local source](../../../../../../source/includes/database/pgsql/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc#L431-L477)
- **Class:** [DatabaseSchema_pgsql](../DatabaseSchema_pgsql.md)

## Signature

```php
public function findTables($table_expression)
```

## Documentation

```text
{@inheritdoc}
```

## Code

```php
  public function findTables($table_expression) {
    $individually_prefixed_tables = $this->connection->getUnprefixedTablesMap();
    $default_prefix = $this->connection->tablePrefix();
    $default_prefix_length = strlen($default_prefix);
    $tables = array();

    // Load all the tables up front in order to take into account per-table
    // prefixes. The actual matching is done at the bottom of the method.
    $results = $this->connection->query("SELECT tablename FROM pg_tables WHERE schemaname = :schema", array(':schema' => $this->defaultSchema));
    foreach ($results as $table) {
      // Take into account tables that have an individual prefix.
      if (isset($individually_prefixed_tables[$table->tablename])) {
        $prefix_length = strlen($this->connection->tablePrefix($individually_prefixed_tables[$table->tablename]));
      }
      elseif ($default_prefix && substr($table->tablename, 0, $default_prefix_length) !== $default_prefix) {
        // This table name does not start the default prefix, which means that
        // it is not managed by Drupal so it should be excluded from the result.
        continue;
      }
      else {
        $prefix_length = $default_prefix_length;
      }

      // Remove the prefix from the returned tables.
      $unprefixed_table_name = substr($table->tablename, $prefix_length);

      // The pattern can match a table which is the same as the prefix. That
      // will become an empty string when we remove the prefix, which will
      // probably surprise the caller, besides not being a prefixed table. So
      // remove it.
      if (!empty($unprefixed_table_name)) {
        $tables[$unprefixed_table_name] = $unprefixed_table_name;
      }
    }

    // Need to use strtolower on the table name as it was used previously by
    // DatabaseSchema_pgsql::buildTableNameCondition().
    // @see https://www.drupal.org/project/drupal/issues/3262341
    $table_expression = strtolower($table_expression);

    // Convert the table expression from its SQL LIKE syntax to a regular
    // expression and escape the delimiter that will be used for matching.
    $table_expression = str_replace(array('%', '_'), array('.*?', '.'), preg_quote($table_expression, '/'));
    $tables = preg_grep('/^' . $table_expression . '$/i', $tables);

    return $tables;
  }
```

---
_Drupal 7.103 · [includes/database/pgsql/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
