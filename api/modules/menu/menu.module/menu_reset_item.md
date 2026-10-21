# menu_reset_item()

- **Type:** Function
- **File:** [`modules/menu/menu.module`](_file.md), lines 472–487 · [local source](../../../../source/modules/menu/menu.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module#L472-L487)
- **Module/theme:** menu

## Signature

```php
function menu_reset_item($link)
```

## Documentation

```text
Reset a system-defined menu link.
```

## Code

```php
function menu_reset_item($link) {
  // To reset the link to its original values, we need to retrieve its
  // definition from hook_menu(). Otherwise, for example, the link's menu would
  // not be reset, because properties like the original 'menu_name' are not
  // stored anywhere else. Since resetting a link happens rarely and this is a
  // one-time operation, retrieving the full menu router does no harm.
  $menu = menu_get_router();
  $router_item = $menu[$link['router_path']];
  $new_link = _menu_link_build($router_item);
  // Merge existing menu link's ID and 'has_children' property.
  foreach (array('mlid', 'has_children') as $key) {
    $new_link[$key] = $link[$key];
  }
  menu_link_save($new_link);
  return $new_link;
}
```

---
_Drupal 7.103 · [modules/menu/menu.module](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module) · Licensed GPL-2.0-or-later (see LICENSE)._
