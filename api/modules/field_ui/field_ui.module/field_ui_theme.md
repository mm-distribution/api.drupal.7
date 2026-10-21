# field_ui_theme()

- **Type:** Function
- **File:** [`modules/field_ui/field_ui.module`](_file.md), lines 305–311 · [local source](../../../../source/modules/field_ui/field_ui.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.module#L305-L311)
- **Module/theme:** field_ui
- **Implements:** [hook_theme()](../../system/system.api.php/hook_theme.md)

## Signature

```php
function field_ui_theme()
```

## Documentation

```text
Implements hook_theme().
```

## Code

```php
function field_ui_theme() {
  return array(
    'field_ui_table' => array(
      'render element' => 'elements',
    ),
  );
}
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.module](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.module) · Licensed GPL-2.0-or-later (see LICENSE)._
