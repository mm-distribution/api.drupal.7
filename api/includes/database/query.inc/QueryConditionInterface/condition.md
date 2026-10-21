# QueryConditionInterface::condition()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 46–46 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L46)
- **Class:** [QueryConditionInterface](../QueryConditionInterface.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function condition($field, $value = NULL, $operator = NULL);
```

## Documentation

```text
Helper function: builds the most common conditional clauses.

This method can take a variable number of parameters. If called with two
parameters, they are taken as $field and $value with $operator having a
value of IN if $value is an array and = otherwise.

Do not use this method to test for NULL values. Instead, use
QueryConditionInterface::isNull() or QueryConditionInterface::isNotNull().

@param $field
  The name of the field to check. If you would like to add a more complex
  condition involving operators or functions, use where().
@param $value
  The value to test the field against. In most cases, this is a scalar.
  For more complex options, it is an array. The meaning of each element in
  the array is dependent on the $operator.
@param $operator
  The comparison operator, such as =, <, or >=. It also accepts more
  complex options such as IN, LIKE, or BETWEEN. Defaults to IN if $value is
  an array, and = otherwise.

@return QueryConditionInterface
  The called object.

@see QueryConditionInterface::isNull()
@see QueryConditionInterface::isNotNull()
```

## Code

```php
  public function condition($field, $value = NULL, $operator = NULL);
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
