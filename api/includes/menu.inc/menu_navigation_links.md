# menu_navigation_links()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 1858–1904 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L1858-L1904)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_navigation_links($menu_name, $level = 0)
```

## Documentation

```text
Returns an array of links for a navigation menu.

@param $menu_name
  The name of the menu.
@param $level
  Optional, the depth of the menu to be returned.

@return
  An array of links of the specified menu and level.
```

## Code

```php
function menu_navigation_links($menu_name, $level = 0) {
  // Don't even bother querying the menu table if no menu is specified.
  if (empty($menu_name)) {
    return array();
  }

  // Get the menu hierarchy for the current page.
  $tree = menu_tree_page_data($menu_name, $level + 1);

  // Go down the active trail until the right level is reached.
  while ($level-- > 0 && $tree) {
    // Loop through the current level's items until we find one that is in trail.
    while ($item = array_shift($tree)) {
      if ($item['link']['in_active_trail']) {
        // If the item is in the active trail, we continue in the subtree.
        $tree = empty($item['below']) ? array() : $item['below'];
        break;
      }
    }
  }

  // Create a single level of links.
  $router_item = menu_get_item();
  $links = array();
  foreach ($tree as $item) {
    if ($item['link']['access'] && !$item['link']['hidden']) {
      $class = '';
      $l = $item['link']['localized_options'];
      $l['href'] = $item['link']['href'];
      $l['title'] = $item['link']['title'];
      if ($item['link']['in_active_trail']) {
        $class = ' active-trail';
        $l['attributes']['class'][] = 'active-trail';
      }
      // Normally, l() compares the href of every link with $_GET['q'] and sets
      // the active class accordingly. But local tasks do not appear in menu
      // trees, so if the current path is a local task, and this link is its
      // tab root, then we have to set the class manually.
      if ($item['link']['href'] == $router_item['tab_root_href'] && $item['link']['href'] != $_GET['q']) {
        $l['attributes']['class'][] = 'active';
      }
      // Keyed with the unique mlid to generate classes in theme_links().
      $links['menu-' . $item['link']['mlid'] . $class] = $l;
    }
  }
  return $links;
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
