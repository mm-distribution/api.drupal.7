# _menu_tree_check_access()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 1531–1549 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L1531-L1549)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function _menu_tree_check_access(&$tree)
```

## Documentation

```text
Sorts the menu tree and recursively checks access for each item.
```

## Code

```php
function _menu_tree_check_access(&$tree) {
  $new_tree = array();
  foreach ($tree as $key => $v) {
    $item = &$tree[$key]['link'];
    _menu_link_translate($item);
    if ($item['access'] || ($item['in_active_trail'] && strpos($item['href'], '%') !== FALSE)) {
      if ($tree[$key]['below']) {
        _menu_tree_check_access($tree[$key]['below']);
      }
      // The weights are made a uniform 5 digits by adding 50000 as an offset.
      // After _menu_link_translate(), $item['title'] has the localized link title.
      // Adding the mlid to the end of the index insures that it is unique.
      $new_tree[(50000 + $item['weight']) . ' ' . $item['title'] . ' ' . $item['mlid']] = $tree[$key];
    }
  }
  // Sort siblings in the tree based on the weights and localized titles.
  ksort($new_tree);
  $tree = $new_tree;
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
