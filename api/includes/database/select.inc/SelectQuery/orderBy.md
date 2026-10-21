# SelectQuery::orderBy()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 1433–1438 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L1433-L1438)
- **Class:** [SelectQuery](../SelectQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function orderBy($field, $direction = 'ASC')
```

## Documentation

_No docblock in source._

## Code

```php
  public function orderBy($field, $direction = 'ASC') {
    // Only allow ASC and DESC, default to ASC.
    $direction = strtoupper($direction) == 'DESC' ? 'DESC' : 'ASC';
    $this->order[$field] = $direction;
    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
