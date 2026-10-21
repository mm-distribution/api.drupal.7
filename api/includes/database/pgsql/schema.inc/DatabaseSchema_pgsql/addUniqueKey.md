# DatabaseSchema_pgsql::addUniqueKey()

- **Type:** Method
- **File:** [`includes/database/pgsql/schema.inc`](../_file.md), lines 663–672 · [local source](../../../../../../source/includes/database/pgsql/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc#L663-L672)
- **Class:** [DatabaseSchema_pgsql](../DatabaseSchema_pgsql.md)

## Signature

```php
function addUniqueKey($table, $name, $fields)
```

## Documentation

_No docblock in source._

## Code

```php
  function addUniqueKey($table, $name, $fields) {
    if (!$this->tableExists($table)) {
      throw new DatabaseSchemaObjectDoesNotExistException(t("Cannot add unique key @name to table @table: table doesn't exist.", array('@table' => $table, '@name' => $name)));
    }
    if ($this->constraintExists($table, $name . '_key')) {
      throw new DatabaseSchemaObjectExistsException(t("Cannot add unique key @name to table @table: unique key already exists.", array('@table' => $table, '@name' => $name)));
    }

    $this->connection->query('ALTER TABLE {' . $table . '} ADD CONSTRAINT "' . $this->ensureIdentifiersLength($table, $name, 'key') . '" UNIQUE (' . implode(',', $fields) . ')');
  }
```

---
_Drupal 7.103 · [includes/database/pgsql/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
