# DatabaseConnection_pgsql::queryRange()

- **Type:** Method
- **File:** [`includes/database/pgsql/database.inc`](../_file.md), lines 144–146 · [local source](../../../../../../source/includes/database/pgsql/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/database.inc#L144-L146)
- **Class:** [DatabaseConnection_pgsql](../DatabaseConnection_pgsql.md)
- **Topics:** [database](../../../../../topics/database.md)

## Signature

```php
public function queryRange($query, $from, $count, array $args = array(), array $options = array())
```

## Documentation

_No docblock in source._

## Code

```php
  public function queryRange($query, $from, $count, array $args = array(), array $options = array()) {
    return $this->query($query . ' LIMIT ' . (int) $count . ' OFFSET ' . (int) $from, $args, $options);
  }
```

---
_Drupal 7.103 · [includes/database/pgsql/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/pgsql/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
