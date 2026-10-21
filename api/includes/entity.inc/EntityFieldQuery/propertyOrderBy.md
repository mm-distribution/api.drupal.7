# EntityFieldQuery::propertyOrderBy()

- **Type:** Method
- **File:** [`includes/entity.inc`](../_file.md), lines 994–1001 · [local source](../../../../source/includes/entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc#L994-L1001)
- **Class:** [EntityFieldQuery](../EntityFieldQuery.md)

## Signature

```php
public function propertyOrderBy($column, $direction = 'ASC')
```

## Documentation

```text
Orders the result set by an entity-specific property.

An $entity_type must be specified by calling
EntityFieldCondition::entityCondition('entity_type', $entity_type) before
executing the query.

If called multiple times, the query will order by each specified column in
the order this method is called.

@param $column
  The column on which to order.
@param $direction
  The direction to sort. Legal values are "ASC" and "DESC".

@return EntityFieldQuery
  The called object.
```

## Code

```php
  public function propertyOrderBy($column, $direction = 'ASC') {
    $this->order[] = array(
      'type' => 'property',
      'specifier' => $column,
      'direction' => $direction,
    );
    return $this;
  }
```

---
_Drupal 7.103 · [includes/entity.inc](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
