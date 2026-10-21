# _rdf_mapping_load()

- **Type:** Function
- **File:** [`modules/rdf/rdf.module`](_file.md), lines 192–195 · [local source](../../../../source/modules/rdf/rdf.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module#L192-L195)
- **Module/theme:** rdf

## Signature

```php
function _rdf_mapping_load($type, $bundle)
```

## Documentation

```text
Helper function to retrieve an RDF mapping from the database.

@param $type
  The entity type the mapping refers to.
@param $bundle
  The bundle the mapping refers to.

@return
  An RDF mapping structure or an empty array if no record was found.
```

## Code

```php
function _rdf_mapping_load($type, $bundle) {
  $mappings = _rdf_mapping_load_multiple($type, array($bundle));
  return $mappings ? reset($mappings) : array();
}
```

---
_Drupal 7.103 · [modules/rdf/rdf.module](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module) · Licensed GPL-2.0-or-later (see LICENSE)._
