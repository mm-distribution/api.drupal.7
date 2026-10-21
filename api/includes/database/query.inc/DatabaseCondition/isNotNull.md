# DatabaseCondition::isNotNull()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 1793–1795 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L1793-L1795)
- **Class:** [DatabaseCondition](../DatabaseCondition.md)
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
    return $this->condition($field, NULL, 'IS NOT NULL');
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
