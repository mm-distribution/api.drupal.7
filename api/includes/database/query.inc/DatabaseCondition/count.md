# DatabaseCondition::count()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 1739–1741 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L1739-L1741)
- **Class:** [DatabaseCondition](../DatabaseCondition.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function count()
```

## Documentation

_No docblock in source._

## Code

```php
  public function count() {
    return count($this->conditions) - 1;
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
