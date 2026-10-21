# SelectQueryExtender::union()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 780–783 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L780-L783)
- **Class:** [SelectQueryExtender](../SelectQueryExtender.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function union(SelectQueryInterface $query, $type = '')
```

## Documentation

_No docblock in source._

## Code

```php
  public function union(SelectQueryInterface $query, $type = '') {
    $this->query->union($query, $type);
    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
