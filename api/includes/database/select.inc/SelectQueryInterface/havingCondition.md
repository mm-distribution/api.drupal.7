# SelectQueryInterface::havingCondition()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 505–505 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L505)
- **Class:** [SelectQueryInterface](../SelectQueryInterface.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function havingCondition($field, $value = NULL, $operator = NULL);
```

## Documentation

```text
Helper function to build most common HAVING conditional clauses.

This method can take a variable number of parameters. If called with two
parameters, they are taken as $field and $value with $operator having a value
of IN if $value is an array and = otherwise.

@param $field
  The name of the field to check. If you would like to add a more complex
  condition involving operators or functions, use having().
@param $value
  The value to test the field against. In most cases, this is a scalar. For more
  complex options, it is an array. The meaning of each element in the array is
  dependent on the $operator.
@param $operator
  The comparison operator, such as =, <, or >=. It also accepts more complex
  options such as IN, LIKE, or BETWEEN. Defaults to IN if $value is an array
  = otherwise.
@return QueryConditionInterface
  The called object.
```

## Code

```php
  public function havingCondition($field, $value = NULL, $operator = NULL);
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
