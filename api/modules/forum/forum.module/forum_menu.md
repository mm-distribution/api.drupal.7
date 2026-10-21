# forum_menu()

- **Type:** Function
- **File:** [`modules/forum/forum.module`](_file.md), lines 89–159 · [local source](../../../../source/modules/forum/forum.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module#L89-L159)
- **Module/theme:** forum
- **Implements:** [hook_menu()](../../system/system.api.php/hook_menu.md)

## Signature

```php
function forum_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function forum_menu() {
  $items['forum'] = array(
    'title' => 'Forums',
    'page callback' => 'forum_page',
    'access arguments' => array('access content'),
    'file' => 'forum.pages.inc',
  );
  $items['forum/%forum_forum'] = array(
    'title' => 'Forums',
    'page callback' => 'forum_page',
    'page arguments' => array(1),
    'access arguments' => array('access content'),
    'file' => 'forum.pages.inc',
  );
  $items['admin/structure/forum'] = array(
    'title' => 'Forums',
    'description' => 'Control forum hierarchy settings.',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('forum_overview'),
    'access arguments' => array('administer forums'),
    'file' => 'forum.admin.inc',
  );
  $items['admin/structure/forum/list'] = array(
    'title' => 'List',
    'type' => MENU_DEFAULT_LOCAL_TASK,
    'weight' => -10,
  );
  $items['admin/structure/forum/add/container'] = array(
    'title' => 'Add container',
    'page callback' => 'forum_form_main',
    'page arguments' => array('container'),
    'access arguments' => array('administer forums'),
    'type' => MENU_LOCAL_ACTION,
    'parent' => 'admin/structure/forum',
    'file' => 'forum.admin.inc',
  );
  $items['admin/structure/forum/add/forum'] = array(
    'title' => 'Add forum',
    'page callback' => 'forum_form_main',
    'page arguments' => array('forum'),
    'access arguments' => array('administer forums'),
    'type' => MENU_LOCAL_ACTION,
    'parent' => 'admin/structure/forum',
    'file' => 'forum.admin.inc',
  );
  $items['admin/structure/forum/settings'] = array(
    'title' => 'Settings',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('forum_admin_settings'),
    'access arguments' => array('administer forums'),
    'weight' => 5,
    'type' => MENU_LOCAL_TASK,
    'parent' => 'admin/structure/forum',
    'file' => 'forum.admin.inc',
  );
  $items['admin/structure/forum/edit/container/%taxonomy_term'] = array(
    'title' => 'Edit container',
    'page callback' => 'forum_form_main',
    'page arguments' => array('container', 5),
    'access arguments' => array('administer forums'),
    'file' => 'forum.admin.inc',
  );
  $items['admin/structure/forum/edit/forum/%taxonomy_term'] = array(
    'title' => 'Edit forum',
    'page callback' => 'forum_form_main',
    'page arguments' => array('forum', 5),
    'access arguments' => array('administer forums'),
    'file' => 'forum.admin.inc',
  );
  return $items;
}
```

---
_Drupal 7.103 · [modules/forum/forum.module](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module) · Licensed GPL-2.0-or-later (see LICENSE)._
