# DatabaseConnection_mysql::utf8mb4IsActive()

- **Type:** Method
- **File:** [`includes/database/mysql/database.inc`](../_file.md), lines 630–632 · [local source](../../../../../../source/includes/database/mysql/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/database.inc#L630-L632)
- **Class:** [DatabaseConnection_mysql](../DatabaseConnection_mysql.md)
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
    return isset($this->connectionOptions['charset']) && $this->connectionOptions['charset'] === 'utf8mb4';
  }
```

---
_Drupal 7.103 · [includes/database/mysql/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
