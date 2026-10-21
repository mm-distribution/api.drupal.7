# SelectQuery::notExists()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 1090–1093 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L1090-L1093)
- **Class:** [SelectQuery](../SelectQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function notExists(SelectQueryInterface $select)
```

## Documentation

_No docblock in source._

## Code

```php
  public function notExists(SelectQueryInterface $select) {
    $this->where->notExists($select);
    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
