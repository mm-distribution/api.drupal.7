# DatabaseTransaction::__construct()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 1999–2015 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L1999-L2015)
- **Class:** [DatabaseTransaction](../DatabaseTransaction.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function __construct(DatabaseConnection $connection, $name = NULL)
```

## Documentation

_No docblock in source._

## Code

```php
  public function __construct(DatabaseConnection $connection, $name = NULL) {
    $this->connection = $connection;
    // If there is no transaction depth, then no transaction has started. Name
    // the transaction 'drupal_transaction'.
    if (!$depth = $connection->transactionDepth()) {
      $this->name = 'drupal_transaction';
    }
    // Within transactions, savepoints are used. Each savepoint requires a
    // name. So if no name is present we need to create one.
    elseif (!$name) {
      $this->name = 'savepoint_' . $depth;
    }
    else {
      $this->name = $name;
    }
    $this->connection->pushTransaction($this->name);
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
