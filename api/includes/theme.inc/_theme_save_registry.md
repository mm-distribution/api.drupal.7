# _theme_save_registry()

- **Type:** Function
- **File:** [`includes/theme.inc`](_file.md), lines 342–344 · [local source](../../../source/includes/theme.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc#L342-L344)

## Signature

```php
function _theme_save_registry($theme, $registry)
```

## Documentation

```text
Writes the theme_registry cache into the database.
```

## Code

```php
function _theme_save_registry($theme, $registry) {
  cache_set("theme_registry:$theme->name", $registry);
}
```

---
_Drupal 7.103 · [includes/theme.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
