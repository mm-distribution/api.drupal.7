# DatabaseSchema_mysql::fieldExists()

- **Type:** Method
- **File:** [`includes/database/mysql/schema.inc`](../_file.md), lines 528–543 · [local source](../../../../../../source/includes/database/mysql/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/schema.inc#L528-L543)
- **Class:** [DatabaseSchema_mysql](../DatabaseSchema_mysql.md)
- **Topics:** [schemaapi](../../../../../topics/schemaapi.md)

## Signature

```php
public function fieldExists($table, $column)
```

## Documentation

_No docblock in source._

## Code

```php
  public function fieldExists($table, $column) {
    // The information_schema table is very slow to query under MySQL 5.0.
    // Instead, we try to select from the table and field in question. If it
    // fails, the most likely reason is that it does not exist. That is
    // dramatically faster than using information_schema.
    // @link http://bugs.mysql.com/bug.php?id=19588
    // @todo: This override should be removed once we require a version of MySQL
    // that has that bug fixed.
    try {
      $this->connection->queryRange("SELECT $column FROM {" . $table . "}", 0, 1);
      return TRUE;
    }
    catch (Exception $e) {
      return FALSE;
    }
  }
```

---
_Drupal 7.103 · [includes/database/mysql/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
