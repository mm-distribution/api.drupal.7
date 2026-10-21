# _rdf_get_default_mapping()

- **Type:** Function
- **File:** [`modules/rdf/rdf.module`](_file.md), lines 160–179 · [local source](../../../../source/modules/rdf/rdf.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module#L160-L179)
- **Module/theme:** rdf

## Signature

```php
function _rdf_get_default_mapping($type)
```

## Documentation

```text
Helper function to get the default RDF mapping for a given entity type.

@param $type
  An entity type, e.g. 'node' or 'comment'.

@return
  The RDF mapping or an empty array if no mapping is defined for this entity
  type.
```

## Code

```php
function _rdf_get_default_mapping($type) {
  $default_mappings = &drupal_static(__FUNCTION__);

  if (!isset($default_mappings)) {
    // Get all of the modules that implement hook_rdf_mapping().
    $modules = module_implements('rdf_mapping');

    // Only consider the default entity mapping definitions.
    foreach ($modules as $module) {
      $mappings = module_invoke($module, 'rdf_mapping');
      foreach ($mappings as $mapping) {
        if ($mapping['bundle'] === RDF_DEFAULT_BUNDLE) {
          $default_mappings[$mapping['type']] = $mapping['mapping'];
        }
      }
    }
  }

  return isset($default_mappings[$type]) ? $default_mappings[$type] : array();
}
```

---
_Drupal 7.103 · [modules/rdf/rdf.module](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module) · Licensed GPL-2.0-or-later (see LICENSE)._
