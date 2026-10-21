# rdf_entity_load()

- **Type:** Function
- **File:** [`modules/rdf/rdf.module`](_file.md), lines 408–414 · [local source](../../../../source/modules/rdf/rdf.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module#L408-L414)
- **Module/theme:** rdf
- **Implements:** [hook_entity_load()](../../system/system.api.php/hook_entity_load.md)

## Signature

```php
function rdf_entity_load($entities, $type)
```

## Documentation

```text
Implements hook_entity_load().
```

## Code

```php
function rdf_entity_load($entities, $type) {
  foreach ($entities as $entity) {
    // Extracts the bundle of the entity being loaded.
    list($id, $vid, $bundle) = entity_extract_ids($type, $entity);
    $entity->rdf_mapping = rdf_mapping_load($type, $bundle);
  }
}
```

---
_Drupal 7.103 · [modules/rdf/rdf.module](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module) · Licensed GPL-2.0-or-later (see LICENSE)._
