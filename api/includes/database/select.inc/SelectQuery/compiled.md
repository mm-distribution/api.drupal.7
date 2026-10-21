# SelectQuery::compiled()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 1116–1142 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L1116-L1142)
- **Class:** [SelectQuery](../SelectQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function compiled()
```

## Documentation

_No docblock in source._

## Code

```php
  public function compiled() {
    if (!$this->where->compiled() || !$this->having->compiled()) {
      return FALSE;
    }

    foreach ($this->tables as $table) {
      // If this table is a subquery, check its status recursively.
      if ($table['table'] instanceof SelectQueryInterface) {
        if (!$table['table']->compiled()) {
          return FALSE;
        }
      }
      if (!empty($table['condition']) && $table['condition'] instanceof QueryConditionInterface) {
        if (!$table['condition']->compiled()) {
          return FALSE;
        }
      }
    }

    foreach ($this->union as $union) {
      if (!$union['query']->compiled()) {
        return FALSE;
      }
    }

    return TRUE;
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
