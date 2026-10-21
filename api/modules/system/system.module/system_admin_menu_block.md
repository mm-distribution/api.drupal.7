# system_admin_menu_block()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 2148–2195 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L2148-L2195)
- **Module/theme:** system

## Signature

```php
function system_admin_menu_block($item)
```

## Documentation

```text
Provide a single block on the administration overview page.

@param $item
  The menu item to be displayed.
```

## Code

```php
function system_admin_menu_block($item) {
  $cache = &drupal_static(__FUNCTION__, array());
  // If we are calling this function for a menu item that corresponds to a
  // local task (for example, admin/tasks), then we want to retrieve the
  // parent item's child links, not this item's (since this item won't have
  // any).
  if ($item['tab_root'] != $item['path']) {
    $item = menu_get_item($item['tab_root_href']);
  }

  if (!isset($item['mlid'])) {
    $item += db_query("SELECT mlid, menu_name FROM {menu_links} ml WHERE ml.router_path = :path AND module = 'system'", array(':path' => $item['path']))->fetchAssoc();
  }

  if (isset($cache[$item['mlid']])) {
    return $cache[$item['mlid']];
  }

  $content = array();
  $query = db_select('menu_links', 'ml', array('fetch' => PDO::FETCH_ASSOC));
  $query->join('menu_router', 'm', 'm.path = ml.router_path');
  $query
    ->fields('ml')
    // Weight should be taken from {menu_links}, not {menu_router}.
    ->fields('m', array_diff(drupal_schema_fields_sql('menu_router'), array('weight')))
    ->condition('ml.plid', $item['mlid'])
    ->condition('ml.menu_name', $item['menu_name'])
    ->condition('ml.hidden', 0);

  foreach ($query->execute() as $link) {
    _menu_link_translate($link);
    if ($link['access']) {
      // The link description, either derived from 'description' in
      // hook_menu() or customized via menu module is used as title attribute.
      if (!empty($link['localized_options']['attributes']['title'])) {
        $link['description'] = $link['localized_options']['attributes']['title'];
        unset($link['localized_options']['attributes']['title']);
      }
      // Prepare for sorting as in function _menu_tree_check_access().
      // The weight is offset so it is always positive, with a uniform 5-digits.
      $key = (50000 + $link['weight']) . ' ' . drupal_strtolower($link['title']) . ' ' . $link['mlid'];
      $content[$key] = $link;
    }
  }
  ksort($content);
  $cache[$item['mlid']] = $content;
  return $content;
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
