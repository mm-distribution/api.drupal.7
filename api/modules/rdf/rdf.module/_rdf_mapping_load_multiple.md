# _rdf_mapping_load_multiple()

- **Type:** Function
- **File:** [`modules/rdf/rdf.module`](_file.md), lines 208–220 · [local source](../../../../source/modules/rdf/rdf.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module#L208-L220)
- **Module/theme:** rdf

## Signature

```php
function _rdf_mapping_load_multiple($type, array $bundles)
```

## Documentation

```text
Helper function to retrieve a set of RDF mappings from the database.

@param $type
  The entity type of the mappings.
@param $bundles
  The bundles the mappings refer to.

@return
  An array of RDF mapping structures, or an empty array.
```

## Code

```php
function _rdf_mapping_load_multiple($type, array $bundles) {
  $mappings = db_select('rdf_mapping')
    ->fields(NULL, array('bundle', 'mapping'))
    ->condition('type', $type)
    ->condition('bundle', $bundles)
    ->execute()
    ->fetchAllKeyed();

  foreach ($mappings as $bundle => $mapping) {
    $mappings[$bundle] = unserialize($mapping);
  }
  return $mappings;
}
```

---
_Drupal 7.103 · [modules/rdf/rdf.module](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module) · Licensed GPL-2.0-or-later (see LICENSE)._
