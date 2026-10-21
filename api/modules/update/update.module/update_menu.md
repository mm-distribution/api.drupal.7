# update_menu()

- **Type:** Function
- **File:** [`modules/update/update.module`](_file.md), lines 165–249 · [local source](../../../../source/modules/update/update.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module#L165-L249)
- **Module/theme:** update
- **Implements:** [hook_menu()](../../system/system.api.php/hook_menu.md)

## Signature

```php
function update_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function update_menu() {
  $items = array();

  $items['admin/reports/updates'] = array(
    'title' => 'Available updates',
    'description' => 'Get a status report about available updates for your installed modules and themes.',
    'page callback' => 'update_status',
    'access arguments' => array('administer site configuration'),
    'weight' => -50,
    'file' => 'update.report.inc',
  );
  $items['admin/reports/updates/list'] = array(
    'title' => 'List',
    'access arguments' => array('administer site configuration'),
    'type' => MENU_DEFAULT_LOCAL_TASK,
  );
  $items['admin/reports/updates/settings'] = array(
    'title' => 'Settings',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('update_settings'),
    'access arguments' => array('administer site configuration'),
    'file' => 'update.settings.inc',
    'type' => MENU_LOCAL_TASK,
    'weight' => 50,
  );
  $items['admin/reports/updates/check'] = array(
    'title' => 'Manual update check',
    'page callback' => 'update_manual_status',
    'access arguments' => array('administer site configuration'),
    'type' => MENU_CALLBACK,
    'file' => 'update.fetch.inc',
  );

  // We want action links for updating projects at a few different locations:
  // both the module and theme administration pages, and on the available
  // updates report itself. The menu items will be mostly identical, except the
  // paths and titles, so we just define them in a loop. We pass in a string
  // indicating what context we're entering the action from, so that can
  // customize the appearance as needed.
  $paths = array(
    'report' => 'admin/reports/updates',
    'module' => 'admin/modules',
    'theme' => 'admin/appearance',
  );
  foreach ($paths as $context => $path) {
    $items[$path . '/install'] = array(
      'page callback' => 'drupal_get_form',
      'page arguments' => array('update_manager_install_form', $context),
      'access callback' => 'update_manager_access',
      'access arguments' => array(),
      'weight' => 25,
      'type' => MENU_LOCAL_ACTION,
      'file' => 'update.manager.inc',
    );
    $items[$path . '/update'] = array(
      'page callback' => 'drupal_get_form',
      'page arguments' => array('update_manager_update_form', $context),
      'access callback' => 'update_manager_access',
      'access arguments' => array(),
      'weight' => 10,
      'title' => 'Update',
      'type' => MENU_LOCAL_TASK,
      'file' => 'update.manager.inc',
    );
  }
  // Customize the titles of the action links depending on where they appear.
  // We use += array() to let the translation extractor find these menu titles.
  $items['admin/reports/updates/install'] += array('title' => 'Install new module or theme');
  $items['admin/modules/install'] += array('title' => 'Install new module');
  $items['admin/appearance/install'] += array('title' => 'Install new theme');

  // Menu callback used for the confirmation page after all the releases
  // have been downloaded, asking you to backup before installing updates.
  $items['admin/update/ready'] = array(
    'title' => 'Ready to update',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('update_manager_update_ready_form'),
    'access callback' => 'update_manager_access',
    'access arguments' => array(),
    'type' => MENU_CALLBACK,
    'file' => 'update.manager.inc',
  );

  return $items;
}
```

---
_Drupal 7.103 · [modules/update/update.module](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module) · Licensed GPL-2.0-or-later (see LICENSE)._
