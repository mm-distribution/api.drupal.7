# DatabaseSchema_mysql::indexExists()

- **Type:** Method
- **File:** [`includes/database/mysql/schema.inc`](../_file.md), lines 398–403 · [local source](../../../../../../source/includes/database/mysql/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/schema.inc#L398-L403)
- **Class:** [DatabaseSchema_mysql](../DatabaseSchema_mysql.md)
- **Topics:** [schemaapi](../../../../../topics/schemaapi.md)

## Signature

```php
public function indexExists($table, $name)
```

## Documentation

_No docblock in source._

## Code

```php
  public function indexExists($table, $name) {
    // Returns one row for each column in the index. Result is string or FALSE.
    // Details at http://dev.mysql.com/doc/refman/5.0/en/show-index.html
    $row = $this->connection->query('SHOW INDEX FROM {' . $table . "} WHERE key_name = '$name'")->fetchAssoc();
    return isset($row['Key_name']);
  }
```

---
_Drupal 7.103 · [includes/database/mysql/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
