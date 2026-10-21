# DatabaseConnection_pgsql::mapConditionOperator()

- **Type:** Method
- **File:** [`includes/database/pgsql/database.inc`](../_file.md), lines 162–176 · [local source](../../../../../../source/includes/database/pgsql/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/database.inc#L162-L176)
- **Class:** [DatabaseConnection_pgsql](../DatabaseConnection_pgsql.md)
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
    static $specials;

    // Function calls not allowed in static declarations, thus this method.
    if (!isset($specials)) {
      $specials = array(
        // In PostgreSQL, 'LIKE' is case-sensitive. For case-insensitive LIKE
        // statements, we need to use ILIKE instead.
        'LIKE' => array('operator' => 'ILIKE'),
        'NOT LIKE' => array('operator' => 'NOT ILIKE'),
      );
    }

    return isset($specials[$operator]) ? $specials[$operator] : NULL;
  }
```

---
_Drupal 7.103 · [includes/database/pgsql/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
