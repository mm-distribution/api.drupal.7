# system_help()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 77–154 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L77-L154)
- **Module/theme:** system
- **Implements:** [hook_help()](../system.api.php/hook_help.md)

## Signature

```php
function system_help($path, $arg)
```

## Documentation

```text
Implements hook_help().
```

## Code

```php
function system_help($path, $arg) {
  global $base_url;

  switch ($path) {
    case 'admin/help#system':
      $output = '';
      $output .= '<h3>' . t('About') . '</h3>';
      $output .= '<p>' . t('The System module is integral to the site, and provides basic but extensible functionality for use by other modules and themes. Some integral elements of Drupal are contained in and managed by the System module, including caching, enabling and disabling modules and themes, preparing and displaying the administrative page, and configuring fundamental site settings. A number of key system maintenance operations are also part of the System module. For more information, see the online handbook entry for <a href="@system">System module</a>.', array('@system' => 'http://drupal.org/documentation/modules/system')) . '</p>';
      $output .= '<h3>' . t('Uses') . '</h3>';
      $output .= '<dl>';
      $output .= '<dt>' . t('Managing modules') . '</dt>';
      $output .= '<dd>' . t('The System module allows users with the appropriate permissions to enable and disable modules on the <a href="@modules">Modules administration page</a>. Drupal comes with a number of core modules, and each module provides a discrete set of features and may be enabled or disabled depending on the needs of the site. Many additional modules contributed by members of the Drupal community are available for download at the <a href="@drupal-modules">Drupal.org module page</a>.', array('@modules' => url('admin/modules'), '@drupal-modules' => 'http://drupal.org/project/modules')) . '</dd>';
      $output .= '<dt>' . t('Managing themes') . '</dt>';
      $output .= '<dd>' . t('The System module allows users with the appropriate permissions to enable and disable themes on the <a href="@themes">Appearance administration page</a>. Themes determine the design and presentation of your site. Drupal comes packaged with several core themes, and additional contributed themes are available at the <a href="@drupal-themes">Drupal.org theme page</a>.', array('@themes' => url('admin/appearance'), '@drupal-themes' => 'http://drupal.org/project/themes')) . '</dd>';
      $output .= '<dt>' . t('Managing caching') . '</dt>';
      $output .= '<dd>' . t("The System module allows users with the appropriate permissions to manage caching on the <a href='@cache-settings'>Performance settings page</a>. Drupal has a robust caching system that allows the efficient re-use of previously-constructed web pages and web page components. Pages requested by anonymous users are stored in a compressed format; depending on your site configuration and the amount of your web traffic tied to anonymous visitors, the caching system may significantly increase the speed of your site.", array('@cache-settings' => url('admin/config/development/performance'))) . '</dd>';
      $output .= '<dt>' . t('Performing system maintenance') . '</dt>';
      $output .= '<dd>' . t('In order for the site and its modules to continue to operate well, a set of routine administrative operations must run on a regular basis. The System module manages this task by making use of a system cron job. You can verify the status of cron tasks by visiting the <a href="@status">Status report page</a>. For more information, see the online handbook entry for <a href="@handbook">configuring cron jobs</a>. You can set up cron job by visiting <a href="@cron">Cron configuration</a> page', array('@status' => url('admin/reports/status'), '@handbook' => 'http://drupal.org/cron', '@cron' => url('admin/config/system/cron'))) . '</dd>';
      $output .= '<dt>' . t('Configuring basic site settings') . '</dt>';
      $output .= '<dd>' . t('The System module also handles basic configuration options for your site, including <a href="@date-time-settings">Date and time settings</a>, <a href="@file-system">File system settings</a>, <a href="@clean-url">Clean URL support</a>, <a href="@site-info">Site name and other information</a>, and a <a href="@maintenance-mode">Maintenance mode</a> for taking your site temporarily offline.', array('@date-time-settings' => url('admin/config/regional/date-time'), '@file-system' => url('admin/config/media/file-system'), '@clean-url' => url('admin/config/search/clean-urls'), '@site-info' => url('admin/config/system/site-information'), '@maintenance-mode' => url('admin/config/development/maintenance'))) . '</dd>';
      $output .= '<dt>' . t('Configuring actions') . '</dt>';
      $output .= '<dd>' . t('Actions are individual tasks that the system can do, such as unpublishing a piece of content or banning a user. Modules, such as the <a href="@trigger-help">Trigger module</a>, can fire these actions when certain system events happen; for example, when a new post is added or when a user logs in. Modules may also provide additional actions. Visit the <a href="@actions">Actions page</a> to configure actions.', array('@trigger-help' => url('admin/help/trigger'), '@actions' => url('admin/config/system/actions'))) . '</dd>';
      $output .= '</dl>';
      return $output;
    case 'admin/index':
      return '<p>' . t('This page shows you all available administration tasks for each module.') . '</p>';
    case 'admin/appearance':
      $output = '<p>' . t('Set and configure the default theme for your website.  Alternative <a href="@themes">themes</a> are available.', array('@themes' => 'http://drupal.org/project/themes')) . '</p>';
      return $output;
    case 'admin/appearance/settings/' . $arg[3]:
      $theme_list = list_themes();
      $theme = $theme_list[$arg[3]];
      return '<p>' . t('These options control the display settings for the %name theme. When your site is displayed using this theme, these settings will be used.', array('%name' => $theme->info['name'])) . '</p>';
    case 'admin/appearance/settings':
      return '<p>' . t('These options control the default display settings for your entire site, across all themes. Unless they have been overridden by a specific theme, these settings will be used.') . '</p>';
    case 'admin/modules':
      $output = '<p>' . t('Download additional <a href="@modules">contributed modules</a> to extend Drupal\'s functionality.', array('@modules' => 'http://drupal.org/project/modules')) . '</p>';
      if (module_exists('update')) {
        if (update_manager_access()) {
          $output .= '<p>' . t('Regularly review and install <a href="@updates">available updates</a> to maintain a secure and current site. Always run the <a href="@update-php">update script</a> each time a module is updated.', array('@update-php' => $base_url . '/update.php', '@updates' => url('admin/reports/updates'))) . '</p>';
        }
        else {
          $output .= '<p>' . t('Regularly review <a href="@updates">available updates</a> to maintain a secure and current site. Always run the <a href="@update-php">update script</a> each time a module is updated.', array('@update-php' => $base_url . '/update.php', '@updates' => url('admin/reports/updates'))) . '</p>';
        }
      }
      else {
        $output .= '<p>' . t('Regularly review available updates to maintain a secure and current site. Always run the <a href="@update-php">update script</a> each time a module is updated. Enable the Update manager module to update and install modules and themes.', array('@update-php' => $base_url . '/update.php')) . '</p>';
      }
      return $output;
    case 'admin/modules/uninstall':
      return '<p>' . t('The uninstall process removes all data related to a module. To uninstall a module, you must first disable it on the main <a href="@modules">Modules page</a>.', array('@modules' => url('admin/modules'))) . '</p>';
    case 'admin/structure/block/manage':
      if ($arg[4] == 'system' && $arg[5] == 'powered-by') {
        return '<p>' . t('The <em>Powered by Drupal</em> block is an optional link to the home page of the Drupal project. While there is absolutely no requirement that sites feature this link, it may be used to show support for Drupal.') . '</p>';
      }
      break;
    case 'admin/config/development/maintenance':
      global $user;
      if ($user->uid == 1) {
        return '<p>' . t('If you are upgrading to a newer version of Drupal or upgrading contributed modules or themes, you may need to run the <a href="@update-php">update script</a>.', array('@update-php' => $base_url . '/update.php')) . '</p>';
      }
      break;
    case 'admin/config/system/actions':
    case 'admin/config/system/actions/manage':
      $output = '';
      $output .= '<p>' . t('There are two types of actions: simple and advanced. Simple actions do not require any additional configuration, and are listed here automatically. Advanced actions need to be created and configured before they can be used, because they have options that need to be specified; for example, sending an e-mail to a specified address, or unpublishing content containing certain words. To create an advanced action, select the action from the drop-down list in the advanced action section below and click the <em>Create</em> button.') . '</p>';
      if (module_exists('trigger')) {
        $output .= '<p>' . t('You may proceed to the <a href="@url">Triggers</a> page to assign these actions to system events.', array('@url' => url('admin/structure/trigger'))) . '</p>';
      }
      return $output;
    case 'admin/config/system/actions/configure':
      return t('An advanced action offers additional configuration options which may be filled out below. Changing the <em>Description</em> field is recommended, in order to better identify the precise action taking place. This description will be displayed in modules such as the Trigger module when assigning actions to system events, so it is best if it is as descriptive as possible (for example, "Send e-mail to Moderation Team" rather than simply "Send e-mail").');
    case 'admin/config/people/ip-blocking':
      return '<p>' . t('IP addresses listed here are blocked from your site. Blocked addresses are completely forbidden from accessing the site and instead see a brief message explaining the situation.') . '</p>';
    case 'admin/reports/status':
      return '<p>' . t("Here you can find a short overview of your site's parameters as well as any problems detected with your installation. It may be useful to copy and paste this information into support requests filed on drupal.org's support forums and project issue queues.") . '</p>';
  }
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
