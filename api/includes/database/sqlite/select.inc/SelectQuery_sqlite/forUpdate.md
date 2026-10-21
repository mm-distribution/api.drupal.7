# SelectQuery_sqlite::forUpdate()

- **Type:** Method
- **File:** [`includes/database/sqlite/select.inc`](../_file.md), lines 17–20 · [local source](../../../../../../source/includes/database/sqlite/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/select.inc#L17-L20)
- **Class:** [SelectQuery_sqlite](../SelectQuery_sqlite.md)
- **Topics:** [database](../../../../../topics/database.md)

## Signature

```php
public function forUpdate($set = TRUE)
```

## Documentation

_No docblock in source._

## Code

```php
  public function forUpdate($set = TRUE) {
    // SQLite does not support FOR UPDATE so nothing to do.
    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
