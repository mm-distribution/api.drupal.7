# menu_overview_page()

- **Type:** Function
- **File:** [`modules/menu/menu.admin.inc`](_file.md), lines 11–24 · [local source](../../../../source/modules/menu/menu.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.admin.inc#L11-L24)
- **Module/theme:** menu

## Signature

```php
function menu_overview_page()
```

## Documentation

```text
Menu callback which shows an overview page of all the custom menus and their descriptions.
```

## Code

```php
function menu_overview_page() {
  $result = db_query("SELECT * FROM {menu_custom} ORDER BY title", array(), array('fetch' => PDO::FETCH_ASSOC));
  $header = array(t('Title'), array('data' => t('Operations'), 'colspan' => '3'));
  $rows = array();
  foreach ($result as $menu) {
    $row = array(theme('menu_admin_overview', array('title' => $menu['title'], 'name' => $menu['menu_name'], 'description' => $menu['description'])));
    $row[] = array('data' => l(t('list links'), 'admin/structure/menu/manage/' . $menu['menu_name']));
    $row[] = array('data' => l(t('edit menu'), 'admin/structure/menu/manage/' . $menu['menu_name'] . '/edit'));
    $row[] = array('data' => l(t('add link'), 'admin/structure/menu/manage/' . $menu['menu_name'] . '/add'));
    $rows[] = $row;
  }

  return theme('table', array('header' => $header, 'rows' => $rows));
}
```

---
_Drupal 7.103 · [modules/menu/menu.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
