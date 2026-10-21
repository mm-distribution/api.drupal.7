# menu_edit_menu_submit()

- **Type:** Function
- **File:** [`modules/menu/menu.admin.inc`](_file.md), lines 605–635 · [local source](../../../../source/modules/menu/menu.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.admin.inc#L605-L635)
- **Module/theme:** menu

## Signature

```php
function menu_edit_menu_submit($form, &$form_state)
```

## Documentation

```text
Submit function for adding or editing a custom menu.
```

## Code

```php
function menu_edit_menu_submit($form, &$form_state) {
  $menu = $form_state['values'];
  $path = 'admin/structure/menu/manage/';
  if ($form['#insert']) {
    // Add 'menu-' to the menu name to help avoid name-space conflicts.
    $menu['menu_name'] = 'menu-' . $menu['menu_name'];
    $link['link_title'] = $menu['title'];
    $link['link_path'] = $path . $menu['menu_name'];
    $link['router_path'] = $path . '%';
    $link['module'] = 'menu';
    $link['plid'] = db_query("SELECT mlid FROM {menu_links} WHERE link_path = :link AND module = :module", array(
      ':link' => 'admin/structure/menu',
      ':module' => 'system'
    ))
    ->fetchField();

    menu_link_save($link);
    menu_save($menu);
  }
  else {
    menu_save($menu);
    $result = db_query("SELECT mlid FROM {menu_links} WHERE link_path = :path", array(':path' => $path . $menu['menu_name']), array('fetch' => PDO::FETCH_ASSOC));
    foreach ($result as $m) {
      $link = menu_link_load($m['mlid']);
      $link['link_title'] = $menu['title'];
      menu_link_save($link);
    }
  }
  drupal_set_message(t('Your configuration has been saved.'));
  $form_state['redirect'] = $path . $menu['menu_name'];
}
```

---
_Drupal 7.103 · [modules/menu/menu.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
