# MergeQuery::conditionTable()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 1388–1391 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L1388-L1391)
- **Class:** [MergeQuery](../MergeQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
protected function conditionTable($table)
```

## Documentation

```text
Sets the table or subquery to be used for the condition.

@param $table
  The table name or the subquery to be used. Use a SelectQuery object to
  pass in a subquery.

@return MergeQuery
  The called object.
```

## Code

```php
  protected function conditionTable($table) {
    $this->conditionTable = $table;
    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
