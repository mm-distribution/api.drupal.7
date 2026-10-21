# SelectQuery::havingCompile()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 1164–1166 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L1164-L1166)
- **Class:** [SelectQuery](../SelectQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function havingCompile(DatabaseConnection $connection)
```

## Documentation

_No docblock in source._

## Code

```php
  public function havingCompile(DatabaseConnection $connection) {
    return $this->having->compile($connection, $this);
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
