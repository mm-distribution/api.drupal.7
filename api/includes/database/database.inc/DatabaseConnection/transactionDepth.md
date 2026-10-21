# DatabaseConnection::transactionDepth()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 1070–1072 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L1070-L1072)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function transactionDepth()
```

## Documentation

```text
Determines current transaction depth.
```

## Code

```php
  public function transactionDepth() {
    return count($this->transactionLayers);
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
