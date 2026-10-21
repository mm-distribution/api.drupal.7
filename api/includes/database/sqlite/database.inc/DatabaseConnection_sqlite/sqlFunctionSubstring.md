# DatabaseConnection_sqlite::sqlFunctionSubstring()

- **Type:** Method
- **File:** [`includes/database/sqlite/database.inc`](../_file.md), lines 209–211 · [local source](../../../../../../source/includes/database/sqlite/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/database.inc#L209-L211)
- **Class:** [DatabaseConnection_sqlite](../DatabaseConnection_sqlite.md)
- **Topics:** [database](../../../../../topics/database.md)

## Signature

```php
public function sqlFunctionSubstring($string, $from, $length)
```

## Documentation

```text
SQLite compatibility implementation for the SUBSTRING() SQL function.
```

## Code

```php
  public function sqlFunctionSubstring($string, $from, $length) {
    return substr($string, $from - 1, $length);
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
