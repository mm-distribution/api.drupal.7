# DatabaseSchema_sqlite::findTablesD8()

- **Type:** Method
- **File:** [`includes/database/sqlite/schema.inc`](../_file.md), lines 690–712 · [local source](../../../../../../source/includes/database/sqlite/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc#L690-L712)
- **Class:** [DatabaseSchema_sqlite](../DatabaseSchema_sqlite.md)

## Signature

```php
public function findTablesD8($table_expression)
```

## Documentation

```text
{@inheritdoc}
```

## Code

```php
  public function findTablesD8($table_expression) {
    $tables = array();

    // The SQLite implementation doesn't need to use the same filtering strategy
    // as the parent one because individually prefixed tables live in their own
    // schema (database), which means that neither the main database nor any
    // attached one will contain a prefixed table name, so we just need to loop
    // over all known schemas and filter by the user-supplied table expression.
    $attached_dbs = $this->connection->getAttachedDatabases();
    foreach ($attached_dbs as $schema) {
      // Can't use query placeholders for the schema because the query would
      // have to be :prefixsqlite_master, which does not work. We also need to
      // ignore the internal SQLite tables.
      $result = db_query("SELECT name FROM " . $schema . ".sqlite_master WHERE type = :type AND name LIKE :table_name AND name NOT LIKE :pattern", array(
        ':type' => 'table',
        ':table_name' => $table_expression,
        ':pattern' => 'sqlite_%',
      ));
      $tables += $result->fetchAllKeyed(0, 0);
    }

    return $tables;
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
