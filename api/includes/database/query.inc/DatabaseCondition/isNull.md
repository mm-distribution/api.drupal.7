# DatabaseCondition::isNull()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 1786–1788 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L1786-L1788)
- **Class:** [DatabaseCondition](../DatabaseCondition.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function isNull($field)
```

## Documentation

```text
Implements QueryConditionInterface::isNull().
```

## Code

```php
  public function isNull($field) {
    return $this->condition($field);
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
