# DatabaseConnection_sqlite::prepareQuery()

- **Type:** Method
- **File:** [`includes/database/sqlite/database.inc`](../_file.md), lines 301–303 · [local source](../../../../../../source/includes/database/sqlite/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/database.inc#L301-L303)
- **Class:** [DatabaseConnection_sqlite](../DatabaseConnection_sqlite.md)
- **Topics:** [database](../../../../../topics/database.md)

## Signature

```php
public function prepareQuery($query)
```

## Documentation

_No docblock in source._

## Code

```php
  public function prepareQuery($query) {
    return $this->prepare($this->prefixTables($query));
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
