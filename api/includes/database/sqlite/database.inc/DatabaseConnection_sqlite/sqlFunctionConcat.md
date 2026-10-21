# DatabaseConnection_sqlite::sqlFunctionConcat()

- **Type:** Method
- **File:** [`includes/database/sqlite/database.inc`](../_file.md), lines 201–204 · [local source](../../../../../../source/includes/database/sqlite/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/database.inc#L201-L204)
- **Class:** [DatabaseConnection_sqlite](../DatabaseConnection_sqlite.md)
- **Topics:** [database](../../../../../topics/database.md)

## Signature

```php
public function sqlFunctionConcat()
```

## Documentation

```text
SQLite compatibility implementation for the CONCAT() SQL function.
```

## Code

```php
  public function sqlFunctionConcat() {
    $args = func_get_args();
    return implode('', $args);
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
