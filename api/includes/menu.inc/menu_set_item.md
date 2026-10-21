# menu_set_item()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 433–435 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L433-L435)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_set_item($path, $router_item)
```

## Documentation

```text
Replaces the statically cached item for a given path.

@param $path
  The path.
@param $router_item
  The router item. Usually a router entry from menu_get_item() is either
  modified or set to a different path. This allows the navigation block,
  the page title, the breadcrumb, and the page help to be modified in one
  call.
```

## Code

```php
function menu_set_item($path, $router_item) {
  menu_get_item($path, $router_item);
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
