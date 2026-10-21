# _menu_clear_page_cache()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 3389–3406 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L3389-L3406)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function _menu_clear_page_cache()
```

## Documentation

```text
Clears the page and block caches at most twice per page load.
```

## Code

```php
function _menu_clear_page_cache() {
  $cache_cleared = &drupal_static(__FUNCTION__, 0);

  // Clear the page and block caches, but at most twice, including at
  //  the end of the page load when there are multiple links saved or deleted.
  if ($cache_cleared == 0) {
    cache_clear_all();
    // Keep track of which menus have expanded items.
    _menu_set_expanded_menus();
    $cache_cleared = 1;
  }
  elseif ($cache_cleared == 1) {
    drupal_register_shutdown_function('cache_clear_all');
    // Keep track of which menus have expanded items.
    drupal_register_shutdown_function('_menu_set_expanded_menus');
    $cache_cleared = 2;
  }
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
