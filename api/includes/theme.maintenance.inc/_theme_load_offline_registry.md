# _theme_load_offline_registry()

- **Type:** Function
- **File:** [`includes/theme.maintenance.inc`](_file.md), lines 90–92 · [local source](../../../source/includes/theme.maintenance.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.maintenance.inc#L90-L92)

## Signature

```php
function _theme_load_offline_registry($theme, $base_theme = NULL, $theme_engine = NULL)
```

## Documentation

```text
Builds the registry when the site needs to bypass any database calls.
```

## Code

```php
function _theme_load_offline_registry($theme, $base_theme = NULL, $theme_engine = NULL) {
  return _theme_build_registry($theme, $base_theme, $theme_engine);
}
```

---
_Drupal 7.103 · [includes/theme.maintenance.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.maintenance.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
