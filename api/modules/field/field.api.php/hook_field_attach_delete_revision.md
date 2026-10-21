# hook_field_attach_delete_revision()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 1477–1479 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L1477-L1479)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_attach](../../../topics/field_attach.md)

## Signature

```php
function hook_field_attach_delete_revision($entity_type, $entity)
```

## Documentation

```text
Act on field_attach_delete_revision().

This hook is invoked after the field module has performed the operation.

See field_attach_delete_revision() for details and arguments.
```

## Code

```php
function hook_field_attach_delete_revision($entity_type, $entity) {
  // @todo Needs function body.
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_attach_delete_revision()".

_None found._

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
