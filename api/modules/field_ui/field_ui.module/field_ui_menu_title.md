# field_ui_menu_title()

- **Type:** Function
- **File:** [`modules/field_ui/field_ui.module`](_file.md), lines 260–262 · [local source](../../../../source/modules/field_ui/field_ui.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.module#L260-L262)
- **Module/theme:** field_ui

## Signature

```php
function field_ui_menu_title($instance)
```

## Documentation

```text
Menu title callback.
```

## Code

```php
function field_ui_menu_title($instance) {
  return $instance['label'];
}
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.module](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.module) · Licensed GPL-2.0-or-later (see LICENSE)._
