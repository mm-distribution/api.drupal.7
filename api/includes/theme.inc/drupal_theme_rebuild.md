# drupal_theme_rebuild()

- **Type:** Function
- **File:** [`includes/theme.inc`](_file.md), lines 352–355 · [local source](../../../source/includes/theme.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc#L352-L355)

## Signature

```php
function drupal_theme_rebuild()
```

## Documentation

```text
Forces the system to rebuild the theme registry.

This function should be called when modules are added to the system, or when
a dynamic system needs to add more theme hooks.
```

## Code

```php
function drupal_theme_rebuild() {
  drupal_static_reset('theme_get_registry');
  cache_clear_all('theme_registry', 'cache', TRUE);
}
```

---
_Drupal 7.103 · [includes/theme.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
