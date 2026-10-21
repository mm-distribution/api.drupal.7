# DatabaseSchema_sqlite::createIndexSql()

- **Type:** Method
- **File:** [`includes/database/sqlite/schema.inc`](../_file.md), lines 52–66 · [local source](../../../../../../source/includes/database/sqlite/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc#L52-L66)
- **Class:** [DatabaseSchema_sqlite](../DatabaseSchema_sqlite.md)

## Signature

```php
protected function createIndexSql($tablename, $schema)
```

## Documentation

```text
Build the SQL expression for indexes.
```

## Code

```php
  protected function createIndexSql($tablename, $schema) {
    $sql = array();
    $info = $this->getPrefixInfo($tablename);
    if (!empty($schema['unique keys'])) {
      foreach ($schema['unique keys'] as $key => $fields) {
        $sql[] = 'CREATE UNIQUE INDEX ' . $info['schema'] . '.' . $info['table'] . '_' . $key . ' ON ' . $info['table'] . ' (' . $this->createKeySql($fields) . "); \n";
      }
    }
    if (!empty($schema['indexes'])) {
      foreach ($schema['indexes'] as $key => $fields) {
        $sql[] = 'CREATE INDEX ' . $info['schema'] . '.' . $info['table'] . '_' . $key . ' ON ' . $info['table'] . ' (' . $this->createKeySql($fields) . "); \n";
      }
    }
    return $sql;
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
