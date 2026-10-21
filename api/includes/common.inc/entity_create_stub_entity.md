# entity_create_stub_entity()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 8162–8173 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L8162-L8173)

## Signature

```php
function entity_create_stub_entity($entity_type, $ids)
```

## Documentation

```text
Helper function to assemble an object structure with initial ids.

This function can be seen as reciprocal to entity_extract_ids().

@param $entity_type
  The entity type; e.g. 'node' or 'user'.
@param $ids
  A numerically indexed array, as returned by entity_extract_ids().

@return
  An entity structure, initialized with the ids provided.

@see entity_extract_ids()
```

## Code

```php
function entity_create_stub_entity($entity_type, $ids) {
  $entity = new stdClass();
  $info = entity_get_info($entity_type);
  $entity->{$info['entity keys']['id']} = $ids[0];
  if (!empty($info['entity keys']['revision']) && isset($ids[1])) {
    $entity->{$info['entity keys']['revision']} = $ids[1];
  }
  if (!empty($info['entity keys']['bundle']) && isset($ids[2])) {
    $entity->{$info['entity keys']['bundle']} = $ids[2];
  }
  return $entity;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
