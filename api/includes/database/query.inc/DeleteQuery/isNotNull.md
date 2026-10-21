# DeleteQuery::isNotNull()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 788–791 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L788-L791)
- **Class:** [DeleteQuery](../DeleteQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function isNotNull($field)
```

## Documentation

```text
Implements QueryConditionInterface::isNotNull().
```

## Code

```php
  public function isNotNull($field) {
    $this->condition->isNotNull($field);
    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
