# system_menu()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 535–1082 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L535-L1082)
- **Module/theme:** system
- **Implements:** [hook_menu()](../system.api.php/hook_menu.md)

## Signature

```php
function system_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function system_menu() {
  $items['system/files'] = array(
    'title' => 'File download',
    'page callback' => 'file_download',
    'page arguments' => array('private'),
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );
  $items['system/temporary'] = array(
    'title' => 'Temporary files',
    'page callback' => 'file_download',
    'page arguments' => array('temporary'),
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
  );
  $items['system/ajax'] = array(
    'title' => 'AHAH callback',
    'page callback' => 'ajax_form_callback',
    'delivery callback' => 'ajax_deliver',
    'access callback' => TRUE,
    'theme callback' => 'ajax_base_page_theme',
    'type' => MENU_CALLBACK,
    'file path' => 'includes',
    'file' => 'form.inc',
  );
  $items['system/timezone'] = array(
    'title' => 'Time zone',
    'page callback' => 'system_timezone',
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
    'file' => 'system.admin.inc',
  );
  $items['admin'] = array(
    'title' => 'Administration',
    'access arguments' => array('access administration pages'),
    'page callback' => 'system_admin_menu_block_page',
    'weight' => 9,
    'menu_name' => 'management',
    'file' => 'system.admin.inc',
  );
  $items['admin/compact'] = array(
    'title' => 'Compact mode',
    'page callback' => 'system_admin_compact_page',
    'access arguments' => array('access administration pages'),
    'type' => MENU_CALLBACK,
    'file' => 'system.admin.inc',
  );
  $items['admin/tasks'] = array(
    'title' => 'Tasks',
    'type' => MENU_DEFAULT_LOCAL_TASK,
    'weight' => -20,
  );
  $items['admin/index'] = array(
    'title' => 'Index',
    'page callback' => 'system_admin_index',
    'access arguments' => array('access administration pages'),
    'type' => MENU_LOCAL_TASK,
    'weight' => -18,
    'file' => 'system.admin.inc',
  );

  // Menu items that are basically just menu blocks.
  $items['admin/structure'] = array(
    'title' => 'Structure',
    'description' => 'Administer blocks, content types, menus, etc.',
    'position' => 'right',
    'weight' => -8,
    'page callback' => 'system_admin_menu_block_page',
    'access arguments' => array('access administration pages'),
    'file' => 'system.admin.inc',
  );
  // Appearance.
  $items['admin/appearance'] = array(
    'title' => 'Appearance',
    'description' => 'Select and configure your themes.',
    'page callback' => 'system_themes_page',
    'access arguments' => array('administer themes'),
    'position' => 'left',
    'weight' => -6,
    'file' => 'system.admin.inc',
  );
  $items['admin/appearance/list'] = array(
    'title' => 'List',
    'description' => 'Select and configure your theme',
    'type' => MENU_DEFAULT_LOCAL_TASK,
    'weight' => -1,
    'file' => 'system.admin.inc',
  );
  $items['admin/appearance/enable'] = array(
    'title' => 'Enable theme',
    'page callback' => 'system_theme_enable',
    'access arguments' => array('administer themes'),
    'type' => MENU_CALLBACK,
    'file' => 'system.admin.inc',
  );
  $items['admin/appearance/disable'] = array(
    'title' => 'Disable theme',
    'page callback' => 'system_theme_disable',
    'access arguments' => array('administer themes'),
    'type' => MENU_CALLBACK,
    'file' => 'system.admin.inc',
  );
  $items['admin/appearance/default'] = array(
    'title' => 'Set default theme',
    'page callback' => 'system_theme_default',
    'access arguments' => array('administer themes'),
    'type' => MENU_CALLBACK,
    'file' => 'system.admin.inc',
  );
  $items['admin/appearance/settings'] = array(
    'title' => 'Settings',
    'description' => 'Configure default and theme specific settings.',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('system_theme_settings'),
    'access arguments' => array('administer themes'),
    'type' => MENU_LOCAL_TASK,
    'file' => 'system.admin.inc',
    'weight' => 20,
  );
  // Theme configuration subtabs.
  $items['admin/appearance/settings/global'] = array(
    'title' => 'Global settings',
    'type' => MENU_DEFAULT_LOCAL_TASK,
    'weight' => -1,
  );

  foreach (list_themes() as $theme) {
    $items['admin/appearance/settings/' . $theme->name] = array(
      'title' => $theme->info['name'],
      'page arguments' => array('system_theme_settings', $theme->name),
      'type' => MENU_LOCAL_TASK,
      'access callback' => '_system_themes_access',
      'access arguments' => array($theme),
      'file' => 'system.admin.inc',
    );
  }

  // Modules.
  $items['admin/modules'] = array(
    'title' => 'Modules',
    'description' => 'Extend site functionality.',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('system_modules'),
    'access arguments' => array('administer modules'),
    'file' => 'system.admin.inc',
    'weight' => -2,
  );
  $items['admin/modules/list'] = array(
    'title' => 'List',
    'type' => MENU_DEFAULT_LOCAL_TASK,
  );
  $items['admin/modules/list/confirm'] = array(
    'title' => 'List',
    'access arguments' => array('administer modules'),
    'type' => MENU_VISIBLE_IN_BREADCRUMB,
  );
  $items['admin/modules/uninstall'] = array(
    'title' => 'Uninstall',
    'page arguments' => array('system_modules_uninstall'),
    'access arguments' => array('administer modules'),
    'type' => MENU_LOCAL_TASK,
    'file' => 'system.admin.inc',
    'weight' => 20,
  );
  $items['admin/modules/uninstall/confirm'] = array(
    'title' => 'Uninstall',
    'access arguments' => array('administer modules'),
    'type' => MENU_VISIBLE_IN_BREADCRUMB,
    'file' => 'system.admin.inc',
  );

  // Configuration.
  $items['admin/config'] = array(
    'title' => 'Configuration',
    'description' => 'Administer settings.',
    'page callback' => 'system_admin_config_page',
    'access arguments' => array('access administration pages'),
    'file' => 'system.admin.inc',
  );

  // IP address blocking.
  $items['admin/config/people/ip-blocking'] = array(
    'title' => 'IP address blocking',
    'description' => 'Manage blocked IP addresses.',
    'page callback' => 'system_ip_blocking',
    'access arguments' => array('block IP addresses'),
    'file' => 'system.admin.inc',
    'weight' => 10,
  );
  $items['admin/config/people/ip-blocking/delete/%blocked_ip'] = array(
    'title' => 'Delete IP address',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('system_ip_blocking_delete', 5),
    'access arguments' => array('block IP addresses'),
    'file' => 'system.admin.inc',
  );

  // Media settings.
  $items['admin/config/media'] = array(
    'title' => 'Media',
    'description' => 'Media tools.',
    'position' => 'left',
    'weight' => -10,
    'page callback' => 'system_admin_menu_block_page',
    'access arguments' => array('access administration pages'),
    'file' => 'system.admin.inc',
  );
  $items['admin/config/media/file-system'] = array(
    'title' => 'File system',
    'description' => 'Tell Drupal where to store uploaded files and how they are accessed.',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('system_file_system_settings'),
    'access arguments' => array('administer site configuration'),
    'weight' => -10,
    'file' => 'system.admin.inc',
  );
  $items['admin/config/media/image-toolkit'] = array(
    'title' => 'Image toolkit',
    'description' => 'Choose which image toolkit to use if you have installed optional toolkits.',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('system_image_toolkit_settings'),
    'access arguments' => array('administer site configuration'),
    'weight' => 20,
    'file' => 'system.admin.inc',
  );

  // Service settings.
  $items['admin/config/services'] = array(
    'title' => 'Web services',
    'description' => 'Tools related to web services.',
    'position' => 'right',
    'weight' => 0,
    'page callback' => 'system_admin_menu_block_page',
    'access arguments' => array('access administration pages'),
    'file' => 'system.admin.inc',
  );
  $items['admin/config/services/rss-publishing'] = array(
    'title' => 'RSS publishing',
    'description' => 'Configure the site description, the number of items per feed and whether feeds should be titles/teasers/full-text.',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('system_rss_feeds_settings'),
    'access arguments' => array('administer site configuration'),
    'file' => 'system.admin.inc',
  );

  // Development settings.
  $items['admin/config/development'] = array(
    'title' => 'Development',
    'description' => 'Development tools.',
    'position' => 'right',
    'weight' => -10,
    'page callback' => 'system_admin_menu_block_page',
    'access arguments' => array('access administration pages'),
    'file' => 'system.admin.inc',
  );
  $items['admin/config/development/maintenance'] = array(
    'title' => 'Maintenance mode',
    'description' => 'Take the site offline for maintenance or bring it back online.',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('system_site_maintenance_mode'),
    'access arguments' => array('administer site configuration'),
    'file' => 'system.admin.inc',
    'weight' => -10,
  );
  $items['admin/config/development/performance'] = array(
    'title' => 'Performance',
    'description' => 'Enable or disable page caching for anonymous users and set CSS and JS bandwidth optimization options.',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('system_performance_settings'),
    'access arguments' => array('administer site configuration'),
    'file' => 'system.admin.inc',
    'weight' => -20,
  );
  $items['admin/config/development/logging'] = array(
    'title' => 'Logging and errors',
    'description' => "Settings for logging and alerts modules. Various modules can route Drupal's system events to different destinations, such as syslog, database, email, etc.",
    'page callback' => 'drupal_get_form',
    'page arguments' => array('system_logging_settings'),
    'access arguments' => array('administer site configuration'),
    'file' => 'system.admin.inc',
    'weight' => -15,
  );

  // Regional and date settings.
  $items['admin/config/regional'] = array(
    'title' => 'Regional and language',
    'description' => 'Regional settings, localization and translation.',
    'position' => 'left',
    'weight' => -5,
    'page callback' => 'system_admin_menu_block_page',
    'access arguments' => array('access administration pages'),
    'file' => 'system.admin.inc',
  );
  $items['admin/config/regional/settings'] = array(
    'title' => 'Regional settings',
    'description' => "Settings for the site's default time zone and country.",
    'page callback' => 'drupal_get_form',
    'page arguments' => array('system_regional_settings'),
    'access arguments' => array('administer site configuration'),
    'weight' => -20,
    'file' => 'system.admin.inc',
  );
  $items['admin/config/regional/date-time'] = array(
    'title' => 'Date and time',
    'description' => 'Configure display formats for date and time.',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('system_date_time_settings'),
    'access arguments' => array('administer site configuration'),
    'weight' => -15,
    'file' => 'system.admin.inc',
  );
  $items['admin/config/regional/date-time/types'] = array(
    'title' => 'Types',
    'description' => 'Configure display formats for date and time.',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('system_date_time_settings'),
    'access arguments' => array('administer site configuration'),
    'type' => MENU_DEFAULT_LOCAL_TASK,
    'weight' => -10,
    'file' => 'system.admin.inc',
  );
  $items['admin/config/regional/date-time/types/add'] = array(
    'title' => 'Add date type',
    'description' => 'Add new date type.',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('system_add_date_format_type_form'),
    'access arguments' => array('administer site configuration'),
    'type' => MENU_LOCAL_ACTION,
    'weight' => -10,
    'file' => 'system.admin.inc',
  );
  $items['admin/config/regional/date-time/types/%/delete'] = array(
    'title' => 'Delete date type',
    'description' => 'Allow users to delete a configured date type.',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('system_delete_date_format_type_form', 5),
    'access arguments' => array('administer site configuration'),
    'file' => 'system.admin.inc',
  );
  $items['admin/config/regional/date-time/formats'] = array(
    'title' => 'Formats',
    'description' => 'Configure display format strings for date and time.',
    'page callback' => 'system_date_time_formats',
    'access arguments' => array('administer site configuration'),
    'type' => MENU_LOCAL_TASK,
    'weight' => -9,
    'file' => 'system.admin.inc',
  );
  $items['admin/config/regional/date-time/formats/add'] = array(
    'title' => 'Add format',
    'description' => 'Allow users to add additional date formats.',
    'type' => MENU_LOCAL_ACTION,
    'page callback' => 'drupal_get_form',
    'page arguments' => array('system_configure_date_formats_form'),
    'access arguments' => array('administer site configuration'),
    'weight' => -10,
    'file' => 'system.admin.inc',
  );
  $items['admin/config/regional/date-time/formats/%/edit'] = array(
    'title' => 'Edit date format',
    'description' => 'Allow users to edit a configured date format.',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('system_configure_date_formats_form', 5),
    'access arguments' => array('administer site configuration'),
    'file' => 'system.admin.inc',
  );
  $items['admin/config/regional/date-time/formats/%/delete'] = array(
    'title' => 'Delete date format',
    'description' => 'Allow users to delete a configured date format.',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('system_date_delete_format_form', 5),
    'access arguments' => array('administer site configuration'),
    'file' => 'system.admin.inc',
  );
  $items['admin/config/regional/date-time/formats/lookup'] = array(
    'title' => 'Date and time lookup',
    'page callback' => 'system_date_time_lookup',
    'access arguments' => array('administer site configuration'),
    'type' => MENU_CALLBACK,
    'file' => 'system.admin.inc',
  );

  // Search settings.
  $items['admin/config/search'] = array(
    'title' => 'Search and metadata',
    'description' => 'Local site search, metadata and SEO.',
    'position' => 'left',
    'weight' => -10,
    'page callback' => 'system_admin_menu_block_page',
    'access arguments' => array('access administration pages'),
    'file' => 'system.admin.inc',
  );
  $items['admin/config/search/clean-urls'] = array(
    'title' => 'Clean URLs',
    'description' => 'Enable or disable clean URLs for your site.',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('system_clean_url_settings'),
    'access arguments' => array('administer site configuration'),
    'file' => 'system.admin.inc',
    'weight' => 5,
  );
  $items['admin/config/search/clean-urls/check'] = array(
    'title' => 'Clean URL check',
    'page callback' => 'drupal_json_output',
    'page arguments' => array(array('status' => TRUE)),
    'access callback' => TRUE,
    'type' => MENU_CALLBACK,
    'file' => 'system.admin.inc',
  );

  // System settings.
  $items['admin/config/system'] = array(
    'title' => 'System',
    'description' => 'General system related configuration.',
    'position' => 'right',
    'weight' => -20,
    'page callback' => 'system_admin_menu_block_page',
    'access arguments' => array('access administration pages'),
    'file' => 'system.admin.inc',
  );
  $items['admin/config/system/actions'] = array(
    'title' => 'Actions',
    'description' => 'Manage the actions defined for your site.',
    'access arguments' => array('administer actions'),
    'page callback' => 'system_actions_manage',
    'file' => 'system.admin.inc',
  );
  $items['admin/config/system/actions/manage'] = array(
    'title' => 'Manage actions',
    'description' => 'Manage the actions defined for your site.',
    'page callback' => 'system_actions_manage',
    'type' => MENU_DEFAULT_LOCAL_TASK,
    'weight' => -2,
    'file' => 'system.admin.inc',
  );
  $items['admin/config/system/actions/configure'] = array(
    'title' => 'Configure an advanced action',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('system_actions_configure'),
    'access arguments' => array('administer actions'),
    'type' => MENU_VISIBLE_IN_BREADCRUMB,
    'file' => 'system.admin.inc',
  );
  $items['admin/config/system/actions/delete/%actions'] = array(
    'title' => 'Delete action',
    'description' => 'Delete an action.',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('system_actions_delete_form', 5),
    'access arguments' => array('administer actions'),
    'file' => 'system.admin.inc',
  );
  $items['admin/config/system/actions/orphan'] = array(
    'title' => 'Remove orphans',
    'page callback' => 'system_actions_remove_orphans',
    'access arguments' => array('administer actions'),
    'type' => MENU_CALLBACK,
    'file' => 'system.admin.inc',
  );
  $items['admin/config/system/site-information'] = array(
    'title' => 'Site information',
    'description' => 'Change site name, e-mail address, slogan, default front page, and number of posts per page, error pages.',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('system_site_information_settings'),
    'access arguments' => array('administer site configuration'),
    'file' => 'system.admin.inc',
    'weight' => -20,
  );
  $items['admin/config/system/cron'] = array(
    'title' => 'Cron',
    'description' => 'Manage automatic site maintenance tasks.',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('system_cron_settings'),
    'access arguments' => array('administer site configuration'),
    'file' => 'system.admin.inc',
    'weight' => 20,
  );
  // Additional categories
  $items['admin/config/user-interface'] = array(
    'title' => 'User interface',
    'description' => 'Tools that enhance the user interface.',
    'position' => 'right',
    'page callback' => 'system_admin_menu_block_page',
    'access arguments' => array('access administration pages'),
    'file' => 'system.admin.inc',
    'weight' => -15,
  );
  $items['admin/config/workflow'] = array(
    'title' => 'Workflow',
    'description' => 'Content workflow, editorial workflow tools.',
    'position' => 'right',
    'weight' => 5,
    'page callback' => 'system_admin_menu_block_page',
    'access arguments' => array('access administration pages'),
    'file' => 'system.admin.inc',
  );
  $items['admin/config/content'] = array(
    'title' => 'Content authoring',
    'description' => 'Settings related to formatting and authoring content.',
    'position' => 'left',
    'weight' => -15,
    'page callback' => 'system_admin_menu_block_page',
    'access arguments' => array('access administration pages'),
    'file' => 'system.admin.inc',
  );

  // Reports.
  $items['admin/reports'] = array(
    'title' => 'Reports',
    'description' => 'View reports, updates, and errors.',
    'page callback' => 'system_admin_menu_block_page',
    'access arguments' => array('access site reports'),
    'weight' => 5,
    'position' => 'left',
    'file' => 'system.admin.inc',
  );
  $items['admin/reports/status'] = array(
    'title' => 'Status report',
    'description' => "Get a status report about your site's operation and any detected problems.",
    'page callback' => 'system_status',
    'weight' => -60,
    'access arguments' => array('administer site configuration'),
    'file' => 'system.admin.inc',
  );
  $items['admin/reports/status/run-cron'] = array(
    'title' => 'Run cron',
    'page callback' => 'system_run_cron',
    'access arguments' => array('administer site configuration'),
    'type' => MENU_CALLBACK,
    'file' => 'system.admin.inc',
  );
  $items['admin/reports/status/php'] = array(
    'title' => 'PHP',
    'page callback' => 'system_php',
    'access arguments' => array('administer site configuration'),
    'type' => MENU_CALLBACK,
    'file' => 'system.admin.inc',
  );

  // Default page for batch operations.
  $items['batch'] = array(
    'page callback' => 'system_batch_page',
    'access callback' => TRUE,
    'theme callback' => '_system_batch_theme',
    'type' => MENU_CALLBACK,
    'file' => 'system.admin.inc',
  );
  return $items;
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
