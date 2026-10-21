# DatabaseSchema_pgsql::addIndex()

- **Type:** Method
- **File:** [`includes/database/pgsql/schema.inc`](../_file.md), lines 683–692 · [local source](../../../../../../source/includes/database/pgsql/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc#L683-L692)
- **Class:** [DatabaseSchema_pgsql](../DatabaseSchema_pgsql.md)

## Signature

```php
public function addIndex($table, $name, $fields)
```

## Documentation

_No docblock in source._

## Code

```php
  public function addIndex($table, $name, $fields) {
    if (!$this->tableExists($table)) {
      throw new DatabaseSchemaObjectDoesNotExistException(t("Cannot add index @name to table @table: table doesn't exist.", array('@table' => $table, '@name' => $name)));
    }
    if ($this->indexExists($table, $name)) {
      throw new DatabaseSchemaObjectExistsException(t("Cannot add index @name to table @table: index already exists.", array('@table' => $table, '@name' => $name)));
    }

    $this->connection->query($this->_createIndexSql($table, $name, $fields));
  }
```

---
_Drupal 7.103 · [includes/database/pgsql/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
