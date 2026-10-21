# EntityFieldQuery::finishQuery()

- **Type:** Method
- **File:** [`includes/entity.inc`](../_file.md), lines 1380–1402 · [local source](../../../../source/includes/entity.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc#L1380-L1402)
- **Class:** [EntityFieldQuery](../EntityFieldQuery.md)

## Signature

```php
function finishQuery($select_query, $id_key = 'entity_id')
```

## Documentation

```text
Finishes the query.

Adds tags, metaData, range and returns the requested list or count.

@param SelectQuery $select_query
  A SelectQuery which has entity_type, entity_id, revision_id and bundle
  fields added.
@param $id_key
  Which field's values to use as the returned array keys.

@return
  See EntityFieldQuery::execute().
```

## Code

```php
  function finishQuery($select_query, $id_key = 'entity_id') {
    foreach ($this->tags as $tag) {
      $select_query->addTag($tag);
    }
    foreach ($this->metaData as $key => $object) {
      $select_query->addMetaData($key, $object);
    }
    $select_query->addMetaData('entity_field_query', $this);
    if ($this->range) {
      $select_query->range($this->range['start'], $this->range['length']);
    }
    if ($this->count) {
      return $select_query->countQuery()->execute()->fetchField();
    }
    $return = array();
    foreach ($select_query->execute() as $partial_entity) {
      $bundle = isset($partial_entity->bundle) ? $partial_entity->bundle : NULL;
      $entity = entity_create_stub_entity($partial_entity->entity_type, array($partial_entity->entity_id, $partial_entity->revision_id, $bundle));
      $return[$partial_entity->entity_type][$partial_entity->$id_key] = $entity;
      $this->ordered_results[] = $partial_entity;
    }
    return $return;
  }
```

---
_Drupal 7.103 · [includes/entity.inc](https://github.com/drupal/drupal/blob/7.103/includes/entity.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
