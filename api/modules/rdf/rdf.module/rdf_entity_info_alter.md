# rdf_entity_info_alter()

- **Type:** Function
- **File:** [`modules/rdf/rdf.module`](_file.md), lines 384–403 · [local source](../../../../source/modules/rdf/rdf.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module#L384-L403)
- **Module/theme:** rdf
- **Implements:** [hook_entity_info_alter()](../../system/system.api.php/hook_entity_info_alter.md)

## Signature

```php
function rdf_entity_info_alter(&$entity_info)
```

## Documentation

```text
Implements hook_entity_info_alter().

Adds the proper RDF mapping to each entity type/bundle pair.

@todo May need to move the comment below to another place.
This hook should not be used by modules to alter the bundle mappings.
The UI should always be authoritative. UI mappings are stored in the
database and if hook_entity_info_alter was used to override module defined
mappings, it would override the user defined mapping as well.
```

## Code

```php
function rdf_entity_info_alter(&$entity_info) {
  // Loop through each entity type and its bundles.
  foreach ($entity_info as $entity_type => $entity_type_info) {
    if (!empty($entity_type_info['bundles'])) {
      $bundles = array_keys($entity_type_info['bundles']);
      $mappings = _rdf_mapping_load_multiple($entity_type, $bundles);

      foreach ($bundles as $bundle) {
        if (isset($mappings[$bundle])) {
          $entity_info[$entity_type]['bundles'][$bundle]['rdf_mapping'] = $mappings[$bundle];
        }
        else {
          // If no mapping was found in the database, assign the default RDF
          // mapping for this entity type.
          $entity_info[$entity_type]['bundles'][$bundle]['rdf_mapping'] = _rdf_get_default_mapping($entity_type);
        }
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/rdf/rdf.module](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module) · Licensed GPL-2.0-or-later (see LICENSE)._
