# SelectQuery::arguments()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 1034–1068 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L1034-L1068)
- **Class:** [SelectQuery](../SelectQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function arguments()
```

## Documentation

_No docblock in source._

## Code

```php
  public function arguments() {
    if (!$this->compiled()) {
      return NULL;
    }

    $args = $this->where->arguments() + $this->having->arguments();

    foreach ($this->tables as $table) {
      if ($table['arguments']) {
        $args += $table['arguments'];
      }
      // If this table is a subquery, grab its arguments recursively.
      if ($table['table'] instanceof SelectQueryInterface) {
        $args += $table['table']->arguments();
      }
      // If the join condition is an object, grab its arguments recursively.
      if (!empty($table['condition']) && $table['condition'] instanceof QueryConditionInterface) {
        $args += $table['condition']->arguments();
      }
    }

    foreach ($this->expressions as $expression) {
      if ($expression['arguments']) {
        $args += $expression['arguments'];
      }
    }

    // If there are any dependent queries to UNION,
    // incorporate their arguments recursively.
    foreach ($this->union as $union) {
      $args += $union['query']->arguments();
    }

    return $args;
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
