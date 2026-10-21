# SelectQuery::getUnion()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 1227–1229 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L1227-L1229)
- **Class:** [SelectQuery](../SelectQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function &getUnion()
```

## Documentation

_No docblock in source._

## Code

```php
  public function &getUnion() {
    return $this->union;
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
