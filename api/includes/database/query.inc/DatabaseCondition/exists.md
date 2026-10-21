# DatabaseCondition::exists()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 1800–1802 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L1800-L1802)
- **Class:** [DatabaseCondition](../DatabaseCondition.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function exists(SelectQueryInterface $select)
```

## Documentation

```text
Implements QueryConditionInterface::exists().
```

## Code

```php
  public function exists(SelectQueryInterface $select) {
    return $this->condition('', $select, 'EXISTS');
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
