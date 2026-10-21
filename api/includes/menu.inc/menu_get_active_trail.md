# menu_get_active_trail()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 2583–2585 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L2583-L2585)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_get_active_trail()
```

## Documentation

```text
Gets the active trail (path to root menu root) of the current page.

If a trail is supplied to menu_set_active_trail(), that value is returned. If
a trail is not supplied to menu_set_active_trail(), the path to the current
page is calculated and returned. The calculated trail is also saved as a
static value for use by subsequent calls to menu_get_active_trail().

@return
  Path to menu root of the current page, as an array of menu link items,
  starting with the site's home page. Each link item is an associative array
  with the following components:
  - title: Title of the item.
  - href: Drupal path of the item.
  - localized_options: Options for passing into the l() function.
  - type: A menu type constant, such as MENU_DEFAULT_LOCAL_TASK, or 0 to
    indicate it's not really in the menu (used for the home page item).
```

## Code

```php
function menu_get_active_trail() {
  return menu_set_active_trail();
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
