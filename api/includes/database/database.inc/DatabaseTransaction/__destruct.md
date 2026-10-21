# DatabaseTransaction::__destruct()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 2017–2022 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2017-L2022)
- **Class:** [DatabaseTransaction](../DatabaseTransaction.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function __destruct()
```

## Documentation

_No docblock in source._

## Code

```php
  public function __destruct() {
    // If we rolled back then the transaction would have already been popped.
    if (!$this->rolledBack) {
      $this->connection->popTransaction($this->name);
    }
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
