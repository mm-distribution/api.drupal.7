# SelectQueryExtender::addMetaData()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 603–606 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L603-L606)
- **Class:** [SelectQueryExtender](../SelectQueryExtender.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function addMetaData($key, $object)
```

## Documentation

_No docblock in source._

## Code

```php
  public function addMetaData($key, $object) {
    $this->query->addMetaData($key, $object);
    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
