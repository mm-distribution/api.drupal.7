# field_info_instances()

- **Type:** Function
- **File:** [`modules/field/field.info.inc`](_file.md), lines 596–607 · [local source](../../../../source/modules/field/field.info.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc#L596-L607)
- **Module/theme:** field
- **Topics:** [field_info](../../../topics/field_info.md)

## Signature

```php
function field_info_instances($entity_type = NULL, $bundle_name = NULL)
```

## Documentation

```text
Retrieves information about field instances.

Use of this function to retrieve instances across separate bundles (i.e.
when the $bundle parameter is NULL) should be avoided when possible, since
it loads and statically caches a potentially large array of information. Use
field_info_field_map() instead.

When retrieving the instances of a specific bundle (i.e. when both
$entity_type and $bundle_name are provided), the function also populates a
static cache with the corresponding field definitions, allowing fast
retrieval of field_info_field() later in the request.

@param $entity_type
  (optional) The entity type for which to return instances.
@param $bundle_name
  (optional) The bundle name for which to return instances. If $entity_type
  is NULL, the $bundle_name parameter is ignored.

@return
  If $entity_type is not set, return all instances keyed by entity type and
  bundle name. If $entity_type is set, return all instances for that entity
  type, keyed by bundle name. If $entity_type and $bundle_name are set, return
  all instances for that bundle.

@see field_info_field_map()
```

## Code

```php
function field_info_instances($entity_type = NULL, $bundle_name = NULL) {
  $cache = _field_info_field_cache();

  if (!isset($entity_type)) {
    return $cache->getInstances();
  }
  if (!isset($bundle_name)) {
    return $cache->getInstances($entity_type);
  }

  return $cache->getBundleInstances($entity_type, $bundle_name);
}
```

---
_Drupal 7.103 · [modules/field/field.info.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
