# shortcut_menu()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.module`](_file.md), lines 69–162 · [local source](../../../../source/modules/shortcut/shortcut.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module#L69-L162)
- **Module/theme:** shortcut
- **Implements:** [hook_menu()](../../system/system.api.php/hook_menu.md)

## Signature

```php
function shortcut_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function shortcut_menu() {
  $items['admin/config/user-interface/shortcut'] = array(
    'title' => 'Shortcuts',
    'description' => 'Add and modify shortcut sets.',
    'page callback' => 'shortcut_set_admin',
    'access arguments' => array('administer shortcuts'),
    'file' => 'shortcut.admin.inc',
  );
  $items['admin/config/user-interface/shortcut/add-set'] = array(
    'title' => 'Add shortcut set',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('shortcut_set_add_form'),
    'access arguments' => array('administer shortcuts'),
    'type' => MENU_LOCAL_ACTION,
    'file' => 'shortcut.admin.inc',
  );
  $items['admin/config/user-interface/shortcut/%shortcut_set'] = array(
    'title' => 'Edit shortcuts',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('shortcut_set_customize', 4),
    'title callback' => 'shortcut_set_title_callback',
    'title arguments' => array(4),
    'access callback' => 'shortcut_set_edit_access',
    'access arguments' => array(4),
    'file' => 'shortcut.admin.inc',
  );
  $items['admin/config/user-interface/shortcut/%shortcut_set/links'] = array(
    'title' => 'List links',
    'type' => MENU_DEFAULT_LOCAL_TASK,
  );
  $items['admin/config/user-interface/shortcut/%shortcut_set/edit'] = array(
    'title' => 'Edit set name',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('shortcut_set_edit_form', 4),
    'access callback' => 'shortcut_set_edit_access',
    'access arguments' => array(4),
    'type' => MENU_LOCAL_TASK,
    'file' => 'shortcut.admin.inc',
    'weight' => 10,
  );
  $items['admin/config/user-interface/shortcut/%shortcut_set/delete'] = array(
    'title' => 'Delete shortcut set',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('shortcut_set_delete_form', 4),
    'access callback' => 'shortcut_set_delete_access',
    'access arguments' => array(4),
    'file' => 'shortcut.admin.inc',
  );
  $items['admin/config/user-interface/shortcut/%shortcut_set/add-link'] = array(
    'title' => 'Add shortcut',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('shortcut_link_add', 4),
    'access callback' => 'shortcut_set_edit_access',
    'access arguments' => array(4),
    'type' => MENU_LOCAL_ACTION,
    'file' => 'shortcut.admin.inc',
  );
  $items['admin/config/user-interface/shortcut/%shortcut_set/add-link-inline'] = array(
    'title' => 'Add shortcut',
    'page callback' => 'shortcut_link_add_inline',
    'page arguments' => array(4),
    'access callback' => 'shortcut_set_edit_access',
    'access arguments' => array(4),
    'type' => MENU_CALLBACK,
    'file' => 'shortcut.admin.inc',
  );
  $items['admin/config/user-interface/shortcut/link/%menu_link'] = array(
    'title' => 'Edit shortcut',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('shortcut_link_edit', 5),
    'access callback' => 'shortcut_link_access',
    'access arguments' => array(5),
    'file' => 'shortcut.admin.inc',
  );
  $items['admin/config/user-interface/shortcut/link/%menu_link/delete'] = array(
    'title' => 'Delete shortcut',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('shortcut_link_delete', 5),
    'access callback' => 'shortcut_link_access',
    'access arguments' => array(5),
    'file' => 'shortcut.admin.inc',
  );
  $items['user/%user/shortcuts'] = array(
    'title' => 'Shortcuts',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('shortcut_set_switch', 1),
    'access callback' => 'shortcut_set_switch_access',
    'access arguments' => array(1),
    'type' => MENU_LOCAL_TASK,
    'file' => 'shortcut.admin.inc',
  );

  return $items;
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.module](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module) · Licensed GPL-2.0-or-later (see LICENSE)._
