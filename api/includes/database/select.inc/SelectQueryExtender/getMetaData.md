# SelectQueryExtender::getMetaData()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 608–610 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L608-L610)
- **Class:** [SelectQueryExtender](../SelectQueryExtender.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function getMetaData($key)
```

## Documentation

_No docblock in source._

## Code

```php
  public function getMetaData($key) {
    return $this->query->getMetaData($key);
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
