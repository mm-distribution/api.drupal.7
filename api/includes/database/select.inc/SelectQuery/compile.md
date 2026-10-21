# SelectQuery::compile()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 1095–1114 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L1095-L1114)
- **Class:** [SelectQuery](../SelectQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function compile(DatabaseConnection $connection, QueryPlaceholderInterface $queryPlaceholder)
```

## Documentation

_No docblock in source._

## Code

```php
  public function compile(DatabaseConnection $connection, QueryPlaceholderInterface $queryPlaceholder) {
    $this->where->compile($connection, $queryPlaceholder);
    $this->having->compile($connection, $queryPlaceholder);

    foreach ($this->tables as $table) {
      // If this table is a subquery, compile it recursively.
      if ($table['table'] instanceof SelectQueryInterface) {
        $table['table']->compile($connection, $queryPlaceholder);
      }
      // Make sure join conditions are also compiled.
      if (!empty($table['condition']) && $table['condition'] instanceof QueryConditionInterface) {
        $table['condition']->compile($connection, $queryPlaceholder);
      }
    }

    // If there are any dependent queries to UNION, compile it recursively.
    foreach ($this->union as $union) {
      $union['query']->compile($connection, $queryPlaceholder);
    }
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
