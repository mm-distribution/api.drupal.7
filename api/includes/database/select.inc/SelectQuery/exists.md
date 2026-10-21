# SelectQuery::exists()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 1085–1088 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L1085-L1088)
- **Class:** [SelectQuery](../SelectQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function exists(SelectQueryInterface $select)
```

## Documentation

_No docblock in source._

## Code

```php
  public function exists(SelectQueryInterface $select) {
    $this->where->exists($select);
    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
