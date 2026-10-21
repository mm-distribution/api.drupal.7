# QueryConditionInterface::isNotNull()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 82–82 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L82)
- **Class:** [QueryConditionInterface](../QueryConditionInterface.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function isNotNull($field);
```

## Documentation

```text
Sets a condition that the specified field be NOT NULL.

@param $field
  The name of the field to check.

@return QueryConditionInterface
  The called object.
```

## Code

```php
  public function isNotNull($field);
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
