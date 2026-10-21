# SelectQuery::havingExists()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 1188–1191 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L1188-L1191)
- **Class:** [SelectQuery](../SelectQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function havingExists(SelectQueryInterface $select)
```

## Documentation

_No docblock in source._

## Code

```php
  public function havingExists(SelectQueryInterface $select) {
    $this->having->exists($select);
    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
