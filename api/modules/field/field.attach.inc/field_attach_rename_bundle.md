# field_attach_rename_bundle()

- **Type:** Function
- **File:** [`modules/field/field.attach.inc`](_file.md), lines 1360–1377 · [local source](../../../../source/modules/field/field.attach.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.attach.inc#L1360-L1377)
- **Module/theme:** field
- **Topics:** [field_attach](../../../topics/field_attach.md)

## Signature

```php
function field_attach_rename_bundle($entity_type, $bundle_old, $bundle_new)
```

## Documentation

```text
Notify field.module that a bundle was renamed.

@param $entity_type
  The entity type to which the bundle is bound.
@param $bundle_old
  The previous name of the bundle.
@param $bundle_new
  The new name of the bundle.
```

## Code

```php
function field_attach_rename_bundle($entity_type, $bundle_old, $bundle_new) {
  db_update('field_config_instance')
    ->fields(array('bundle' => $bundle_new))
    ->condition('entity_type', $entity_type)
    ->condition('bundle', $bundle_old)
    ->execute();

  // Clear the cache.
  field_cache_clear();

  // Update bundle settings.
  $settings = variable_get('field_bundle_settings_' . $entity_type . '__' . $bundle_old, array());
  variable_set('field_bundle_settings_' . $entity_type . '__' . $bundle_new, $settings);
  variable_del('field_bundle_settings_' . $entity_type . '__' . $bundle_old);

  // Let other modules act on renaming the bundle.
  module_invoke_all('field_attach_rename_bundle', $entity_type, $bundle_old, $bundle_new);
}
```

---
_Drupal 7.103 · [modules/field/field.attach.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.attach.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
