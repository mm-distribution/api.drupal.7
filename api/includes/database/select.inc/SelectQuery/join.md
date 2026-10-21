# SelectQuery::join()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 1384–1386 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L1384-L1386)
- **Class:** [SelectQuery](../SelectQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function join($table, $alias = NULL, $condition = NULL, $arguments = array())
```

## Documentation

_No docblock in source._

## Code

```php
  public function join($table, $alias = NULL, $condition = NULL, $arguments = array()) {
    return $this->addJoin('INNER', $table, $alias, $condition, $arguments);
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
