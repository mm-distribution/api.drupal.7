# DatabaseCondition::notExists()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 1807–1809 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L1807-L1809)
- **Class:** [DatabaseCondition](../DatabaseCondition.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function notExists(SelectQueryInterface $select)
```

## Documentation

```text
Implements QueryConditionInterface::notExists().
```

## Code

```php
  public function notExists(SelectQueryInterface $select) {
    return $this->condition('', $select, 'NOT EXISTS');
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
