# DatabaseConnection::supportsTransactions()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 1311–1313 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L1311-L1313)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function supportsTransactions()
```

## Documentation

```text
Determines if this driver supports transactions.

@return
  TRUE if this connection supports transactions, FALSE otherwise.
```

## Code

```php
  public function supportsTransactions() {
    return $this->transactionSupport;
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
