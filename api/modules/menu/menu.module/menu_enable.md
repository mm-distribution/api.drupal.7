# menu_enable()

- **Type:** Function
- **File:** [`modules/menu/menu.module`](_file.md), lines 180–202 · [local source](../../../../source/modules/menu/menu.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module#L180-L202)
- **Module/theme:** menu
- **Implements:** [hook_enable()](../../system/system.api.php/hook_enable.md)

## Signature

```php
function menu_enable()
```

## Documentation

```text
Implements hook_enable().

Add a link for each custom menu.
```

## Code

```php
function menu_enable() {
  menu_rebuild();
  $base_link = db_query("SELECT mlid AS plid, menu_name FROM {menu_links} WHERE link_path = 'admin/structure/menu' AND module = 'system'")->fetchAssoc();
  $base_link['router_path'] = 'admin/structure/menu/manage/%';
  $base_link['module'] = 'menu';
  $result = db_query("SELECT * FROM {menu_custom}", array(), array('fetch' => PDO::FETCH_ASSOC));
  foreach ($result as $menu) {
    // $link is passed by reference to menu_link_save(), so we make a copy of $base_link.
    $link = $base_link;
    $link['mlid'] = 0;
    $link['link_title'] = $menu['title'];
    $link['link_path'] = 'admin/structure/menu/manage/' . $menu['menu_name'];
    $menu_link = db_query("SELECT mlid FROM {menu_links} WHERE link_path = :path AND plid = :plid", array(
      ':path' => $link['link_path'],
      ':plid' => $link['plid']
    ))
    ->fetchField();
    if (!$menu_link) {
      menu_link_save($link);
    }
  }
  menu_cache_clear_all();
}
```

---
_Drupal 7.103 · [modules/menu/menu.module](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module) · Licensed GPL-2.0-or-later (see LICENSE)._
