# DatabaseConnection::utf8mb4IsActive()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 1403–1407 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L1403-L1407)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function utf8mb4IsActive()
```

## Documentation

```text
Checks whether utf8mb4 support is currently active.

@return bool
```

## Code

```php
  public function utf8mb4IsActive() {
    // Since 4 byte UTF-8 is not supported by default, there is nothing to
    // activate.
    return FALSE;
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
