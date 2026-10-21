# SelectQuery::conditions()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 1030–1032 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L1030-L1032)
- **Class:** [SelectQuery](../SelectQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function &conditions()
```

## Documentation

_No docblock in source._

## Code

```php
  public function &conditions() {
    return $this->where->conditions();
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
