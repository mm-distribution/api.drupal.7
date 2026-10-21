# DatabaseConnection_sqlite::sqlFunctionIf()

- **Type:** Method
- **File:** [`includes/database/sqlite/database.inc`](../_file.md), lines 176–178 · [local source](../../../../../../source/includes/database/sqlite/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/database.inc#L176-L178)
- **Class:** [DatabaseConnection_sqlite](../DatabaseConnection_sqlite.md)
- **Topics:** [database](../../../../../topics/database.md)

## Signature

```php
public function sqlFunctionIf($condition, $expr1, $expr2 = NULL)
```

## Documentation

```text
SQLite compatibility implementation for the IF() SQL function.
```

## Code

```php
  public function sqlFunctionIf($condition, $expr1, $expr2 = NULL) {
    return $condition ? $expr1 : $expr2;
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
