# _menu_router_cache()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 2850–2857 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L2850-L2857)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function _menu_router_cache($new_menu = NULL)
```

## Documentation

```text
Stores the menu router if we have it in memory.
```

## Code

```php
function _menu_router_cache($new_menu = NULL) {
  $menu = &drupal_static(__FUNCTION__);

  if (isset($new_menu)) {
    $menu = $new_menu;
  }
  return $menu;
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
