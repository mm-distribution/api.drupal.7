# QueryConditionInterface::isNull()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 71–71 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L71)
- **Class:** [QueryConditionInterface](../QueryConditionInterface.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function isNull($field);
```

## Documentation

```text
Sets a condition that the specified field be NULL.

@param $field
  The name of the field to check.

@return QueryConditionInterface
  The called object.
```

## Code

```php
  public function isNull($field);
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
