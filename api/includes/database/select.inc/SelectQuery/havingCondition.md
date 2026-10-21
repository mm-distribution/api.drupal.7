# SelectQuery::havingCondition()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 1146–1149 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L1146-L1149)
- **Class:** [SelectQuery](../SelectQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function havingCondition($field, $value = NULL, $operator = NULL)
```

## Documentation

_No docblock in source._

## Code

```php
  public function havingCondition($field, $value = NULL, $operator = NULL) {
    $this->having->condition($field, $value, $operator);
    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
