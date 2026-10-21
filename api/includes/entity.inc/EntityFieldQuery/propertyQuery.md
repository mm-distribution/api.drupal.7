# EntityFieldQuery::propertyQuery()

- **Type:** Method
- **File:** [`includes/entity.inc`](../_file.md), lines 1267–1347 · [local source](../../../../source/includes/entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc#L1267-L1347)
- **Class:** [EntityFieldQuery](../EntityFieldQuery.md)

## Signature

```php
protected function propertyQuery()
```

## Documentation

```text
Queries entity tables in SQL for property conditions and sorts.

This method is only used if there are no field conditions and sorts.

@return
  See EntityFieldQuery::execute().
```

## Code

```php
  protected function propertyQuery() {
    if (empty($this->entityConditions['entity_type'])) {
      throw new EntityFieldQueryException(t('For this query an entity type must be specified.'));
    }
    $entity_type = $this->entityConditions['entity_type']['value'];
    $entity_info = entity_get_info($entity_type);
    if (empty($entity_info['base table'])) {
      throw new EntityFieldQueryException(t('Entity %entity has no base table.', array('%entity' => $entity_type)));
    }
    $base_table = $entity_info['base table'];
    $base_table_schema = drupal_get_schema($base_table);
    $select_query = db_select($base_table);
    $select_query->addExpression(':entity_type', 'entity_type', array(':entity_type' => $entity_type));
    // Process the property conditions.
    foreach ($this->propertyConditions as $property_condition) {
      $this->addCondition($select_query, $base_table . '.' . $property_condition['column'], $property_condition);
    }
    // Process the four possible entity condition.
    // The id field is always present in entity keys.
    $sql_field = $entity_info['entity keys']['id'];
    $id_map['entity_id'] = $sql_field;
    $select_query->addField($base_table, $sql_field, 'entity_id');
    if (isset($this->entityConditions['entity_id'])) {
      $this->addCondition($select_query, $base_table . '.' . $sql_field, $this->entityConditions['entity_id']);
    }

    // If there is a revision key defined, use it.
    if (!empty($entity_info['entity keys']['revision'])) {
      $sql_field = $entity_info['entity keys']['revision'];
      $select_query->addField($base_table, $sql_field, 'revision_id');
      if (isset($this->entityConditions['revision_id'])) {
        $this->addCondition($select_query, $base_table . '.' . $sql_field, $this->entityConditions['revision_id']);
      }
    }
    else {
      $sql_field = 'revision_id';
      $select_query->addExpression('NULL', 'revision_id');
    }
    $id_map['revision_id'] = $sql_field;

    // Handle bundles.
    if (!empty($entity_info['entity keys']['bundle'])) {
      $sql_field = $entity_info['entity keys']['bundle'];
      $having = FALSE;

      if (!empty($base_table_schema['fields'][$sql_field])) {
        $select_query->addField($base_table, $sql_field, 'bundle');
      }
    }
    else {
      $sql_field = 'bundle';
      $select_query->addExpression(':bundle', 'bundle', array(':bundle' => $entity_type));
      $having = TRUE;
    }
    $id_map['bundle'] = $sql_field;
    if (isset($this->entityConditions['bundle'])) {
      if (!empty($entity_info['entity keys']['bundle'])) {
        $this->addCondition($select_query, $base_table . '.' . $sql_field, $this->entityConditions['bundle'], $having);
      }
      else {
        // This entity has no bundle, so invalidate the query.
        $select_query->where('1 = 0');
      }
    }

    // Order the query.
    foreach ($this->order as $order) {
      if ($order['type'] == 'entity') {
        $key = $order['specifier'];
        if (!isset($id_map[$key])) {
          throw new EntityFieldQueryException(t('Do not know how to order on @key for @entity_type', array('@key' => $key, '@entity_type' => $entity_type)));
        }
        $select_query->orderBy($id_map[$key], $order['direction']);
      }
      elseif ($order['type'] == 'property') {
        $select_query->orderBy($base_table . '.' . $order['specifier'], $order['direction']);
      }
    }

    return $this->finishQuery($select_query);
  }
```

---
_Drupal 7.103 · [includes/entity.inc](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
