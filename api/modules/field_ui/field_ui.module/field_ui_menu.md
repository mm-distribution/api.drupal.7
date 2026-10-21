# field_ui_menu()

- **Type:** Function
- **File:** [`modules/field_ui/field_ui.module`](_file.md), lines 63–210 · [local source](../../../../source/modules/field_ui/field_ui.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.module#L63-L210)
- **Module/theme:** field_ui
- **Implements:** [hook_menu()](../../system/system.api.php/hook_menu.md)

## Signature

```php
function field_ui_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function field_ui_menu() {
  $items['admin/reports/fields'] = array(
    'title' => 'Field list',
    'description' => 'Overview of fields on all entity types.',
    'page callback' => 'field_ui_fields_list',
    'access arguments' => array('administer content types'),
    'type' => MENU_NORMAL_ITEM,
    'file' => 'field_ui.admin.inc',
  );

  // Ensure the following is not executed until field_bundles is working and
  // tables are updated. Needed to avoid errors on initial installation.
  if (defined('MAINTENANCE_MODE')) {
    return $items;
  }

  // Create tabs for all possible bundles.
  foreach (entity_get_info() as $entity_type => $entity_info) {
    if ($entity_info['fieldable']) {
      foreach ($entity_info['bundles'] as $bundle_name => $bundle_info) {
        if (isset($bundle_info['admin'])) {
          // Extract path information from the bundle.
          $path = $bundle_info['admin']['path'];
          // Different bundles can appear on the same path (e.g. %node_type and
          // %comment_node_type). To allow field_ui_menu_load() to extract the
          // actual bundle object from the translated menu router path
          // arguments, we need to identify the argument position of the bundle
          // name string ('bundle argument') and pass that position to the menu
          // loader. The position needs to be casted into a string; otherwise it
          // would be replaced with the bundle name string.
          if (isset($bundle_info['admin']['bundle argument'])) {
            $bundle_arg = $bundle_info['admin']['bundle argument'];
            $bundle_pos = (string) $bundle_arg;
          }
          else {
            $bundle_arg = $bundle_name;
            $bundle_pos = '0';
          }
          // This is the position of the %field_ui_menu placeholder in the
          // items below.
          $field_position = count(explode('/', $path)) + 1;

          // Extract access information, providing defaults.
          $access = array_intersect_key($bundle_info['admin'], drupal_map_assoc(array('access callback', 'access arguments')));
          $access += array(
            'access callback' => 'user_access',
            'access arguments' => array('administer fields'),
          );

          // Add the "administer fields" permission on top of the access
          // restriction because the field UI should only be accessible to
          // trusted users.
          if ($access['access callback'] != 'user_access' || $access['access arguments'] != array('administer fields')) {
            $access = array(
              'access callback' => 'field_ui_admin_access',
              'access arguments' => array($access['access callback'], $access['access arguments']),
            );
          }

          $items["$path/fields"] = array(
            'title' => 'Manage fields',
            'page callback' => 'drupal_get_form',
            'page arguments' => array('field_ui_field_overview_form', $entity_type, $bundle_arg),
            'type' => MENU_LOCAL_TASK,
            'weight' => 1,
            'file' => 'field_ui.admin.inc',
          ) + $access;
          $items["$path/fields/%field_ui_menu"] = array(
            'load arguments' => array($entity_type, $bundle_arg, $bundle_pos, '%map'),
            'title callback' => 'field_ui_menu_title',
            'title arguments' => array($field_position),
            'page callback' => 'drupal_get_form',
            'page arguments' => array('field_ui_field_edit_form', $field_position),
            'file' => 'field_ui.admin.inc',
          ) + $access;
          $items["$path/fields/%field_ui_menu/edit"] = array(
            'load arguments' => array($entity_type, $bundle_arg, $bundle_pos, '%map'),
            'title' => 'Edit',
            'page callback' => 'drupal_get_form',
            'page arguments' => array('field_ui_field_edit_form', $field_position),
            'type' => MENU_DEFAULT_LOCAL_TASK,
            'file' => 'field_ui.admin.inc',
          ) + $access;
          $items["$path/fields/%field_ui_menu/field-settings"] = array(
            'load arguments' => array($entity_type, $bundle_arg, $bundle_pos, '%map'),
            'title' => 'Field settings',
            'page callback' => 'drupal_get_form',
            'page arguments' => array('field_ui_field_settings_form', $field_position),
            'type' => MENU_LOCAL_TASK,
            'file' => 'field_ui.admin.inc',
          ) + $access;
          $items["$path/fields/%field_ui_menu/widget-type"] = array(
            'load arguments' => array($entity_type, $bundle_arg, $bundle_pos, '%map'),
            'title' => 'Widget type',
            'page callback' => 'drupal_get_form',
            'page arguments' => array('field_ui_widget_type_form', $field_position),
            'type' => MENU_LOCAL_TASK,
            'file' => 'field_ui.admin.inc',
          ) + $access;
          $items["$path/fields/%field_ui_menu/delete"] = array(
            'load arguments' => array($entity_type, $bundle_arg, $bundle_pos, '%map'),
            'title' => 'Delete',
            'page callback' => 'drupal_get_form',
            'page arguments' => array('field_ui_field_delete_form', $field_position),
            'type' => MENU_LOCAL_TASK,
            'weight' => 10,
            'file' => 'field_ui.admin.inc',
          ) + $access;

          // 'Manage display' tab.
          $items["$path/display"] = array(
            'title' => 'Manage display',
            'page callback' => 'drupal_get_form',
            'page arguments' => array('field_ui_display_overview_form', $entity_type, $bundle_arg, 'default'),
            'type' => MENU_LOCAL_TASK,
            'weight' => 2,
            'file' => 'field_ui.admin.inc',
          ) + $access;

          // View modes secondary tabs.
          // The same base $path for the menu item (with a placeholder) can be
          // used for all bundles of a given entity type; but depending on
          // administrator settings, each bundle has a different set of view
          // modes available for customisation. So we define menu items for all
          // view modes, and use an access callback to determine which ones are
          // actually visible for a given bundle.
          $weight = 0;
          $view_modes = array('default' => array('label' => t('Default'))) + $entity_info['view modes'];
          foreach ($view_modes as $view_mode => $view_mode_info) {
            $items["$path/display/$view_mode"] = array(
              'title' => $view_mode_info['label'],
              'page arguments' => array('field_ui_display_overview_form', $entity_type, $bundle_arg, $view_mode),
              // The access callback needs to check both the current 'custom
              // display' setting for the view mode, and the overall access
              // rules for the bundle admin pages.
              'access callback' => '_field_ui_view_mode_menu_access',
              'access arguments' => array_merge(array($entity_type, $bundle_arg, $view_mode, $access['access callback']), $access['access arguments']),
              'type' => ($view_mode == 'default' ? MENU_DEFAULT_LOCAL_TASK : MENU_LOCAL_TASK),
              'weight' => ($view_mode == 'default' ? -10 : $weight++),
              'file' => 'field_ui.admin.inc',
            );
          }
        }
      }
    }
  }
  return $items;
}
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.module](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.module) · Licensed GPL-2.0-or-later (see LICENSE)._
