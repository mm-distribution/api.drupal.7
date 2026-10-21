# menu_overview_form()

- **Type:** Function
- **File:** [`modules/menu/menu.admin.inc`](_file.md), lines 49–88 · [local source](../../../../source/modules/menu/menu.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.admin.inc#L49-L88)
- **Module/theme:** menu

## Signature

```php
function menu_overview_form($form, &$form_state, $menu)
```

## Documentation

```text
Form for editing an entire menu tree at once.

Shows for one menu the menu links accessible to the current user and
relevant operations.
```

## Code

```php
function menu_overview_form($form, &$form_state, $menu) {
  global $menu_admin;
  $form['#attached']['css'] = array(drupal_get_path('module', 'menu') . '/menu.css');
  $sql = "
    SELECT m.load_functions, m.to_arg_functions, m.access_callback, m.access_arguments, m.page_callback, m.page_arguments, m.delivery_callback, m.title, m.title_callback, m.title_arguments, m.type, m.description, ml.*
    FROM {menu_links} ml LEFT JOIN {menu_router} m ON m.path = ml.router_path
    WHERE ml.menu_name = :menu
    ORDER BY p1 ASC, p2 ASC, p3 ASC, p4 ASC, p5 ASC, p6 ASC, p7 ASC, p8 ASC, p9 ASC";
  $result = db_query($sql, array(':menu' => $menu['menu_name']), array('fetch' => PDO::FETCH_ASSOC));
  $links = array();
  foreach ($result as $item) {
    $links[] = $item;
  }
  $link_count = db_query("SELECT COUNT(*) AS counter FROM {menu_links} WHERE menu_name = :menu AND link_path NOT LIKE :link_path", array(':menu' => $menu['menu_name'], ':link_path' => '%\%%'))->fetchObject();
  $counter = intval($link_count->counter / 2 ) + 1;

  $tree = menu_tree_data($links);
  $node_links = array();
  menu_tree_collect_node_links($tree, $node_links);
  // We indicate that a menu administrator is running the menu access check.
  $menu_admin = TRUE;
  menu_tree_check_access($tree, $node_links);
  $menu_admin = FALSE;

  $delta = _menu_get_menu_weight_delta($menu['menu_name'], $counter);
  $form = array_merge($form, _menu_overview_tree_form($tree, $delta));
  $form['#menu'] =  $menu;

  if (element_children($form)) {
    $form['actions'] = array('#type' => 'actions');
    $form['actions']['submit'] = array(
      '#type' => 'submit',
      '#value' => t('Save configuration'),
    );
  }
  else {
    $form['#empty_text'] = t('There are no menu links yet. <a href="@link">Add link</a>.', array('@link' => url('admin/structure/menu/manage/'. $form['#menu']['menu_name'] .'/add')));
  }
  return $form;
}
```

---
_Drupal 7.103 · [modules/menu/menu.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
