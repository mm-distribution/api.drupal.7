# SelectQueryInterface::forUpdate()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 530–530 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L530)
- **Class:** [SelectQueryInterface](../SelectQueryInterface.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function forUpdate($set = TRUE);
```

## Documentation

```text
Add FOR UPDATE to the query.

FOR UPDATE prevents the rows retrieved by the SELECT statement from being
modified or deleted by other transactions until the current transaction
ends. Other transactions that attempt UPDATE, DELETE, or SELECT FOR UPDATE
of these rows will be blocked until the current transaction ends.

@param $set
  IF TRUE, FOR UPDATE will be added to the query, if FALSE then it won't.

@return QueryConditionInterface
  The called object.
```

## Code

```php
  public function forUpdate($set = TRUE);
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
