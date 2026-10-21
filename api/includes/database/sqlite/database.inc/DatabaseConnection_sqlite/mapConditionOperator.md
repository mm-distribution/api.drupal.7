# DatabaseConnection_sqlite::mapConditionOperator()

- **Type:** Method
- **File:** [`includes/database/sqlite/database.inc`](../_file.md), lines 292–299 · [local source](../../../../../../source/includes/database/sqlite/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/database.inc#L292-L299)
- **Class:** [DatabaseConnection_sqlite](../DatabaseConnection_sqlite.md)
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
    static $specials = array(
      'LIKE' => array('postfix' => " ESCAPE '\\'"),
      'NOT LIKE' => array('postfix' => " ESCAPE '\\'"),
    );
    return isset($specials[$operator]) ? $specials[$operator] : NULL;
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
