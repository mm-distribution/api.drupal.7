# DatabaseCondition::compiled()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 1920–1922 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L1920-L1922)
- **Class:** [DatabaseCondition](../DatabaseCondition.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function compiled()
```

## Documentation

```text
Implements QueryConditionInterface::compiled().
```

## Code

```php
  public function compiled() {
    return !$this->changed;
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
