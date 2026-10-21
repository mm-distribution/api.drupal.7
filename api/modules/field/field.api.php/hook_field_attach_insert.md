# hook_field_attach_insert()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 1425–1427 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L1425-L1427)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_attach](../../../topics/field_attach.md)

## Signature

```php
function hook_field_attach_insert($entity_type, $entity)
```

## Documentation

```text
Act on field_attach_insert().

This hook is invoked after the field module has performed the operation.

See field_attach_insert() for details and arguments.
```

## Code

```php
function hook_field_attach_insert($entity_type, $entity) {
  // @todo Needs function body.
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_attach_insert()".

_None found._

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
