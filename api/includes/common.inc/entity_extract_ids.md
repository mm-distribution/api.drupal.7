# entity_extract_ids()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 8118–8145 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L8118-L8145)

## Signature

```php
function entity_extract_ids($entity_type, $entity)
```

## Documentation

```text
Helper function to extract id, vid, and bundle name from an entity.

@param $entity_type
  The entity type; e.g. 'node' or 'user'.
@param $entity
  The entity from which to extract values.

@return
  A numerically indexed array (not a hash table) containing these
  elements:
  - 0: Primary ID of the entity.
  - 1: Revision ID of the entity, or NULL if $entity_type is not versioned.
  - 2: Bundle name of the entity, or NULL if $entity_type has no bundles.
```

## Code

```php
function entity_extract_ids($entity_type, $entity) {
  $info = entity_get_info($entity_type);

  // Objects being created might not have id/vid yet.
  if (!empty($info)) {
    $id = isset($entity->{$info['entity keys']['id']}) ? $entity->{$info['entity keys']['id']} : NULL;
    $vid = ($info['entity keys']['revision'] && isset($entity->{$info['entity keys']['revision']})) ? $entity->{$info['entity keys']['revision']} : NULL;
  }
  else {
    $id = NULL;
    $vid = NULL;
  }

  if (!empty($info['entity keys']['bundle'])) {
    // Explicitly fail for malformed entities missing the bundle property.
    if (!isset($entity->{$info['entity keys']['bundle']}) || $entity->{$info['entity keys']['bundle']} === '') {
      throw new EntityMalformedException(t('Missing bundle property on entity of type @entity_type.', array('@entity_type' => $entity_type)));
    }
    $bundle = $entity->{$info['entity keys']['bundle']};
  }
  else {
    // The entity type provides no bundle key: assume a single bundle, named
    // after the entity type.
    $bundle = $entity_type;
  }

  return array($id, $vid, $bundle);
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
