# SelectQuery::havingIsNull()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 1178–1181 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L1178-L1181)
- **Class:** [SelectQuery](../SelectQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function havingIsNull($field)
```

## Documentation

_No docblock in source._

## Code

```php
  public function havingIsNull($field) {
    $this->having->isNull($field);
    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
