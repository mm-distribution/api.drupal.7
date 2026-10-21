# SelectQueryExtender::havingConditions()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 647–649 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L647-L649)
- **Class:** [SelectQueryExtender](../SelectQueryExtender.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function &havingConditions()
```

## Documentation

_No docblock in source._

## Code

```php
  public function &havingConditions() {
    return $this->query->havingConditions();
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
