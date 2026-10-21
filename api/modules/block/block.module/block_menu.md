# block_menu()

- **Type:** Function
- **File:** [`modules/block/block.module`](_file.md), lines 106–178 · [local source](../../../../source/modules/block/block.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module#L106-L178)
- **Module/theme:** block
- **Implements:** [hook_menu()](../../system/system.api.php/hook_menu.md)

## Signature

```php
function block_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function block_menu() {
  $default_theme = variable_get('theme_default', 'bartik');
  $items['admin/structure/block'] = array(
    'title' => 'Blocks',
    'description' => 'Configure what block content appears in your site\'s sidebars and other regions.',
    'page callback' => 'block_admin_display',
    'page arguments' => array($default_theme),
    'access arguments' => array('administer blocks'),
    'file' => 'block.admin.inc',
  );
  $items['admin/structure/block/manage/%/%'] = array(
    'title' => 'Configure block',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('block_admin_configure', 4, 5),
    'access arguments' => array('administer blocks'),
    'file' => 'block.admin.inc',
  );
  $items['admin/structure/block/manage/%/%/configure'] = array(
    'title' => 'Configure block',
    'type' => MENU_DEFAULT_LOCAL_TASK,
    'context' => MENU_CONTEXT_INLINE,
  );
  $items['admin/structure/block/manage/%/%/delete'] = array(
    'title' => 'Delete block',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('block_custom_block_delete', 4, 5),
    'access arguments' => array('administer blocks'),
    'type' => MENU_LOCAL_TASK,
    'context' => MENU_CONTEXT_NONE,
    'file' => 'block.admin.inc',
  );
  $items['admin/structure/block/add'] = array(
    'title' => 'Add block',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('block_add_block_form'),
    'access arguments' => array('administer blocks'),
    'type' => MENU_LOCAL_ACTION,
    'file' => 'block.admin.inc',
  );
  foreach (list_themes() as $key => $theme) {
    $items['admin/structure/block/list/' . $key] = array(
      'title' => $theme->info['name'],
      'page arguments' => array($key),
      'type' => $key == $default_theme ? MENU_DEFAULT_LOCAL_TASK : MENU_LOCAL_TASK,
      'weight' => $key == $default_theme ? -10 : 0,
      'access callback' => '_block_themes_access',
      'access arguments' => array($theme),
      'file' => 'block.admin.inc',
    );
    if ($key != $default_theme) {
      $items['admin/structure/block/list/' . $key . '/add'] = array(
        'title' => 'Add block',
        'page callback' => 'drupal_get_form',
        'page arguments' => array('block_add_block_form'),
        'access arguments' => array('administer blocks'),
        'type' => MENU_LOCAL_ACTION,
        'file' => 'block.admin.inc',
      );
    }
    $items['admin/structure/block/demo/' . $key] = array(
      'title' => $theme->info['name'],
      'page callback' => 'block_admin_demo',
      'page arguments' => array($key),
      'type' => MENU_CALLBACK,
      'access callback' => '_block_themes_access',
      'access arguments' => array($theme),
      'theme callback' => '_block_custom_theme',
      'theme arguments' => array($key),
      'file' => 'block.admin.inc',
    );
  }
  return $items;
}
```

---
_Drupal 7.103 · [modules/block/block.module](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module) · Licensed GPL-2.0-or-later (see LICENSE)._
