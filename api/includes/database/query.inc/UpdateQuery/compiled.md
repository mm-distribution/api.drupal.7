# UpdateQuery::compiled()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 1106–1108 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L1106-L1108)
- **Class:** [UpdateQuery](../UpdateQuery.md)
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
    return $this->condition->compiled();
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
