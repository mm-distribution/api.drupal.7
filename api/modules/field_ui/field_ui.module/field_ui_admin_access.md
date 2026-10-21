# field_ui_admin_access()

- **Type:** Function
- **File:** [`modules/field_ui/field_ui.module`](_file.md), lines 417–419 · [local source](../../../../source/modules/field_ui/field_ui.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.module#L417-L419)
- **Module/theme:** field_ui

## Signature

```php
function field_ui_admin_access($access_callback, $access_arguments)
```

## Documentation

```text
Access callback to determine if a user is allowed to use the field UI.

Only grant access if the user has both the "administer fields" permission and
is granted access by the entity specific restrictions.
```

## Code

```php
function field_ui_admin_access($access_callback, $access_arguments) {
  return user_access('administer fields') && call_user_func_array($access_callback, $access_arguments);
}
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.module](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.module) · Licensed GPL-2.0-or-later (see LICENSE)._
