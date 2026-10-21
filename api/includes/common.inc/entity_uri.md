# entity_uri()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 8371–8396 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L8371-L8396)

## Signature

```php
function entity_uri($entity_type, $entity)
```

## Documentation

```text
Returns the URI elements of an entity.

@param $entity_type
  The entity type; e.g. 'node' or 'user'.
@param $entity
  The entity for which to generate a path.
@return
  An array containing the 'path' and 'options' keys used to build the URI of
  the entity, and matching the signature of url(). NULL if the entity has no
  URI of its own.
```

## Code

```php
function entity_uri($entity_type, $entity) {
  $info = entity_get_info($entity_type);
  list($id, $vid, $bundle) = entity_extract_ids($entity_type, $entity);

  // A bundle-specific callback takes precedence over the generic one for the
  // entity type.
  if (isset($info['bundles'][$bundle]['uri callback'])) {
    $uri_callback = $info['bundles'][$bundle]['uri callback'];
  }
  elseif (isset($info['uri callback'])) {
    $uri_callback = $info['uri callback'];
  }
  else {
    return NULL;
  }

  // Invoke the callback to get the URI. If there is no callback, return NULL.
  if (isset($uri_callback) && function_exists($uri_callback)) {
    $uri = $uri_callback($entity);
    // Pass the entity data to url() so that alter functions do not need to
    // lookup this entity again.
    $uri['options']['entity_type'] = $entity_type;
    $uri['options']['entity'] = $entity;
    return $uri;
  }
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
