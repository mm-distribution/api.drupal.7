# SelectQuery::havingConditions()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 1151–1153 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L1151-L1153)
- **Class:** [SelectQuery](../SelectQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function &havingConditions()
```

## Documentation

_No docblock in source._

## Code

```php
  public function &havingConditions() {
    return $this->having->conditions();
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
