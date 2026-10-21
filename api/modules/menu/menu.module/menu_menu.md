# menu_menu()

- **Type:** Function
- **File:** [`modules/menu/menu.module`](_file.md), lines 59–157 · [local source](../../../../source/modules/menu/menu.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module#L59-L157)
- **Module/theme:** menu
- **Implements:** [hook_menu()](../../system/system.api.php/hook_menu.md)

## Signature

```php
function menu_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function menu_menu() {
  $items['admin/structure/menu'] = array(
    'title' => 'Menus',
    'description' => 'Add new menus to your site, edit existing menus, and rename and reorganize menu links.',
    'page callback' => 'menu_overview_page',
    'access callback' => 'user_access',
    'access arguments' => array('administer menu'),
    'file' => 'menu.admin.inc',
  );
  $items['admin/structure/menu/parents'] = array(
    'title' => 'Parent menu items',
    'page callback' => 'menu_parent_options_js',
    'type' => MENU_CALLBACK,
    'access arguments' => array('administer menu'),
  );
  $items['admin/structure/menu/list'] = array(
    'title' => 'List menus',
    'type' => MENU_DEFAULT_LOCAL_TASK,
    'weight' => -10,
  );
  $items['admin/structure/menu/add'] = array(
    'title' => 'Add menu',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('menu_edit_menu', 'add'),
    'access arguments' => array('administer menu'),
    'type' => MENU_LOCAL_ACTION,
    'file' => 'menu.admin.inc',
  );
  $items['admin/structure/menu/settings'] = array(
    'title' => 'Settings',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('menu_configure'),
    'access arguments' => array('administer menu'),
    'type' => MENU_LOCAL_TASK,
    'weight' => 5,
    'file' => 'menu.admin.inc',
  );
  $items['admin/structure/menu/manage/%menu'] = array(
    'title' => 'Customize menu',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('menu_overview_form', 4),
    'title callback' => 'menu_overview_title',
    'title arguments' => array(4),
    'access arguments' => array('administer menu'),
    'file' => 'menu.admin.inc',
  );
  $items['admin/structure/menu/manage/%menu/list'] = array(
    'title' => 'List links',
    'weight' => -10,
    'type' => MENU_DEFAULT_LOCAL_TASK,
    'context' => MENU_CONTEXT_PAGE | MENU_CONTEXT_INLINE,
  );
  $items['admin/structure/menu/manage/%menu/add'] = array(
    'title' => 'Add link',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('menu_edit_item', 'add', NULL, 4),
    'access arguments' => array('administer menu'),
    'type' => MENU_LOCAL_ACTION,
    'file' => 'menu.admin.inc',
  );
  $items['admin/structure/menu/manage/%menu/edit'] = array(
    'title' => 'Edit menu',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('menu_edit_menu', 'edit', 4),
    'access arguments' => array('administer menu'),
    'type' => MENU_LOCAL_TASK,
    'context' => MENU_CONTEXT_PAGE | MENU_CONTEXT_INLINE,
    'file' => 'menu.admin.inc',
  );
  $items['admin/structure/menu/manage/%menu/delete'] = array(
    'title' => 'Delete menu',
    'page callback' => 'menu_delete_menu_page',
    'page arguments' => array(4),
    'access arguments' => array('administer menu'),
    'file' => 'menu.admin.inc',
  );
  $items['admin/structure/menu/item/%menu_link/edit'] = array(
    'title' => 'Edit menu link',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('menu_edit_item', 'edit', 4, NULL),
    'access arguments' => array('administer menu'),
    'file' => 'menu.admin.inc',
  );
  $items['admin/structure/menu/item/%menu_link/reset'] = array(
    'title' => 'Reset menu link',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('menu_reset_item_confirm', 4),
    'access arguments' => array('administer menu'),
    'file' => 'menu.admin.inc',
  );
  $items['admin/structure/menu/item/%menu_link/delete'] = array(
    'title' => 'Delete menu link',
    'page callback' => 'menu_item_delete_page',
    'page arguments' => array(4),
    'access arguments' => array('administer menu'),
    'file' => 'menu.admin.inc',
  );
  return $items;
}
```

---
_Drupal 7.103 · [modules/menu/menu.module](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module) · Licensed GPL-2.0-or-later (see LICENSE)._
