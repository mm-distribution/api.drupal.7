# rdf_mapping_load()

- **Type:** Function
- **File:** [`modules/rdf/rdf.module`](_file.md), lines 133–144 · [local source](../../../../source/modules/rdf/rdf.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module#L133-L144)
- **Module/theme:** rdf
- **Topics:** [rdf](../../../topics/rdf.md)

## Signature

```php
function rdf_mapping_load($type, $bundle = RDF_DEFAULT_BUNDLE)
```

## Documentation

```text
Returns the mapping for attributes of a given entity type/bundle pair.

@param $type
  An entity type.
@param $bundle
  (optional) A bundle name.

@return
  The mapping corresponding to the requested entity type/bundle pair or an
  empty array.
```

## Code

```php
function rdf_mapping_load($type, $bundle = RDF_DEFAULT_BUNDLE) {
  // Retrieves the bundle-specific mapping from the entity info.
  $entity_info = entity_get_info($type);
  if (!empty($entity_info['bundles'][$bundle]['rdf_mapping'])) {
    return $entity_info['bundles'][$bundle]['rdf_mapping'];
  }
  // If there is no mapping defined for this bundle, we return the default
  // mapping that is defined for this entity type.
  else {
    return _rdf_get_default_mapping($type);
  }
}
```

---
_Drupal 7.103 · [modules/rdf/rdf.module](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module) · Licensed GPL-2.0-or-later (see LICENSE)._
