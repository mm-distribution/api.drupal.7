# QueryConditionInterface::notExists()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 104–104 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L104)
- **Class:** [QueryConditionInterface](../QueryConditionInterface.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function notExists(SelectQueryInterface $select);
```

## Documentation

```text
Sets a condition that the specified subquery returns no values.

@param SelectQueryInterface $select
  The subquery that must not contain results.

@return QueryConditionInterface
  The called object.
```

## Code

```php
  public function notExists(SelectQueryInterface $select);
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
