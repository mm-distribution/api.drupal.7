# _menu_navigation_links_rebuild()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 2899–2994 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L2899-L2994)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function _menu_navigation_links_rebuild($menu)
```

## Documentation

```text
Builds menu links for the items in the menu router.
```

## Code

```php
function _menu_navigation_links_rebuild($menu) {
  // Add normal and suggested items as links.
  $menu_links = array();
  foreach ($menu as $path => $item) {
    if ($item['_visible']) {
      $menu_links[$path] = $item;
      $sort[$path] = $item['_number_parts'];
    }
  }
  if ($menu_links) {
    // Keep an array of processed menu links, to allow menu_link_save() to
    // check this for parents instead of querying the database.
    $parent_candidates = array();
    // Make sure no child comes before its parent.
    array_multisort($sort, SORT_NUMERIC, $menu_links);

    foreach ($menu_links as $key => $item) {
      $existing_item = db_select('menu_links')
        ->fields('menu_links')
        ->condition('link_path', $item['path'])
        ->condition('module', 'system')
        ->execute()->fetchAssoc();
      if ($existing_item) {
        $item['mlid'] = $existing_item['mlid'];
        // A change in hook_menu may move the link to a different menu
        if (empty($item['menu_name']) || ($item['menu_name'] == $existing_item['menu_name'])) {
          $item['menu_name'] = $existing_item['menu_name'];
          $item['plid'] = $existing_item['plid'];
        }
        else {
          // It moved to a new menu. Let menu_link_save() try to find a new
          // parent based on the path.
          unset($item['plid']);
        }
        $item['has_children'] = $existing_item['has_children'];
        $item['updated'] = $existing_item['updated'];
      }
      if ($existing_item && $existing_item['customized']) {
        $parent_candidates[$existing_item['mlid']] = $existing_item;
      }
      else {
        $item = _menu_link_build($item);
        menu_link_save($item, $existing_item, $parent_candidates);
        $parent_candidates[$item['mlid']] = $item;
        unset($menu_links[$key]);
      }
    }
  }
  $paths = array_keys($menu);
  // Updated and customized items whose router paths are gone need new ones.
  $result = db_select('menu_links', NULL, array('fetch' => PDO::FETCH_ASSOC))
    ->fields('menu_links', array(
      'link_path',
      'mlid',
      'router_path',
      'updated',
    ))
    ->condition(db_or()
      ->condition('updated', 1)
      ->condition(db_and()
        ->condition('router_path', $paths, 'NOT IN')
        ->condition('external', 0)
        ->condition('customized', 1)
      )
    )
    ->execute();
  foreach ($result as $item) {
    $router_path = _menu_find_router_path($item['link_path']);
    if (!empty($router_path) && ($router_path != $item['router_path'] || $item['updated'])) {
      // If the router path and the link path matches, it's surely a working
      // item, so we clear the updated flag.
      $updated = $item['updated'] && $router_path != $item['link_path'];
      db_update('menu_links')
        ->fields(array(
          'router_path' => $router_path,
          'updated' => (int) $updated,
        ))
        ->condition('mlid', $item['mlid'])
        ->execute();
    }
  }
  // Find any item whose router path does not exist any more.
  $result = db_select('menu_links')
    ->fields('menu_links')
    ->condition('router_path', $paths, 'NOT IN')
    ->condition('external', 0)
    ->condition('updated', 0)
    ->condition('customized', 0)
    ->orderBy('depth', 'DESC')
    ->execute();
  // Remove all such items. Starting from those with the greatest depth will
  // minimize the amount of re-parenting done by menu_link_delete().
  foreach ($result as $item) {
    _menu_delete_item($item, TRUE);
  }
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
