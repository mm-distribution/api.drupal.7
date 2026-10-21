# SelectQuery::addMetaData()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 1014–1017 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L1014-L1017)
- **Class:** [SelectQuery](../SelectQuery.md)
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
    $this->alterMetaData[$key] = $object;
    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
