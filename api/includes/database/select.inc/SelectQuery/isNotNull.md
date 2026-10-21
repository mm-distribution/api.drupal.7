# SelectQuery::isNotNull()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 1080–1083 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L1080-L1083)
- **Class:** [SelectQuery](../SelectQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function isNotNull($field)
```

## Documentation

_No docblock in source._

## Code

```php
  public function isNotNull($field) {
    $this->where->isNotNull($field);
    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
