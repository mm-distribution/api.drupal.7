# DatabaseSchema_pgsql::addPrimaryKey()

- **Type:** Method
- **File:** [`includes/database/pgsql/schema.inc`](../_file.md), lines 643–652 · [local source](../../../../../../source/includes/database/pgsql/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc#L643-L652)
- **Class:** [DatabaseSchema_pgsql](../DatabaseSchema_pgsql.md)

## Signature

```php
public function addPrimaryKey($table, $fields)
```

## Documentation

_No docblock in source._

## Code

```php
  public function addPrimaryKey($table, $fields) {
    if (!$this->tableExists($table)) {
      throw new DatabaseSchemaObjectDoesNotExistException(t("Cannot add primary key to table @table: table doesn't exist.", array('@table' => $table)));
    }
    if ($this->constraintExists($table, 'pkey')) {
      throw new DatabaseSchemaObjectExistsException(t("Cannot add primary key to table @table: primary key already exists.", array('@table' => $table)));
    }

    $this->connection->query('ALTER TABLE {' . $table . '} ADD CONSTRAINT ' . $this->ensureIdentifiersLength($table, '', 'pkey') . ' PRIMARY KEY (' . implode(',', $fields) . ')');
  }
```

---
_Drupal 7.103 · [includes/database/pgsql/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
