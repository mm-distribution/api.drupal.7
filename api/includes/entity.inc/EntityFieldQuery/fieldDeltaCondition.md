# EntityFieldQuery::fieldDeltaCondition()

- **Type:** Method
- **File:** [`includes/entity.inc`](../_file.md), lines 786–788 · [local source](../../../../source/includes/entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc#L786-L788)
- **Class:** [EntityFieldQuery](../EntityFieldQuery.md)

## Signature

```php
public function fieldDeltaCondition($field, $value = NULL, $operator = NULL, $delta_group = NULL, $language_group = NULL)
```

## Documentation

```text
Adds a condition on the field delta column.

@param $field
  Either a field name or a field array.
@param $value
  The value to test the column value against.
@param $operator
  The operator to be used to test the given value.
@param $delta_group
  An arbitrary identifier: conditions in the same group must have the same
  $delta_group.
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
  public function fieldDeltaCondition($field, $value = NULL, $operator = NULL, $delta_group = NULL, $language_group = NULL) {
    return $this->addFieldCondition($this->fieldMetaConditions, $field, 'delta', $value, $operator, $delta_group, $language_group);
  }
```

---
_Drupal 7.103 · [includes/entity.inc](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
