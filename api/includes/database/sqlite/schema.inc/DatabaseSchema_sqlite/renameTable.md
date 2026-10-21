# DatabaseSchema_sqlite::renameTable()

- **Type:** Method
- **File:** [`includes/database/sqlite/schema.inc`](../_file.md), lines 233–268 · [local source](../../../../../../source/includes/database/sqlite/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc#L233-L268)
- **Class:** [DatabaseSchema_sqlite](../DatabaseSchema_sqlite.md)

## Signature

```php
public function renameTable($table, $new_name)
```

## Documentation

_No docblock in source._

## Code

```php
  public function renameTable($table, $new_name) {
    if (!$this->tableExists($table)) {
      throw new DatabaseSchemaObjectDoesNotExistException(t("Cannot rename @table to @table_new: table @table doesn't exist.", array('@table' => $table, '@table_new' => $new_name)));
    }
    if ($this->tableExists($new_name)) {
      throw new DatabaseSchemaObjectExistsException(t("Cannot rename @table to @table_new: table @table_new already exists.", array('@table' => $table, '@table_new' => $new_name)));
    }

    $schema = $this->introspectSchema($table);

    // SQLite doesn't allow you to rename tables outside of the current
    // database. So the syntax '...RENAME TO database.table' would fail.
    // So we must determine the full table name here rather than surrounding
    // the table with curly braces incase the db_prefix contains a reference
    // to a database outside of our existing database.
    $info = $this->getPrefixInfo($new_name);
    $this->connection->query('ALTER TABLE {' . $table . '} RENAME TO ' . $info['table']);

    // Drop the indexes, there is no RENAME INDEX command in SQLite.
    if (!empty($schema['unique keys'])) {
      foreach ($schema['unique keys'] as $key => $fields) {
        $this->dropIndex($table, $key);
      }
    }
    if (!empty($schema['indexes'])) {
      foreach ($schema['indexes'] as $index => $fields) {
        $this->dropIndex($table, $index);
      }
    }

    // Recreate the indexes.
    $statements = $this->createIndexSql($new_name, $schema);
    foreach ($statements as $statement) {
      $this->connection->query($statement);
    }
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
