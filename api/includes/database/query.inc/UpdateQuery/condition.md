# UpdateQuery::condition()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 1037–1040 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L1037-L1040)
- **Class:** [UpdateQuery](../UpdateQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function condition($field, $value = NULL, $operator = NULL)
```

## Documentation

```text
Implements QueryConditionInterface::condition().
```

## Code

```php
  public function condition($field, $value = NULL, $operator = NULL) {
    $this->condition->condition($field, $value, $operator);
    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
