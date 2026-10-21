# DatabaseConnection_sqlite::utf8mb4IsSupported()

- **Type:** Method
- **File:** [`includes/database/sqlite/database.inc`](../_file.md), lines 412–414 · [local source](../../../../../../source/includes/database/sqlite/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/database.inc#L412-L414)
- **Class:** [DatabaseConnection_sqlite](../DatabaseConnection_sqlite.md)
- **Topics:** [database](../../../../../topics/database.md)

## Signature

```php
public function utf8mb4IsSupported()
```

## Documentation

_No docblock in source._

## Code

```php
  public function utf8mb4IsSupported() {
    return TRUE;
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
