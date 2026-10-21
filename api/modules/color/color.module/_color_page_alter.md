# _color_page_alter()

- **Type:** Function
- **File:** [`modules/color/color.module`](_file.md), lines 120–128 · [local source](../../../../source/modules/color/color.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module#L120-L128)
- **Module/theme:** color

## Signature

```php
function _color_page_alter(&$vars)
```

## Documentation

```text
Replaces the logo with a color-altered logo.

A theme that supports the color module should call this function from its
THEME_process_page() function, so that the correct logo is included when
page.tpl.php is rendered.

@see theme()
```

## Code

```php
function _color_page_alter(&$vars) {
  global $theme_key;

  // Override logo.
  $logo = variable_get('color_' . $theme_key . '_logo');
  if ($logo && $vars['logo'] && preg_match('!' . $theme_key . '/logo.png$!', $vars['logo'])) {
    $vars['logo'] = file_create_url($logo);
  }
}
```

---
_Drupal 7.103 · [modules/color/color.module](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module) · Licensed GPL-2.0-or-later (see LICENSE)._
