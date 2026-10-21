# DatabaseConnection::utf8mb4IsSupported()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 1414–1418 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L1414-L1418)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function utf8mb4IsSupported()
```

## Documentation

```text
Checks whether utf8mb4 support is available on the current database system.

@return bool
```

## Code

```php
  public function utf8mb4IsSupported() {
    // By default we assume that the database backend may not support 4 byte
    // UTF-8.
    return FALSE;
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
