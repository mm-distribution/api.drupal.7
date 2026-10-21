# trigger_menu()

- **Type:** Function
- **File:** [`modules/trigger/trigger.module`](_file.md), lines 42–76 · [local source](../../../../source/modules/trigger/trigger.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module#L42-L76)
- **Module/theme:** trigger
- **Implements:** [hook_menu()](../../system/system.api.php/hook_menu.md)

## Signature

```php
function trigger_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function trigger_menu() {
  $items['admin/structure/trigger'] = array(
    'title' => 'Triggers',
    'description' => 'Configure when to execute actions.',
    'page callback' => 'trigger_assign',
    'access arguments' => array('administer actions'),
    'file' => 'trigger.admin.inc',
  );

  $trigger_info = _trigger_tab_information();
  foreach ($trigger_info as $module => $module_name) {
    $items["admin/structure/trigger/$module"] = array(
      'title' => $module_name,
      'page callback' => 'trigger_assign',
      'page arguments' => array($module),
      'access arguments' => array('administer actions'),
      'type' => MENU_LOCAL_TASK,
      'file' => 'trigger.admin.inc',
    );
  }

  $items['admin/structure/trigger/unassign'] = array(
    'title' => 'Unassign',
    'description' => 'Unassign an action from a trigger.',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('trigger_unassign'),
    // Only accessible if there are any actions that can be unassigned.
    'access callback' => 'trigger_menu_unassign_access',
    // Only output in the breadcrumb, not in menu trees.
    'type' => MENU_VISIBLE_IN_BREADCRUMB,
    'file' => 'trigger.admin.inc',
  );

  return $items;
}
```

---
_Drupal 7.103 · [modules/trigger/trigger.module](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module) · Licensed GPL-2.0-or-later (see LICENSE)._
