# EntityFieldQuery::propertyCondition()

- **Type:** Method
- **File:** [`includes/entity.inc`](../_file.md), lines 894–906 · [local source](../../../../source/includes/entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc#L894-L906)
- **Class:** [EntityFieldQuery](../EntityFieldQuery.md)

## Signature

```php
public function propertyCondition($column, $value, $operator = NULL)
```

## Documentation

```text
Adds a condition on an entity-specific property.

An $entity_type must be specified by calling
EntityFieldCondition::entityCondition('entity_type', $entity_type) before
executing the query. Also, by default only entities stored in SQL are
supported; however, EntityFieldQuery::executeCallback can be set to handle
different entity storage.

@param $column
  A column defined in the hook_schema() of the base table of the entity.
@param $value
  The value to test the field against. In most cases, this is a scalar. For
  more complex options, it is an array. The meaning of each element in the
  array is dependent on $operator.
@param $operator
  Possible values:
  - '=', '<>', '>', '>=', '<', '<=', 'STARTS_WITH', 'CONTAINS': These
    operators expect $value to be a literal of the same type as the
    column.
  - 'IN', 'NOT IN': These operators expect $value to be an array of
    literals of the same type as the column.
  - 'BETWEEN': This operator expects $value to be an array of two literals
    of the same type as the column.
  The operator can be omitted, and will default to 'IN' if the value is an
  array, or to '=' otherwise.

@return EntityFieldQuery
  The called object.
```

## Code

```php
  public function propertyCondition($column, $value, $operator = NULL) {
    // The '!=' operator is deprecated in favour of the '<>' operator since the
    // latter is ANSI SQL compatible.
    if ($operator == '!=') {
      $operator = '<>';
    }
    $this->propertyConditions[] = array(
      'column' => $column,
      'value' => $value,
      'operator' => $operator,
    );
    return $this;
  }
```

---
_Drupal 7.103 · [includes/entity.inc](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
