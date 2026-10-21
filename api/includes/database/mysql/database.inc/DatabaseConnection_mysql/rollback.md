# DatabaseConnection_mysql::rollback()

- **Type:** Method
- **File:** [`includes/database/mysql/database.inc`](../_file.md), lines 599–624 · [local source](../../../../../../source/includes/database/mysql/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/database.inc#L599-L624)
- **Class:** [DatabaseConnection_mysql](../DatabaseConnection_mysql.md)
- **Topics:** [database](../../../../../topics/database.md)

## Signature

```php
public function rollback($savepoint_name = 'drupal_transaction')
```

## Documentation

```text
{@inheritdoc}
```

## Code

```php
  public function rollback($savepoint_name = 'drupal_transaction') {
    // MySQL will automatically commit transactions when tables are altered or
    // created (DDL transactions are not supported). Prevent triggering an
    // exception to ensure that the error that has caused the rollback is
    // properly reported.
    if (!$this->connection->inTransaction()) {
      // Before PHP 8 $this->connection->inTransaction() will return TRUE and
      // $this->connection->rollback() does not throw an exception; the
      // following code is unreachable.

      // If \DatabaseConnection::rollback() would throw an
      // exception then continue to throw an exception.
      if (!$this->inTransaction()) {
        throw new DatabaseTransactionNoActiveException();
      }
      // A previous rollback to an earlier savepoint may mean that the savepoint
      // in question has already been accidentally committed.
      if (!isset($this->transactionLayers[$savepoint_name])) {
        throw new DatabaseTransactionNoActiveException();
      }

      trigger_error('Rollback attempted when there is no active transaction. This can cause data integrity issues.', E_USER_WARNING);
      return;
    }
    return parent::rollback($savepoint_name);
  }
```

---
_Drupal 7.103 · [includes/database/mysql/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
