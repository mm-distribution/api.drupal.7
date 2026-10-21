# menu_main_menu()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 1828–1830 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L1828-L1830)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_main_menu()
```

## Documentation

```text
Returns an array of links to be rendered as the Main menu.
```

## Code

```php
function menu_main_menu() {
  return menu_navigation_links(variable_get('menu_main_links_source', 'main-menu'));
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
