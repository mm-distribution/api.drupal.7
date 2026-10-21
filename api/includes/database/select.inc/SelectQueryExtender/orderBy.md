# SelectQueryExtender::orderBy()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 765–768 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L765-L768)
- **Class:** [SelectQueryExtender](../SelectQueryExtender.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function orderBy($field, $direction = 'ASC')
```

## Documentation

_No docblock in source._

## Code

```php
  public function orderBy($field, $direction = 'ASC') {
    $this->query->orderBy($field, $direction);
    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
