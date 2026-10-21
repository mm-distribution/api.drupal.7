# rdf_mapping_save()

- **Type:** Function
- **File:** [`modules/rdf/rdf.module`](_file.md), lines 241–260 · [local source](../../../../source/modules/rdf/rdf.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module#L241-L260)
- **Module/theme:** rdf
- **Topics:** [rdf](../../../topics/rdf.md)

## Signature

```php
function rdf_mapping_save($mapping)
```

## Documentation

```text
Saves an RDF mapping to the database.

Takes a mapping structure returned by hook_rdf_mapping() implementations
and creates or updates a record mapping for each encountered entity
type/bundle pair. If available, adds default values for non-existent mapping
keys.

@param $mapping
  The RDF mapping to save, as an array.

@return
  Status flag indicating the outcome of the operation.
```

## Code

```php
function rdf_mapping_save($mapping) {
  // In the case where a field has a mapping defined in the default entity
  // mapping, but a mapping is not specified in the bundle-specific mapping,
  // then use the default mapping for that field.
  $mapping['mapping'] += _rdf_get_default_mapping($mapping['type']);

  $status = db_merge('rdf_mapping')
    ->key(array(
      'type' => $mapping['type'],
      'bundle' => $mapping['bundle'],
    ))
    ->fields(array(
      'mapping' => serialize($mapping['mapping']),
    ))
    ->execute();

  entity_info_cache_clear();

  return $status;
}
```

---
_Drupal 7.103 · [modules/rdf/rdf.module](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module) · Licensed GPL-2.0-or-later (see LICENSE)._
