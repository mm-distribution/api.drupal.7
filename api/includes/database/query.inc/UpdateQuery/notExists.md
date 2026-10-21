# UpdateQuery::notExists()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 1069–1072 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L1069-L1072)
- **Class:** [UpdateQuery](../UpdateQuery.md)
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
    $this->condition->notExists($select);
    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
