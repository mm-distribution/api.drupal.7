# SelectQuery::forUpdate()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 1198–1203 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L1198-L1203)
- **Class:** [SelectQuery](../SelectQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function forUpdate($set = TRUE)
```

## Documentation

_No docblock in source._

## Code

```php
  public function forUpdate($set = TRUE) {
    if (isset($set)) {
      $this->forUpdate = $set;
    }
    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
