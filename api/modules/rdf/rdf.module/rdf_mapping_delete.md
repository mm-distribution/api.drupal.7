# rdf_mapping_delete()

- **Type:** Function
- **File:** [`modules/rdf/rdf.module`](_file.md), lines 273–280 · [local source](../../../../source/modules/rdf/rdf.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module#L273-L280)
- **Module/theme:** rdf
- **Topics:** [rdf](../../../topics/rdf.md)

## Signature

```php
function rdf_mapping_delete($type, $bundle)
```

## Documentation

```text
Deletes the mapping for the given bundle from the database.

@param $type
  The entity type the mapping refers to.
@param $bundle
  The bundle the mapping refers to.

@return
  Return boolean TRUE if mapping deleted, FALSE if not.
```

## Code

```php
function rdf_mapping_delete($type, $bundle) {
  $num_rows = db_delete('rdf_mapping')
    ->condition('type', $type)
    ->condition('bundle', $bundle)
    ->execute();

  return (bool) ($num_rows > 0);
}
```

---
_Drupal 7.103 · [modules/rdf/rdf.module](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module) · Licensed GPL-2.0-or-later (see LICENSE)._
