# hook_field_attach_create_bundle()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 1621–1625 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L1621-L1625)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_attach](../../../topics/field_attach.md)

## Signature

```php
function hook_field_attach_create_bundle($entity_type, $bundle)
```

## Documentation

```text
Act on field_attach_create_bundle().

This hook is invoked after the field module has performed the operation.

See field_attach_create_bundle() for details and arguments.
```

## Code

```php
function hook_field_attach_create_bundle($entity_type, $bundle) {
  // When a new bundle is created, the menu needs to be rebuilt to add the
  // Field UI menu item tabs.
  variable_set('menu_rebuild_needed', TRUE);
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_attach_create_bundle()".

- [field_test_field_attach_create_bundle()](../tests/field_test.storage.inc/field_test_field_attach_create_bundle.md) — `modules/field/tests/field_test.storage.inc`
- [field_ui_field_attach_create_bundle()](../../field_ui/field_ui.module/field_ui_field_attach_create_bundle.md) — `modules/field_ui/field_ui.module`

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
