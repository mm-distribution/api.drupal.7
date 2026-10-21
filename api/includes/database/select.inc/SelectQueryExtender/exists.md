# SelectQueryExtender::exists()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 809–812 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L809-L812)
- **Class:** [SelectQueryExtender](../SelectQueryExtender.md)
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
    $this->query->exists($select);
    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
