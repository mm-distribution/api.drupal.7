# field_attach_create_bundle()

- **Type:** Function
- **File:** [`modules/field/field.attach.inc`](_file.md), lines 1342–1348 · [local source](../../../../source/modules/field/field.attach.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.attach.inc#L1342-L1348)
- **Module/theme:** field
- **Topics:** [field_attach](../../../topics/field_attach.md)

## Signature

```php
function field_attach_create_bundle($entity_type, $bundle)
```

## Documentation

```text
Notify field.module that a new bundle was created.

The default SQL-based storage doesn't need to do anything about it, but
others might.

@param $entity_type
  The entity type to which the bundle is bound.
@param $bundle
  The name of the newly created bundle.
```

## Code

```php
function field_attach_create_bundle($entity_type, $bundle) {
  // Clear the cache.
  field_cache_clear();

  // Let other modules act on creating the bundle.
  module_invoke_all('field_attach_create_bundle', $entity_type, $bundle);
}
```

---
_Drupal 7.103 · [modules/field/field.attach.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.attach.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
