# DatabaseConnection_pgsql::utf8mb4IsActive()

- **Type:** Method
- **File:** [`includes/database/pgsql/database.inc`](../_file.md), lines 221–223 · [local source](../../../../../../source/includes/database/pgsql/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/database.inc#L221-L223)
- **Class:** [DatabaseConnection_pgsql](../DatabaseConnection_pgsql.md)
- **Topics:** [database](../../../../../topics/database.md)

## Signature

```php
public function utf8mb4IsActive()
```

## Documentation

_No docblock in source._

## Code

```php
  public function utf8mb4IsActive() {
    return TRUE;
  }
```

---
_Drupal 7.103 · [includes/database/pgsql/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
