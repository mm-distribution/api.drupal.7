# SelectQueryExtender::notExists()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 814–817 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L814-L817)
- **Class:** [SelectQueryExtender](../SelectQueryExtender.md)
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
    $this->query->notExists($select);
    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
