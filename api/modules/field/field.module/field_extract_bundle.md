# field_extract_bundle()

- **Type:** Function
- **File:** [`modules/field/field.module`](_file.md), lines 1025–1034 · [local source](../../../../source/modules/field/field.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module#L1025-L1034)
- **Module/theme:** field
- **Topics:** [field](../../../topics/field.md)

## Signature

```php
function field_extract_bundle($entity_type, $bundle)
```

## Documentation

```text
Helper function to extract the bundle name of from a bundle object.

@param $entity_type
  The type of $entity; e.g., 'node' or 'user'.
@param $bundle
  The bundle object (or string if bundles for this entity type do not exist
  as standalone objects).
@return
  The bundle name.
```

## Code

```php
function field_extract_bundle($entity_type, $bundle) {
  if (is_string($bundle)) {
    return $bundle;
  }

  $info = entity_get_info($entity_type);
  if (is_object($bundle) && isset($info['bundle keys']['bundle']) && isset($bundle->{$info['bundle keys']['bundle']})) {
    return $bundle->{$info['bundle keys']['bundle']};
  }
}
```

---
_Drupal 7.103 · [modules/field/field.module](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module) · Licensed GPL-2.0-or-later (see LICENSE)._
