# DatabaseConnection_mysql::__destruct()

- **Type:** Method
- **File:** [`includes/database/mysql/database.inc`](../_file.md), lines 461–465 · [local source](../../../../../../source/includes/database/mysql/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/database.inc#L461-L465)
- **Class:** [DatabaseConnection_mysql](../DatabaseConnection_mysql.md)
- **Topics:** [database](../../../../../topics/database.md)

## Signature

```php
public function __destruct()
```

## Documentation

_No docblock in source._

## Code

```php
  public function __destruct() {
    if ($this->needsCleanup) {
      $this->nextIdDelete();
    }
  }
```

---
_Drupal 7.103 · [includes/database/mysql/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
