# SelectQuery::condition()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 1025–1028 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L1025-L1028)
- **Class:** [SelectQuery](../SelectQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function condition($field, $value = NULL, $operator = NULL)
```

## Documentation

_No docblock in source._

## Code

```php
  public function condition($field, $value = NULL, $operator = NULL) {
    $this->where->condition($field, $value, $operator);
    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
