# SelectQueryExtender::isPrepared()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 703–705 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L703-L705)
- **Class:** [SelectQueryExtender](../SelectQueryExtender.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function isPrepared()
```

## Documentation

_No docblock in source._

## Code

```php
  public function isPrepared() {
    return $this->query->isPrepared();
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
