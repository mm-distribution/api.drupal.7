# path_menu()

- **Type:** Function
- **File:** [`modules/path/path.module`](_file.md), lines 55–92 · [local source](../../../../source/modules/path/path.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/path/path.module#L55-L92)
- **Module/theme:** path
- **Implements:** [hook_menu()](../../system/system.api.php/hook_menu.md)

## Signature

```php
function path_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function path_menu() {
  $items['admin/config/search/path'] = array(
    'title' => 'URL aliases',
    'description' => "Change your site's URL paths by aliasing them.",
    'page callback' => 'path_admin_overview',
    'access arguments' => array('administer url aliases'),
    'weight' => -5,
    'file' => 'path.admin.inc',
  );
  $items['admin/config/search/path/edit/%path'] = array(
    'title' => 'Edit alias',
    'page callback' => 'path_admin_edit',
    'page arguments' => array(5),
    'access arguments' => array('administer url aliases'),
    'file' => 'path.admin.inc',
  );
  $items['admin/config/search/path/delete/%path'] = array(
    'title' => 'Delete alias',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('path_admin_delete_confirm', 5),
    'access arguments' => array('administer url aliases'),
    'file' => 'path.admin.inc',
  );
  $items['admin/config/search/path/list'] = array(
    'title' => 'List',
    'type' => MENU_DEFAULT_LOCAL_TASK,
    'weight' => -10,
  );
  $items['admin/config/search/path/add'] = array(
    'title' => 'Add alias',
    'page callback' => 'path_admin_edit',
    'access arguments' => array('administer url aliases'),
    'type' => MENU_LOCAL_ACTION,
    'file' => 'path.admin.inc',
  );

  return $items;
}
```

---
_Drupal 7.103 · [modules/path/path.module](https://github.com/drupal/drupal/blob/7.103/modules/path/path.module) · Licensed GPL-2.0-or-later (see LICENSE)._
