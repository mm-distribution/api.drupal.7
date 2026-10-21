# color_form_system_themes_alter()

- **Type:** Function
- **File:** [`modules/color/color.module`](_file.md), lines 57–59 · [local source](../../../../source/modules/color/color.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module#L57-L59)
- **Module/theme:** color
- **Implements:** [hook_form_FORM_ID_alter()](../../system/system.api.php/hook_form_FORM_ID_alter.md)

## Signature

```php
function color_form_system_themes_alter(&$form, &$form_state)
```

## Documentation

```text
Implements hook_form_FORM_ID_alter().
```

## Code

```php
function color_form_system_themes_alter(&$form, &$form_state) {
  _color_theme_select_form_alter($form, $form_state);
}
```

---
_Drupal 7.103 · [modules/color/color.module](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module) · Licensed GPL-2.0-or-later (see LICENSE)._
