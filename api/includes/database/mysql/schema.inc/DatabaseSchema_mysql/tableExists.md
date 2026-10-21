# DatabaseSchema_mysql::tableExists()

- **Type:** Method
- **File:** [`includes/database/mysql/schema.inc`](../_file.md), lines 511–526 · [local source](../../../../../../source/includes/database/mysql/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/schema.inc#L511-L526)
- **Class:** [DatabaseSchema_mysql](../DatabaseSchema_mysql.md)
- **Topics:** [schemaapi](../../../../../topics/schemaapi.md)

## Signature

```php
public function tableExists($table)
```

## Documentation

_No docblock in source._

## Code

```php
  public function tableExists($table) {
    // The information_schema table is very slow to query under MySQL 5.0.
    // Instead, we try to select from the table in question.  If it fails,
    // the most likely reason is that it does not exist. That is dramatically
    // faster than using information_schema.
    // @link http://bugs.mysql.com/bug.php?id=19588
    // @todo: This override should be removed once we require a version of MySQL
    // that has that bug fixed.
    try {
      $this->connection->queryRange("SELECT 1 FROM {" . $table . "}", 0, 1);
      return TRUE;
    }
    catch (Exception $e) {
      return FALSE;
    }
  }
```

---
_Drupal 7.103 · [includes/database/mysql/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
