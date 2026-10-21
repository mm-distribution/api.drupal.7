# field_ui_field_attach_create_bundle()

- **Type:** Function
- **File:** [`modules/field_ui/field_ui.module`](_file.md), lines 329–333 · [local source](../../../../source/modules/field_ui/field_ui.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.module#L329-L333)
- **Module/theme:** field_ui
- **Implements:** [hook_field_attach_create_bundle()](../../field/field.api.php/hook_field_attach_create_bundle.md)

## Signature

```php
function field_ui_field_attach_create_bundle($entity_type, $bundle)
```

## Documentation

```text
Implements hook_field_attach_create_bundle().
```

## Code

```php
function field_ui_field_attach_create_bundle($entity_type, $bundle) {
  // When a new bundle is created, the menu needs to be rebuilt to add our
  // menu item tabs.
  variable_set('menu_rebuild_needed', TRUE);
}
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.module](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.module) · Licensed GPL-2.0-or-later (see LICENSE)._
