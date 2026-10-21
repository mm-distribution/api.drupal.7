# menu_cache_clear()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 2706–2720 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L2706-L2720)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_cache_clear($menu_name = 'navigation')
```

## Documentation

```text
Clears the cached data for a single named menu.
```

## Code

```php
function menu_cache_clear($menu_name = 'navigation') {
  $cache_cleared = &drupal_static(__FUNCTION__, array());

  if (empty($cache_cleared[$menu_name])) {
    cache_clear_all('links:' . $menu_name . ':', 'cache_menu', TRUE);
    $cache_cleared[$menu_name] = 1;
  }
  elseif ($cache_cleared[$menu_name] == 1) {
    drupal_register_shutdown_function('cache_clear_all', 'links:' . $menu_name . ':', 'cache_menu', TRUE);
    $cache_cleared[$menu_name] = 2;
  }

  // Also clear the menu system static caches.
  menu_reset_static_cache();
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
