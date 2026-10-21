# _drupal_theme_access()

- **Type:** Function
- **File:** [`includes/theme.inc`](_file.md), lines 62–65 · [local source](../../../source/includes/theme.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc#L62-L65)

## Signature

```php
function _drupal_theme_access($theme)
```

## Documentation

```text
Helper function for determining access to a theme.

@see drupal_theme_access()
```

## Code

```php
function _drupal_theme_access($theme) {
  $admin_theme = variable_get('admin_theme');
  return !empty($theme->status) || ($admin_theme && $theme->name == $admin_theme);
}
```

---
_Drupal 7.103 · [includes/theme.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
