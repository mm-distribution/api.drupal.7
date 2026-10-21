# SelectQuery::leftJoin()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 1392–1394 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L1392-L1394)
- **Class:** [SelectQuery](../SelectQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function leftJoin($table, $alias = NULL, $condition = NULL, $arguments = array())
```

## Documentation

_No docblock in source._

## Code

```php
  public function leftJoin($table, $alias = NULL, $condition = NULL, $arguments = array()) {
    return $this->addJoin('LEFT OUTER', $table, $alias, $condition, $arguments);
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
