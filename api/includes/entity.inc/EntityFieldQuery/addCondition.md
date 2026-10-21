# EntityFieldQuery::addCondition()

- **Type:** Method
- **File:** [`includes/entity.inc`](../_file.md), lines 1420–1432 · [local source](../../../../source/includes/entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc#L1420-L1432)
- **Class:** [EntityFieldQuery](../EntityFieldQuery.md)

## Signature

```php
public function addCondition(SelectQuery $select_query, $sql_field, $condition, $having = FALSE)
```

## Documentation

```text
Adds a condition to an already built SelectQuery (internal function).

This is a helper for hook_entity_query() and hook_field_storage_query().

@param SelectQuery $select_query
  A SelectQuery object.
@param $sql_field
  The name of the field.
@param $condition
  A condition as described in EntityFieldQuery::fieldCondition() and
  EntityFieldQuery::entityCondition().
@param $having
  HAVING or WHERE. This is necessary because SQL can't handle WHERE
  conditions on aliased columns.
```

## Code

```php
  public function addCondition(SelectQuery $select_query, $sql_field, $condition, $having = FALSE) {
    $method = $having ? 'havingCondition' : 'condition';
    $like_prefix = '';
    switch ($condition['operator']) {
      case 'CONTAINS':
        $like_prefix = '%';
      case 'STARTS_WITH':
        $select_query->$method($sql_field, $like_prefix . db_like($condition['value']) . '%', 'LIKE');
        break;
      default:
        $select_query->$method($sql_field, $condition['value'], $condition['operator']);
    }
  }
```

---
_Drupal 7.103 · [includes/entity.inc](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
