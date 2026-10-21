# DatabaseConnection::inTransaction()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 1063–1065 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L1063-L1065)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function inTransaction()
```

## Documentation

```text
Determines if there is an active transaction open.

@return
  TRUE if we're currently in a transaction, FALSE otherwise.
```

## Code

```php
  public function inTransaction() {
    return ($this->transactionDepth() > 0);
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
