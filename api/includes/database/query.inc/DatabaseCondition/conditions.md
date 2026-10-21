# DatabaseCondition::conditions()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 1814–1816 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L1814-L1816)
- **Class:** [DatabaseCondition](../DatabaseCondition.md)
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
    return $this->conditions;
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
