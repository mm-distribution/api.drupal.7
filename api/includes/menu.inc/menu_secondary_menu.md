# menu_secondary_menu()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 1835–1845 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L1835-L1845)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_secondary_menu()
```

## Documentation

```text
Returns an array of links to be rendered as the Secondary links.
```

## Code

```php
function menu_secondary_menu() {

  // If the secondary menu source is set as the primary menu, we display the
  // second level of the primary menu.
  if (variable_get('menu_secondary_links_source', 'user-menu') == variable_get('menu_main_links_source', 'main-menu')) {
    return menu_navigation_links(variable_get('menu_main_links_source', 'main-menu'), 1);
  }
  else {
    return menu_navigation_links(variable_get('menu_secondary_links_source', 'user-menu'), 0);
  }
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
