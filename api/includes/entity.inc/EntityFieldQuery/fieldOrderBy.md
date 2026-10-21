# EntityFieldQuery::fieldOrderBy()

- **Type:** Method
- **File:** [`includes/entity.inc`](../_file.md), lines 953–974 · [local source](../../../../source/includes/entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc#L953-L974)
- **Class:** [EntityFieldQuery](../EntityFieldQuery.md)

## Signature

```php
public function fieldOrderBy($field, $column, $direction = 'ASC')
```

## Documentation

```text
Orders the result set by a given field column.

If called multiple times, the query will order by each specified column in
the order this method is called. Note that entities with empty field
values will be excluded from the EntityFieldQuery results when using this
method.

@param $field
  Either a field name or a field array.
@param $column
  A column defined in the hook_field_schema() of this field. entity_id and
  bundle can also be used.
@param $direction
  The direction to sort. Legal values are "ASC" and "DESC".

@return EntityFieldQuery
  The called object.
```

## Code

```php
  public function fieldOrderBy($field, $column, $direction = 'ASC') {
    if (is_scalar($field)) {
      $field_definition = field_info_field($field);
      if (empty($field_definition)) {
        throw new EntityFieldQueryException(t('Unknown field: @field_name', array('@field_name' => $field)));
      }
      $field = $field_definition;
    }
    // Save the index used for the new field, for later use in field storage.
    $index = count($this->fields);
    $this->fields[$index] = $field;
    $this->order[] = array(
      'type' => 'field',
      'specifier' => array(
        'field' => $field,
        'index' => $index,
        'column' => $column,
      ),
      'direction' => $direction,
    );
    return $this;
  }
```

---
_Drupal 7.103 · [includes/entity.inc](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
