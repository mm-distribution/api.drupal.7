# UpdateQuery::isNotNull()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 1053–1056 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L1053-L1056)
- **Class:** [UpdateQuery](../UpdateQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function isNotNull($field)
```

## Documentation

```text
Implements QueryConditionInterface::isNotNull().
```

## Code

```php
  public function isNotNull($field) {
    $this->condition->isNotNull($field);
    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
