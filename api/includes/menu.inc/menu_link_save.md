# menu_link_save()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 3153–3304 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L3153-L3304)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_link_save(&$item, $existing_item = array(), $parent_candidates = array())
```

## Documentation

```text
Saves a menu link.

After calling this function, rebuild the menu cache using
menu_cache_clear_all().

@param $item
  An associative array representing a menu link item, with elements:
  - link_path: (required) The path of the menu item, which should be
    normalized first by calling drupal_get_normal_path() on it.
  - link_title: (required) Title to appear in menu for the link.
  - menu_name: (optional) The machine name of the menu for the link.
    Defaults to 'navigation'.
  - weight: (optional) Integer to determine position in menu. Default is 0.
  - expanded: (optional) Boolean that determines if the item is expanded.
  - options: (optional) An array of options, see l() for more.
  - mlid: (optional) Menu link identifier, the primary integer key for each
    menu link. Can be set to an existing value, or to 0 or NULL
    to insert a new link.
  - plid: (optional) The mlid of the parent.
  - router_path: (optional) The path of the relevant router item.
@param $existing_item
  Optional, the current record from the {menu_links} table as an array.
@param $parent_candidates
  Optional array of menu links keyed by mlid. Used by
  _menu_navigation_links_rebuild() only.

@return
  The mlid of the saved menu link, or FALSE if the menu link could not be
  saved.
```

## Code

```php
function menu_link_save(&$item, $existing_item = array(), $parent_candidates = array()) {
  drupal_alter('menu_link', $item);

  // This is the easiest way to handle the unique internal path '<front>',
  // since a path marked as external does not need to match a router path.
  $item['external'] = (url_is_external($item['link_path'])  || $item['link_path'] == '<front>') ? 1 : 0;
  // Load defaults.
  $item += array(
    'menu_name' => 'navigation',
    'weight' => 0,
    'link_title' => '',
    'hidden' => 0,
    'has_children' => 0,
    'expanded' => 0,
    'options' => array(),
    'module' => 'menu',
    'customized' => 0,
    'updated' => 0,
  );
  if (isset($item['mlid'])) {
    if (!$existing_item) {
      $existing_item = db_query('SELECT * FROM {menu_links} WHERE mlid = :mlid', array('mlid' => $item['mlid']))->fetchAssoc();
    }
    if ($existing_item) {
      $existing_item['options'] = unserialize($existing_item['options']);
    }
  }
  else {
    $existing_item = FALSE;
  }

  // Try to find a parent link. If found, assign it and derive its menu.
  $parent = _menu_link_find_parent($item, $parent_candidates);
  if (!empty($parent['mlid'])) {
    $item['plid'] = $parent['mlid'];
    $item['menu_name'] = $parent['menu_name'];
  }
  // If no corresponding parent link was found, move the link to the top-level.
  else {
    $item['plid'] = 0;
  }
  $menu_name = $item['menu_name'];

  if (!$existing_item) {
    $item['mlid'] = db_insert('menu_links')
      ->fields(array(
        'menu_name' => $item['menu_name'],
        'plid' => $item['plid'],
        'link_path' => $item['link_path'],
        'hidden' => $item['hidden'],
        'external' => $item['external'],
        'has_children' => $item['has_children'],
        'expanded' => $item['expanded'],
        'weight' => (int) $item['weight'],
        'module' => $item['module'],
        'link_title' => $item['link_title'],
        'options' => serialize($item['options']),
        'customized' => $item['customized'],
        'updated' => $item['updated'],
      ))
      ->execute();
  }

  // Directly fill parents for top-level links.
  if ($item['plid'] == 0) {
    $item['p1'] = $item['mlid'];
    for ($i = 2; $i <= MENU_MAX_DEPTH; $i++) {
      $item["p$i"] = 0;
    }
    $item['depth'] = 1;
  }
  // Otherwise, ensure that this link's depth is not beyond the maximum depth
  // and fill parents based on the parent link.
  else {
    if ($item['has_children'] && $existing_item) {
      $limit = MENU_MAX_DEPTH - menu_link_children_relative_depth($existing_item) - 1;
    }
    else {
      $limit = MENU_MAX_DEPTH - 1;
    }
    if ($parent['depth'] > $limit) {
      return FALSE;
    }
    $item['depth'] = $parent['depth'] + 1;
    _menu_link_parents_set($item, $parent);
  }
  // Need to check both plid and menu_name, since plid can be 0 in any menu.
  if ($existing_item && ($item['plid'] != $existing_item['plid'] || $menu_name != $existing_item['menu_name'])) {
    _menu_link_move_children($item, $existing_item);
  }
  // Find the router_path.
  if (empty($item['router_path'])  || !$existing_item || ($existing_item['link_path'] != $item['link_path'])) {
    if ($item['external']) {
      $item['router_path'] = '';
    }
    else {
      // Find the router path which will serve this path.
      $item['parts'] = explode('/', $item['link_path'], MENU_MAX_PARTS);
      $item['router_path'] = _menu_find_router_path($item['link_path']);
    }
  }
  // If every value in $existing_item is the same in the $item, there is no
  // reason to run the update queries or clear the caches. We use
  // array_intersect_key() with the $item as the first parameter because
  // $item may have additional keys left over from building a router entry.
  // The intersect removes the extra keys, allowing a meaningful comparison.
  if (!$existing_item || (array_intersect_key($item, $existing_item) != $existing_item)) {
    db_update('menu_links')
      ->fields(array(
        'menu_name' => $item['menu_name'],
        'plid' => $item['plid'],
        'link_path' => $item['link_path'],
        'router_path' => $item['router_path'],
        'hidden' => $item['hidden'],
        'external' => $item['external'],
        'has_children' => $item['has_children'],
        'expanded' => $item['expanded'],
        'weight' => (int) $item['weight'],
        'depth' => $item['depth'],
        'p1' => $item['p1'],
        'p2' => $item['p2'],
        'p3' => $item['p3'],
        'p4' => $item['p4'],
        'p5' => $item['p5'],
        'p6' => $item['p6'],
        'p7' => $item['p7'],
        'p8' => $item['p8'],
        'p9' => $item['p9'],
        'module' => $item['module'],
        'link_title' => $item['link_title'],
        'options' => serialize($item['options']),
        'customized' => $item['customized'],
      ))
      ->condition('mlid', $item['mlid'])
      ->execute();
    // Check the has_children status of the parent.
    _menu_update_parental_status($item);
    menu_cache_clear($menu_name);
    if ($existing_item && $menu_name != $existing_item['menu_name']) {
      menu_cache_clear($existing_item['menu_name']);
    }
    // Notify modules we have acted on a menu item.
    $hook = 'menu_link_insert';
    if ($existing_item) {
      $hook = 'menu_link_update';
    }
    module_invoke_all($hook, $item);
    // Now clear the cache.
    _menu_clear_page_cache();
  }
  return $item['mlid'];
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
