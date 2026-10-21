# _menu_link_find_parent()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 3326–3384 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L3326-L3384)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function _menu_link_find_parent($menu_link, $parent_candidates = array())
```

## Documentation

```text
Finds a possible parent for a given menu link.

Because the parent of a given link might not exist anymore in the database,
we apply a set of heuristics to determine a proper parent:

 - use the passed parent link if specified and existing.
 - else, use the first existing link down the previous link hierarchy
 - else, for system menu links (derived from hook_menu()), reparent
   based on the path hierarchy.

@param $menu_link
  A menu link.
@param $parent_candidates
  An array of menu links keyed by mlid.

@return
  A menu link structure of the possible parent or FALSE if no valid parent
  has been found.
```

## Code

```php
function _menu_link_find_parent($menu_link, $parent_candidates = array()) {
  $parent = FALSE;

  // This item is explicitely top-level, skip the rest of the parenting.
  if (isset($menu_link['plid']) && empty($menu_link['plid'])) {
    return $parent;
  }

  // If we have a parent link ID, try to use that.
  $candidates = array();
  if (isset($menu_link['plid'])) {
    $candidates[] = $menu_link['plid'];
  }

  // Else, if we have a link hierarchy try to find a valid parent in there.
  if (!empty($menu_link['depth']) && $menu_link['depth'] > 1) {
    for ($depth = $menu_link['depth'] - 1; $depth >= 1; $depth--) {
      $candidates[] = $menu_link['p' . $depth];
    }
  }

  foreach ($candidates as $mlid) {
    if (isset($parent_candidates[$mlid])) {
      $parent = $parent_candidates[$mlid];
    }
    else {
      $parent = db_query("SELECT * FROM {menu_links} WHERE mlid = :mlid", array(':mlid' => $mlid))->fetchAssoc();
    }
    if ($parent) {
      return $parent;
    }
  }

  // If everything else failed, try to derive the parent from the path
  // hierarchy. This only makes sense for links derived from menu router
  // items (ie. from hook_menu()).
  if ($menu_link['module'] == 'system') {
    $query = db_select('menu_links');
    $query->condition('module', 'system');
    // We always respect the link's 'menu_name'; inheritance for router items is
    // ensured in _menu_router_build().
    $query->condition('menu_name', $menu_link['menu_name']);

    // Find the parent - it must be unique.
    $parent_path = $menu_link['link_path'];
    do {
      $parent = FALSE;
      $parent_path = substr($parent_path, 0, strrpos($parent_path, '/'));
      $new_query = clone $query;
      $new_query->condition('link_path', $parent_path);
      // Only valid if we get a unique result.
      if ($new_query->countQuery()->execute()->fetchField() == 1) {
        $parent = $new_query->fields('menu_links')->execute()->fetchAssoc();
      }
    } while ($parent === FALSE && $parent_path);
  }

  return $parent;
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
