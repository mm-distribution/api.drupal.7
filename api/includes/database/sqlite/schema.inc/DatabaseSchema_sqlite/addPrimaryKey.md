# DatabaseSchema_sqlite::addPrimaryKey()

- **Type:** Method
- **File:** [`includes/database/sqlite/schema.inc`](../_file.md), lines 618–632 · [local source](../../../../../../source/includes/database/sqlite/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc#L618-L632)
- **Class:** [DatabaseSchema_sqlite](../DatabaseSchema_sqlite.md)

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

    $old_schema = $this->introspectSchema($table);
    $new_schema = $old_schema;

    if (!empty($new_schema['primary key'])) {
      throw new DatabaseSchemaObjectExistsException(t("Cannot add primary key to table @table: primary key already exists.", array('@table' => $table)));
    }

    $new_schema['primary key'] = $fields;
    $this->alterTable($table, $old_schema, $new_schema);
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
