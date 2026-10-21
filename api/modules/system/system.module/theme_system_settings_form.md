# theme_system_settings_form()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 4058–4060 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L4058-L4060)
- **Module/theme:** system
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_system_settings_form($variables)
```

## Documentation

```text
Returns HTML for a system settings form.

By default this does not alter the appearance of a form at all,
but is provided as a convenience for themers.

@param $variables
  An associative array containing:
  - form: A render element representing the form.

@ingroup themeable
```

## Code

```php
function theme_system_settings_form($variables) {
  return drupal_render_children($variables['form']);
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
