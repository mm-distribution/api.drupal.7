# DatabaseSchema_mysql::getPrefixInfo()

- **Type:** Method
- **File:** [`includes/database/mysql/schema.inc`](../_file.md), lines 32–47 · [local source](../../../../../../source/includes/database/mysql/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/schema.inc#L32-L47)
- **Class:** [DatabaseSchema_mysql](../DatabaseSchema_mysql.md)
- **Topics:** [schemaapi](../../../../../topics/schemaapi.md)

## Signature

```php
protected function getPrefixInfo($table = 'default', $add_prefix = TRUE)
```

## Documentation

```text
Get information about the table and database name from the prefix.

@return
  A keyed array with information about the database, table name and prefix.
```

## Code

```php
  protected function getPrefixInfo($table = 'default', $add_prefix = TRUE) {
    $info = array('prefix' => $this->connection->tablePrefix($table));
    if ($add_prefix) {
      $table = $info['prefix'] . $table;
    }
    if (($pos = strpos($table, '.')) !== FALSE) {
      $info['database'] = substr($table, 0, $pos);
      $info['table'] = substr($table, ++$pos);
    }
    else {
      $db_info = $this->connection->getConnectionOptions();
      $info['database'] = $db_info['database'];
      $info['table'] = $table;
    }
    return $info;
  }
```

---
_Drupal 7.103 · [includes/database/mysql/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
