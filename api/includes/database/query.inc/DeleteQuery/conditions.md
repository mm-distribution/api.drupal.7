# DeleteQuery::conditions()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 812–814 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L812-L814)
- **Class:** [DeleteQuery](../DeleteQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function &conditions()
```

## Documentation

```text
Implements QueryConditionInterface::conditions().
```

## Code

```php
  public function &conditions() {
    return $this->condition->conditions();
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
