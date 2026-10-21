# SelectQuery::rightJoin()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 1396–1398 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L1396-L1398)
- **Class:** [SelectQuery](../SelectQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function rightJoin($table, $alias = NULL, $condition = NULL, $arguments = array())
```

## Documentation

_No docblock in source._

## Code

```php
  public function rightJoin($table, $alias = NULL, $condition = NULL, $arguments = array()) {
    return $this->addJoin('RIGHT OUTER', $table, $alias, $condition, $arguments);
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
