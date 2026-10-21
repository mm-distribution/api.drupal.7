# menu_get_router()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 2862–2869 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L2862-L2869)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_get_router()
```

## Documentation

```text
Gets the menu router.
```

## Code

```php
function menu_get_router() {
  // Check first if we have it in memory already.
  $menu = _menu_router_cache();
  if (empty($menu)) {
    list($menu, $masks) = menu_router_build();
  }
  return $menu;
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
