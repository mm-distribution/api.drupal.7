# DatabaseSchema_sqlite::createTableSql()

- **Type:** Method
- **File:** [`includes/database/sqlite/schema.inc`](../_file.md), lines 43–47 · [local source](../../../../../../source/includes/database/sqlite/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc#L43-L47)
- **Class:** [DatabaseSchema_sqlite](../DatabaseSchema_sqlite.md)

## Signature

```php
public function createTableSql($name, $table)
```

## Documentation

```text
Generate SQL to create a new table from a Drupal schema definition.

@param $name
  The name of the table to create.
@param $table
  A Schema API table definition array.
@return
  An array of SQL statements to create the table.
```

## Code

```php
  public function createTableSql($name, $table) {
    $sql = array();
    $sql[] = "CREATE TABLE {" . $name . "} (\n" . $this->createColumsSql($name, $table) . "\n);\n";
    return array_merge($sql, $this->createIndexSql($name, $table));
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
