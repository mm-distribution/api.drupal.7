# SelectQuery::addExpression()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 1363–1382 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L1363-L1382)
- **Class:** [SelectQuery](../SelectQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function addExpression($expression, $alias = NULL, $arguments = array())
```

## Documentation

_No docblock in source._

## Code

```php
  public function addExpression($expression, $alias = NULL, $arguments = array()) {
    if (empty($alias)) {
      $alias = 'expression';
    }

    $alias_candidate = $alias;
    $count = 2;
    while (!empty($this->expressions[$alias_candidate])) {
      $alias_candidate = $alias . '_' . $count++;
    }
    $alias = $alias_candidate;

    $this->expressions[$alias] = array(
      'expression' => $expression,
      'alias' => $alias,
      'arguments' => $arguments,
    );

    return $alias;
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
