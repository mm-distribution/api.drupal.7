# SelectQuery::isNull()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 1075–1078 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L1075-L1078)
- **Class:** [SelectQuery](../SelectQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function isNull($field)
```

## Documentation

_No docblock in source._

## Code

```php
  public function isNull($field) {
    $this->where->isNull($field);
    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
