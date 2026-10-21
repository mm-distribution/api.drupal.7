# field_ui_field_attach_rename_bundle()

- **Type:** Function
- **File:** [`modules/field_ui/field_ui.module`](_file.md), lines 52–58 · [local source](../../../../source/modules/field_ui/field_ui.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.module#L52-L58)
- **Module/theme:** field_ui
- **Implements:** [hook_field_attach_rename_bundle()](../../field/field.api.php/hook_field_attach_rename_bundle.md)

## Signature

```php
function field_ui_field_attach_rename_bundle($entity_type, $bundle_old, $bundle_new)
```

## Documentation

```text
Implements hook_field_attach_rename_bundle().
```

## Code

```php
function field_ui_field_attach_rename_bundle($entity_type, $bundle_old, $bundle_new) {
  // The Field UI relies on entity_get_info() to build menu items for entity
  // field administration pages. Clear the entity info cache and ensure that
  // the menu is rebuilt.
  entity_info_cache_clear();
  menu_rebuild();
}
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.module](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.module) · Licensed GPL-2.0-or-later (see LICENSE)._
