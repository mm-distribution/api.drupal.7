# menu_tree()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 1003–1011 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L1003-L1011)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_tree($menu_name)
```

## Documentation

```text
Renders a menu tree based on the current path.

The tree is expanded based on the current path and dynamic paths are also
changed according to the defined to_arg functions (for example the 'My
account' link is changed from user/% to a link with the current user's uid).

@param $menu_name
  The name of the menu.

@return
  A structured array representing the specified menu on the current page, to
  be rendered by drupal_render().
```

## Code

```php
function menu_tree($menu_name) {
  $menu_output = &drupal_static(__FUNCTION__, array());

  if (!isset($menu_output[$menu_name])) {
    $tree = menu_tree_page_data($menu_name);
    $menu_output[$menu_name] = menu_tree_output($tree);
  }
  return $menu_output[$menu_name];
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
