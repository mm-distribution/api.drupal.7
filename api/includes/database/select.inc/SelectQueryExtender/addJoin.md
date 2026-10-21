# SelectQueryExtender::addJoin()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 761–763 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L761-L763)
- **Class:** [SelectQueryExtender](../SelectQueryExtender.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function addJoin($type, $table, $alias = NULL, $condition = NULL, $arguments = array())
```

## Documentation

_No docblock in source._

## Code

```php
  public function addJoin($type, $table, $alias = NULL, $condition = NULL, $arguments = array()) {
    return $this->query->addJoin($type, $table, $alias, $condition, $arguments);
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
