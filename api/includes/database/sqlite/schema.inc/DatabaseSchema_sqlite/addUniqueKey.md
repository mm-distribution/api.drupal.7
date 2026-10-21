# DatabaseSchema_sqlite::addUniqueKey()

- **Type:** Method
- **File:** [`includes/database/sqlite/schema.inc`](../_file.md), lines 592–605 · [local source](../../../../../../source/includes/database/sqlite/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc#L592-L605)
- **Class:** [DatabaseSchema_sqlite](../DatabaseSchema_sqlite.md)

## Signature

```php
public function addUniqueKey($table, $name, $fields)
```

## Documentation

_No docblock in source._

## Code

```php
  public function addUniqueKey($table, $name, $fields) {
    if (!$this->tableExists($table)) {
      throw new DatabaseSchemaObjectDoesNotExistException(t("Cannot add unique key @name to table @table: table doesn't exist.", array('@table' => $table, '@name' => $name)));
    }
    if ($this->indexExists($table, $name)) {
      throw new DatabaseSchemaObjectExistsException(t("Cannot add unique key @name to table @table: unique key already exists.", array('@table' => $table, '@name' => $name)));
    }

    $schema['unique keys'][$name] = $fields;
    $statements = $this->createIndexSql($table, $schema);
    foreach ($statements as $statement) {
      $this->connection->query($statement);
    }
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
