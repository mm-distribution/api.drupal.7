# SelectQuery::havingNotExists()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 1193–1196 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L1193-L1196)
- **Class:** [SelectQuery](../SelectQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function havingNotExists(SelectQueryInterface $select)
```

## Documentation

_No docblock in source._

## Code

```php
  public function havingNotExists(SelectQueryInterface $select) {
    $this->having->notExists($select);
    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
