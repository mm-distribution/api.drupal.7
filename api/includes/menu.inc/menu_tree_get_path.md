# menu_tree_get_path()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 1199–1201 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L1199-L1201)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_tree_get_path($menu_name)
```

## Documentation

```text
Gets the path for determining the active trail of the specified menu tree.

@param $menu_name
  The menu name of the requested tree.

@return
  A string containing the path. If no path has been specified with
  menu_tree_set_path(), NULL is returned.
```

## Code

```php
function menu_tree_get_path($menu_name) {
  return menu_tree_set_path($menu_name);
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
