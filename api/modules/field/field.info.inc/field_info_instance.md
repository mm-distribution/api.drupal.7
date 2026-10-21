# field_info_instance()

- **Type:** Function
- **File:** [`modules/field/field.info.inc`](_file.md), lines 627–633 · [local source](../../../../source/modules/field/field.info.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc#L627-L633)
- **Module/theme:** field
- **Topics:** [field_info](../../../topics/field_info.md)

## Signature

```php
function field_info_instance($entity_type, $field_name, $bundle_name)
```

## Documentation

```text
Returns an array of instance data for a specific field and bundle.

The function populates a static cache with all fields and instances used in
the bundle, allowing fast retrieval of field_info_field() or
field_info_instance() later in the request.

@param $entity_type
  The entity type for the instance.
@param $field_name
  The field name for the instance.
@param $bundle_name
  The bundle name for the instance.

@return
  An associative array of instance data for the specific field and bundle;
  NULL if the instance does not exist.
```

## Code

```php
function field_info_instance($entity_type, $field_name, $bundle_name) {
  $cache = _field_info_field_cache();
  $info = $cache->getBundleInstances($entity_type, $bundle_name);
  if (isset($info[$field_name])) {
    return $info[$field_name];
  }
}
```

---
_Drupal 7.103 · [modules/field/field.info.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
