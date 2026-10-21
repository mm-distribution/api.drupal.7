# color_get_info()

- **Type:** Function
- **File:** [`modules/color/color.module`](_file.md), lines 133–147 · [local source](../../../../source/modules/color/color.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module#L133-L147)
- **Module/theme:** color

## Signature

```php
function color_get_info($theme)
```

## Documentation

```text
Retrieves the Color module information for a particular theme.
```

## Code

```php
function color_get_info($theme) {
  static $theme_info = array();

  if (isset($theme_info[$theme])) {
    return $theme_info[$theme];
  }

  $path = drupal_get_path('theme', $theme);
  $file = DRUPAL_ROOT . '/' . $path . '/color/color.inc';
  if ($path && file_exists($file)) {
    include $file;
    $theme_info[$theme] = $info;
    return $info;
  }
}
```

---
_Drupal 7.103 · [modules/color/color.module](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module) · Licensed GPL-2.0-or-later (see LICENSE)._
