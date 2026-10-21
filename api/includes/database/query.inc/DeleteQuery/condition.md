# DeleteQuery::condition()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 772–775 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L772-L775)
- **Class:** [DeleteQuery](../DeleteQuery.md)
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
