# EntityFieldQuery::entityOrderBy()

- **Type:** Method
- **File:** [`includes/entity.inc`](../_file.md), lines 925–932 · [local source](../../../../source/includes/entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc#L925-L932)
- **Class:** [EntityFieldQuery](../EntityFieldQuery.md)

## Signature

```php
public function entityOrderBy($name, $direction = 'ASC')
```

## Documentation

```text
Orders the result set by entity-generic metadata.

If called multiple times, the query will order by each specified column in
the order this method is called.

Note: The "comment" and "taxonomy_term" entity types don't support ordering
by bundle. For "taxonomy_term", propertyOrderBy('vid') can be used instead.

@param $name
  'entity_type', 'bundle', 'revision_id' or 'entity_id'.
@param $direction
  The direction to sort. Legal values are "ASC" and "DESC".

@return EntityFieldQuery
  The called object.
```

## Code

```php
  public function entityOrderBy($name, $direction = 'ASC') {
    $this->order[] = array(
      'type' => 'entity',
      'specifier' => $name,
      'direction' => $direction,
    );
    return $this;
  }
```

---
_Drupal 7.103 · [includes/entity.inc](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
