# DatabaseConnection_pgsql::queryTemporary()

- **Type:** Method
- **File:** [`includes/database/pgsql/database.inc`](../_file.md), lines 148–152 · [local source](../../../../../../source/includes/database/pgsql/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/database.inc#L148-L152)
- **Class:** [DatabaseConnection_pgsql](../DatabaseConnection_pgsql.md)
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
    $tablename = $this->generateTemporaryTableName();
    $this->query('CREATE TEMPORARY TABLE {' . $tablename . '} AS ' . $query, $args, $options);
    return $tablename;
  }
```

---
_Drupal 7.103 · [includes/database/pgsql/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
