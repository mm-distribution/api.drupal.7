# SelectQueryInterface::leftJoin()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 308–308 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L308)
- **Class:** [SelectQueryInterface](../SelectQueryInterface.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function leftJoin($table, $alias = NULL, $condition = NULL, $arguments = array());
```

## Documentation

```text
Left Outer Join against another table in the database.

@param $table
  The table against which to join.
@param $alias
  The alias for the table. In most cases this should be the first letter
  of the table, or the first letter of each "word" in the table.
@param $condition
  The condition on which to join this table. If the join requires values,
  this clause should use a named placeholder and the value or values to
  insert should be passed in the 4th parameter. For the first table joined
  on a query, this value is ignored as the first table is taken as the base
  table. The token %alias can be used in this string to be replaced with
  the actual alias. This is useful when $alias is modified by the database
  system, for example, when joining the same table more than once.
@param $arguments
  An array of arguments to replace into the $condition of this join.
@return
  The unique alias that was assigned for this table.
```

## Code

```php
  public function leftJoin($table, $alias = NULL, $condition = NULL, $arguments = array());
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
