# drupal_theme_access()

- **Type:** Function
- **File:** [`includes/theme.inc`](_file.md), lines 47–55 · [local source](../../../source/includes/theme.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc#L47-L55)

## Signature

```php
function drupal_theme_access($theme)
```

## Documentation

```text
Determines if a theme is available to use.

@param $theme
  Either the name of a theme or a full theme object.

@return
  Boolean TRUE if the theme is enabled or is the site administration theme;
  FALSE otherwise.
```

## Code

```php
function drupal_theme_access($theme) {
  if (is_object($theme)) {
    return _drupal_theme_access($theme);
  }
  else {
    $themes = list_themes();
    return isset($themes[$theme]) && _drupal_theme_access($themes[$theme]);
  }
}
```

---
_Drupal 7.103 · [includes/theme.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
