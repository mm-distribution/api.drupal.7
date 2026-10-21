# color_get_palette()

- **Type:** Function
- **File:** [`modules/color/color.module`](_file.md), lines 152–159 · [local source](../../../../source/modules/color/color.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module#L152-L159)
- **Module/theme:** color

## Signature

```php
function color_get_palette($theme, $default = FALSE)
```

## Documentation

```text
Retrieves the color palette for a particular theme.
```

## Code

```php
function color_get_palette($theme, $default = FALSE) {
  // Fetch and expand default palette.
  $info = color_get_info($theme);
  $palette = $info['schemes']['default']['colors'];

  // Load variable.
  return $default ? $palette : variable_get('color_' . $theme . '_palette', $palette);
}
```

---
_Drupal 7.103 · [modules/color/color.module](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module) · Licensed GPL-2.0-or-later (see LICENSE)._
