# DeleteQuery::compile()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 834–836 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L834-L836)
- **Class:** [DeleteQuery](../DeleteQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function compile(DatabaseConnection $connection, QueryPlaceholderInterface $queryPlaceholder)
```

## Documentation

```text
Implements QueryConditionInterface::compile().
```

## Code

```php
  public function compile(DatabaseConnection $connection, QueryPlaceholderInterface $queryPlaceholder) {
    return $this->condition->compile($connection, $queryPlaceholder);
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
