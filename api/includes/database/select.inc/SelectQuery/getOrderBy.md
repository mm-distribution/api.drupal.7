# SelectQuery::getOrderBy()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 1215–1217 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L1215-L1217)
- **Class:** [SelectQuery](../SelectQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function &getOrderBy()
```

## Documentation

_No docblock in source._

## Code

```php
  public function &getOrderBy() {
    return $this->order;
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
