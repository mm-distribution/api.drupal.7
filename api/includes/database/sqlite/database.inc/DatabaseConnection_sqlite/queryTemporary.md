# DatabaseConnection_sqlite::queryTemporary()

- **Type:** Method
- **File:** [`includes/database/sqlite/database.inc`](../_file.md), lines 272–282 · [local source](../../../../../../source/includes/database/sqlite/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/database.inc#L272-L282)
- **Class:** [DatabaseConnection_sqlite](../DatabaseConnection_sqlite.md)
- **Topics:** [database](../../../../../topics/database.md)

## Signature

```php
public function queryTemporary($query, array $args = array(), array $options = array())
```

## Documentation

_No docblock in source._

## Code

```php
  public function queryTemporary($query, array $args = array(), array $options = array()) {
    // Generate a new temporary table name and protect it from prefixing.
    // SQLite requires that temporary tables to be non-qualified.
    $tablename = $this->generateTemporaryTableName();
    $prefixes = $this->prefixes;
    $prefixes[$tablename] = '';
    $this->setPrefix($prefixes);

    $this->query('CREATE TEMPORARY TABLE ' . $tablename . ' AS ' . $query, $args, $options);
    return $tablename;
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
