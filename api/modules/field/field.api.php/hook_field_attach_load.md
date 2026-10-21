# hook_field_attach_load()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 1341–1343 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L1341-L1343)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_attach](../../../topics/field_attach.md)

## Signature

```php
function hook_field_attach_load($entity_type, $entities, $age, $options)
```

## Documentation

```text
Act on field_attach_load().

This hook is invoked after the field module has performed the operation.

Unlike other field_attach hooks, this hook accounts for 'multiple loads'.
Instead of the usual $entity parameter, it accepts an array of entities,
indexed by entity ID. For performance reasons, information for all available
entities should be loaded in a single query where possible.

The changes made to the entities' field values get cached by the field cache
for subsequent loads.

See field_attach_load() for details and arguments.
```

## Code

```php
function hook_field_attach_load($entity_type, $entities, $age, $options) {
  // @todo Needs function body.
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_attach_load()".

_None found._

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
