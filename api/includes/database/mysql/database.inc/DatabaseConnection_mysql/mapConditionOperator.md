# DatabaseConnection_mysql::mapConditionOperator()

- **Type:** Method
- **File:** [`includes/database/mysql/database.inc`](../_file.md), lines 485–488 · [local source](../../../../../../source/includes/database/mysql/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/database.inc#L485-L488)
- **Class:** [DatabaseConnection_mysql](../DatabaseConnection_mysql.md)
- **Topics:** [database](../../../../../topics/database.md)

## Signature

```php
public function mapConditionOperator($operator)
```

## Documentation

_No docblock in source._

## Code

```php
  public function mapConditionOperator($operator) {
    // We don't want to override any of the defaults.
    return NULL;
  }
```

---
_Drupal 7.103 · [includes/database/mysql/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/mysql/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
