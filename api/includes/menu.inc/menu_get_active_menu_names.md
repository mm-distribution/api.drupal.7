# menu_get_active_menu_names()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 2350–2352 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L2350-L2352)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_get_active_menu_names()
```

## Documentation

```text
Gets the active menu for the current page.
```

## Code

```php
function menu_get_active_menu_names() {
  return menu_set_active_menu_names();
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
