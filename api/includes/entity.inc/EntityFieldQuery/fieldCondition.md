# EntityFieldQuery::fieldCondition()

- **Type:** Method
- **File:** [`includes/entity.inc`](../_file.md), lines 734–736 · [local source](../../../../source/includes/entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc#L734-L736)
- **Class:** [EntityFieldQuery](../EntityFieldQuery.md)

## Signature

```php
public function fieldCondition($field, $column = NULL, $value = NULL, $operator = NULL, $delta_group = NULL, $language_group = NULL)
```

## Documentation

```text
Adds a condition on field values.

Note that entities with empty field values will be excluded from the
EntityFieldQuery results when using this method.

@param $field
  Either a field name or a field array.
@param $column
  The column that should hold the value to be matched, defined in the
  hook_field_schema() of this field. If this is omitted then all of the
  other parameters are ignored, except $field, and this call will just be
  adding a condition that says that the field has a value, rather than
  testing the value itself.
@param $value
  The value to test the column value against. In most cases, this is a
  scalar. For more complex options, it is an array. The meaning of each
  element in the array is dependent on $operator.
@param $operator
  The operator to be used to test the given value. The possible values are:
  - '=', '<>', '>', '>=', '<', '<=', 'STARTS_WITH', 'CONTAINS': These
    operators expect $value to be a literal of the same type as the
    column.
  - 'IN', 'NOT IN': These operators expect $value to be an array of
    literals of the same type as the column.
  - 'BETWEEN': This operator expects $value to be an array of two literals
    of the same type as the column.
  The operator can be omitted, and will default to 'IN' if the value is an
  array, or to '=' otherwise.
@param $delta_group
  An arbitrary identifier: conditions in the same group must have the same
  $delta_group. For example, let's presume a multivalue field which has
  two columns, 'color' and 'shape', and for entity ID 1, there are two
  values: red/square and blue/circle. Entity ID 1 does not have values
  corresponding to 'red circle'; however if you pass 'red' and 'circle' as
  conditions, it will appear in the results -- by default queries will run
  against any combination of deltas. By passing the conditions with the
  same $delta_group it will ensure that only values attached to the same
  delta are matched, and entity 1 would then be excluded from the results.
@param $language_group
  An arbitrary identifier: conditions in the same group must have the same
  $language_group.

@return EntityFieldQuery
  The called object.

@see EntityFieldQuery::addFieldCondition
@see EntityFieldQuery::deleted
```

## Code

```php
  public function fieldCondition($field, $column = NULL, $value = NULL, $operator = NULL, $delta_group = NULL, $language_group = NULL) {
    return $this->addFieldCondition($this->fieldConditions, $field, $column, $value, $operator, $delta_group, $language_group);
  }
```

---
_Drupal 7.103 · [includes/entity.inc](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
