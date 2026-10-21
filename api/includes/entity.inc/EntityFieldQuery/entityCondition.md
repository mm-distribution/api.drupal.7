# EntityFieldQuery::entityCondition()

- **Type:** Method
- **File:** [`includes/entity.inc`](../_file.md), lines 672–683 · [local source](../../../../source/includes/entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc#L672-L683)
- **Class:** [EntityFieldQuery](../EntityFieldQuery.md)

## Signature

```php
public function entityCondition($name, $value, $operator = NULL)
```

## Documentation

```text
Adds a condition on entity-generic metadata.

If the overall query contains only entity conditions or ordering, or if
there are property conditions, then specifying the entity type is
mandatory. If there are field conditions or ordering but no property
conditions or ordering, then specifying an entity type is optional. While
the field storage engine might support field conditions on more than one
entity type, there is no way to query across multiple entity base tables by
default. To specify the entity type, pass in 'entity_type' for $name,
the type as a string for $value, and no $operator (it's disregarded).

'bundle', 'revision_id' and 'entity_id' have no such restrictions.

Note: The "comment" entity type does not support bundle conditions.

@param $name
  'entity_type', 'bundle', 'revision_id' or 'entity_id'.
@param $value
  The value for $name. In most cases, this is a scalar. For more complex
  options, it is an array. The meaning of each element in the array is
  dependent on $operator.
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
  public function entityCondition($name, $value, $operator = NULL) {
    // The '!=' operator is deprecated in favour of the '<>' operator since the
    // latter is ANSI SQL compatible.
    if ($operator == '!=') {
      $operator = '<>';
    }
    $this->entityConditions[$name] = array(
      'value' => $value,
      'operator' => $operator,
    );
    return $this;
  }
```

---
_Drupal 7.103 · [includes/entity.inc](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
