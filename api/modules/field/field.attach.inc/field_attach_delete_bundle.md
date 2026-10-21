# field_attach_delete_bundle()

- **Type:** Function
- **File:** [`modules/field/field.attach.inc`](_file.md), lines 1394–1411 · [local source](../../../../source/modules/field/field.attach.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.attach.inc#L1394-L1411)
- **Module/theme:** field
- **Topics:** [field_attach](../../../topics/field_attach.md)

## Signature

```php
function field_attach_delete_bundle($entity_type, $bundle)
```

## Documentation

```text
Notify field.module the a bundle was deleted.

This deletes the data for the field instances as well as the field instances
themselves. This function actually just marks the data and field instances
and deleted, leaving the garbage collection for a separate process, because
it is not always possible to delete this much data in a single page request
(particularly since for some field types, the deletion is more than just a
simple DELETE query).

@param $entity_type
  The entity type to which the bundle is bound.
@param $bundle
  The bundle to delete.
```

## Code

```php
function field_attach_delete_bundle($entity_type, $bundle) {
  // First, delete the instances themselves. field_read_instances() must be
  // used here since field_info_instances() does not return instances for
  // disabled entity types or bundles.
  $instances = field_read_instances(array('entity_type' => $entity_type, 'bundle' => $bundle), array('include_inactive' => 1));
  foreach ($instances as $instance) {
    field_delete_instance($instance);
  }

  // Clear the cache.
  field_cache_clear();

  // Clear bundle display settings.
  variable_del('field_bundle_settings_' . $entity_type . '__' . $bundle);

  // Let other modules act on deleting the bundle.
  module_invoke_all('field_attach_delete_bundle', $entity_type, $bundle, $instances);
}
```

---
_Drupal 7.103 · [modules/field/field.attach.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.attach.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
