# QueryConditionInterface::compile()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 151–151 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L151)
- **Class:** [QueryConditionInterface](../QueryConditionInterface.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function compile(DatabaseConnection $connection, QueryPlaceholderInterface $queryPlaceholder);
```

## Documentation

```text
Compiles the saved conditions for later retrieval.

This method does not return anything, but simply prepares data to be
retrieved via __toString() and arguments().

@param $connection
  The database connection for which to compile the conditionals.
@param $queryPlaceholder
  The query this condition belongs to. If not given, the current query is
  used.
```

## Code

```php
  public function compile(DatabaseConnection $connection, QueryPlaceholderInterface $queryPlaceholder);
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
