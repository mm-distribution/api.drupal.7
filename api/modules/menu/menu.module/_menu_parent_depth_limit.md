# _menu_parent_depth_limit()

- **Type:** Function
- **File:** [`modules/menu/menu.module`](_file.md), lines 639–641 · [local source](../../../../source/modules/menu/menu.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module#L639-L641)
- **Module/theme:** menu

## Signature

```php
function _menu_parent_depth_limit($item)
```

## Documentation

```text
Find the depth limit for items in the parent select.
```

## Code

```php
function _menu_parent_depth_limit($item) {
  return MENU_MAX_DEPTH - 1 - (($item['mlid'] && $item['has_children']) ? menu_link_children_relative_depth($item) : 0);
}
```

---
_Drupal 7.103 · [modules/menu/menu.module](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module) · Licensed GPL-2.0-or-later (see LICENSE)._
