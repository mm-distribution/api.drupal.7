# UpdateQuery::exists()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 1061–1064 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L1061-L1064)
- **Class:** [UpdateQuery](../UpdateQuery.md)
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
    $this->condition->exists($select);
    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
