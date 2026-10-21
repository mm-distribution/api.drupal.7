# DatabaseConnection_mysql::doCommit()

- **Type:** Method
- **File:** [`includes/database/mysql/database.inc`](../_file.md), lines 585–594 · [local source](../../../../../../source/includes/database/mysql/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/database.inc#L585-L594)
- **Class:** [DatabaseConnection_mysql](../DatabaseConnection_mysql.md)
- **Topics:** [database](../../../../../topics/database.md)

## Signature

```php
protected function doCommit()
```

## Documentation

```text
Do the actual commit, including a workaround for PHP 8 behaviour changes.

@return bool
  Success or otherwise of the commit.
```

## Code

```php
  protected function doCommit() {
    if ($this->connection->inTransaction()) {
      return $this->connection->commit();
    }
    else {
      // In PHP 8.0 a PDOException is thrown when a commit is attempted with no
      // transaction active. In previous PHP versions this failed silently.
      return TRUE;
    }
  }
```

---
_Drupal 7.103 · [includes/database/mysql/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
