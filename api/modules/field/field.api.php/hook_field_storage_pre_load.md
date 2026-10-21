# hook_field_storage_pre_load()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 2236–2238 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L2236-L2238)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_storage](../../../topics/field_storage.md)

## Signature

```php
function hook_field_storage_pre_load($entity_type, $entities, $age, &$skip_fields, $options)
```

## Documentation

```text
Act before the storage backends load field data.

This hook allows modules to load data before the Field Storage API,
optionally preventing the field storage module from doing so.

This lets 3rd party modules override, mirror, shard, or otherwise store a
subset of fields in a different way than the current storage engine.
Possible use cases include per-bundle storage, per-combo-field storage, etc.

Modules implementing this hook should load field values and add them to
objects in $entities. Fields with no values should be added as empty
arrays. In addition, fields loaded should be added as keys to $skip_fields.

@param $entity_type
  The type of entity, such as 'node' or 'user'.
@param $entities
  The array of entity objects to add fields to, keyed by entity ID.
@param $age
  FIELD_LOAD_CURRENT to load the most recent revision for all fields, or
  FIELD_LOAD_REVISION to load the version indicated by each entity.
@param $skip_fields
  An array keyed by field IDs whose data has already been loaded and
  therefore should not be loaded again. Add a key to this array to indicate
  that your module has already loaded a field.
@param $options
  An associative array of additional options, with the following keys:
  - field_id: The field ID that should be loaded. If unset, all fields
    should be loaded.
  - deleted: If TRUE, deleted fields should be loaded as well as
    non-deleted fields. If unset or FALSE, only non-deleted fields should be
    loaded.
```

## Code

```php
function hook_field_storage_pre_load($entity_type, $entities, $age, &$skip_fields, $options) {
  // @todo Needs function body.
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_storage_pre_load()".

_None found._

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
