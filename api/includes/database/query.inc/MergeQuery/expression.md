# MergeQuery::expression()

- **Type:** Method
- **File:** [`includes/database/query.inc`](../_file.md), lines 1428–1435 · [local source](../../../../../source/includes/database/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc#L1428-L1435)
- **Class:** [MergeQuery](../MergeQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function expression($field, $expression, array $arguments = NULL)
```

## Documentation

```text
Specifies fields to be updated as an expression.

Expression fields are cases such as counter = counter + 1. This method
takes precedence over MergeQuery::updateFields() and it's wrappers,
MergeQuery::key() and MergeQuery::fields().

@param $field
  The field to set.
@param $expression
  The field will be set to the value of this expression. This parameter
  may include named placeholders.
@param $arguments
  If specified, this is an array of key/value pairs for named placeholders
  corresponding to the expression.

@return MergeQuery
  The called object.
```

## Code

```php
  public function expression($field, $expression, array $arguments = NULL) {
    $this->expressionFields[$field] = array(
      'expression' => $expression,
      'arguments' => $arguments,
    );
    $this->needsUpdate = TRUE;
    return $this;
  }
```

---
_Drupal 7.103 · [includes/database/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
