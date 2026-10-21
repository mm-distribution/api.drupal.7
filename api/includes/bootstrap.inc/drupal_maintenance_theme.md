# drupal_maintenance_theme()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 2976–2979 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L2976-L2979)

## Signature

```php
function drupal_maintenance_theme()
```

## Documentation

```text
Enables use of the theme system without requiring database access.

Loads and initializes the theme system for site installs, updates and when
the site is in maintenance mode. This also applies when the database fails.

@see _drupal_maintenance_theme()
```

## Code

```php
function drupal_maintenance_theme() {
  require_once DRUPAL_ROOT . '/includes/theme.maintenance.inc';
  _drupal_maintenance_theme();
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
