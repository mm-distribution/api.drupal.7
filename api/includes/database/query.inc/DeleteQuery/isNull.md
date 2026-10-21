# DeleteQuery::isNull()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 780–783 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L780-L783)
- **Class:** [DeleteQuery](../DeleteQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function isNull($field)
```

## Documentation

```text
Implements QueryConditionInterface::isNull().
```

## Code

```php
  public function isNull($field) {
    $this->condition->isNull($field);
    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
