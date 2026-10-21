# SelectQuery::addJoin()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 1400–1431 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L1400-L1431)
- **Class:** [SelectQuery](../SelectQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function addJoin($type, $table, $alias = NULL, $condition = NULL, $arguments = array())
```

## Documentation

_No docblock in source._

## Code

```php
  public function addJoin($type, $table, $alias = NULL, $condition = NULL, $arguments = array()) {

    if (empty($alias)) {
      if ($table instanceof SelectQueryInterface) {
        $alias = 'subquery';
      }
      else {
        $alias = $table;
      }
    }

    $alias_candidate = $alias;
    $count = 2;
    while (!empty($this->tables[$alias_candidate])) {
      $alias_candidate = $alias . '_' . $count++;
    }
    $alias = $alias_candidate;

    if (is_string($condition)) {
      $condition = str_replace('%alias', $alias, $condition);
    }

    $this->tables[$alias] = array(
      'join type' => $type,
      'table' => $table,
      'alias' => $alias,
      'condition' => $condition,
      'arguments' => $arguments,
    );

    return $alias;
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
