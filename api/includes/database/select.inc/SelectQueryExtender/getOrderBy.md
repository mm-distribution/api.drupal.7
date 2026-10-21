# SelectQueryExtender::getOrderBy()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 683–685 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L683-L685)
- **Class:** [SelectQueryExtender](../SelectQueryExtender.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function &getOrderBy()
```

## Documentation

_No docblock in source._

## Code

```php
  public function &getOrderBy() {
    return $this->query->getOrderBy();
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
