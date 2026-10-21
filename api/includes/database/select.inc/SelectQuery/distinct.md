# SelectQuery::distinct()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 1314–1317 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L1314-L1317)
- **Class:** [SelectQuery](../SelectQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function distinct($distinct = TRUE)
```

## Documentation

_No docblock in source._

## Code

```php
  public function distinct($distinct = TRUE) {
    $this->distinct = $distinct;
    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
