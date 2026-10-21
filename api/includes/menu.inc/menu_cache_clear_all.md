# menu_cache_clear_all()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 2728–2731 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L2728-L2731)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_cache_clear_all()
```

## Documentation

```text
Clears all cached menu data.

This should be called any time broad changes
might have been made to the router items or menu links.
```

## Code

```php
function menu_cache_clear_all() {
  cache_clear_all('*', 'cache_menu', TRUE);
  menu_reset_static_cache();
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
