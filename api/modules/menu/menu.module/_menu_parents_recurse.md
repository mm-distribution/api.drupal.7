# _menu_parents_recurse()

- **Type:** Function
- **File:** [`modules/menu/menu.module`](_file.md), lines 431–446 · [local source](../../../../source/modules/menu/menu.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module#L431-L446)
- **Module/theme:** menu

## Signature

```php
function _menu_parents_recurse($tree, $menu_name, $indent, &$options, $exclude, $depth_limit)
```

## Documentation

```text
Recursive helper function for menu_parent_options().
```

## Code

```php
function _menu_parents_recurse($tree, $menu_name, $indent, &$options, $exclude, $depth_limit) {
  foreach ($tree as $data) {
    if ($data['link']['depth'] > $depth_limit) {
      // Don't iterate through any links on this level.
      break;
    }
    if ($data['link']['mlid'] != $exclude && $data['link']['hidden'] >= 0) {
      $title = $indent . ' ' . truncate_utf8($data['link']['title'], 30, TRUE, FALSE);
      menu_add_link_labels($title, $data['link']);
      $options[$menu_name . ':' . $data['link']['mlid']] = $title;
      if ($data['below']) {
        _menu_parents_recurse($data['below'], $menu_name, $indent . '--', $options, $exclude, $depth_limit);
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/menu/menu.module](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module) · Licensed GPL-2.0-or-later (see LICENSE)._
