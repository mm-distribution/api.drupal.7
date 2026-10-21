# menu_links_clone()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 3013–3022 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L3013-L3022)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_links_clone($links, $menu_name = NULL)
```

## Documentation

```text
Clones an array of menu links.

@param $links
  An array of menu links to clone.
@param $menu_name
  (optional) The name of a menu that the links will be cloned for. If not
  set, the cloned links will be in the same menu as the original set of
  links that were passed in.

@return
  An array of menu links with the same properties as the passed-in array,
  but with the link identifiers removed so that a new link will be created
  when any of them is passed in to menu_link_save().

@see menu_link_save()
```

## Code

```php
function menu_links_clone($links, $menu_name = NULL) {
  foreach ($links as &$link) {
    unset($link['mlid']);
    unset($link['plid']);
    if (isset($menu_name)) {
      $link['menu_name'] = $menu_name;
    }
  }
  return $links;
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
