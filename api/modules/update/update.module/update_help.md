# update_help()

- **Type:** Function
- **File:** [`modules/update/update.module`](_file.md), lines 79–106 · [local source](../../../../source/modules/update/update.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module#L79-L106)
- **Module/theme:** update
- **Implements:** [hook_help()](../../system/system.api.php/hook_help.md)

## Signature

```php
function update_help($path, $arg)
```

## Documentation

```text
Implements hook_help().
```

## Code

```php
function update_help($path, $arg) {
  switch ($path) {
    case 'admin/reports/updates':
      return '<p>' . t('Here you can find information about available updates for your installed modules and themes. Note that each module or theme is part of a "project", which may or may not have the same name, and might include multiple modules or themes within it.') . '</p>';

    case 'admin/help#update':
      $output = '';
      $output .= '<h3>' . t('About') . '</h3>';
      $output .= '<p>' . t("The Update manager module periodically checks for new versions of your site's software (including contributed modules and themes), and alerts administrators to available updates. In order to provide update information, anonymous usage statistics are sent to Drupal.org. If desired, you may disable the Update manager module from the <a href='@modules'>Module administration page</a>. For more information, see the online handbook entry for <a href='@update'>Update manager module</a>.", array('@update' => 'http://drupal.org/documentation/modules/update', '@modules' => url('admin/modules'))) . '</p>';
      // Only explain the Update manager if it has not been disabled.
      if (update_manager_access()) {
        $output .= '<p>' . t('The Update manager also allows administrators to update and install modules and themes through the administration interface.') . '</p>';
      }
      $output .= '<h3>' . t('Uses') . '</h3>';
      $output .= '<dl>';
      $output .= '<dt>' . t('Checking for available updates') . '</dt>';
      $output .= '<dd>' . t('A report of <a href="@update-report">available updates</a> will alert you when new releases are available for download. You may configure options for the frequency for checking updates (which are performed during <a href="@cron">cron</a> runs) and e-mail notifications at the <a href="@update-settings">Update manager settings</a>  page.', array('@update-report' => url('admin/reports/updates'), '@cron' => 'http://drupal.org/cron', '@update-settings' => url('admin/reports/updates/settings'))) . '</dd>';
      // Only explain the Update manager if it has not been disabled.
      if (update_manager_access()) {
        $output .= '<dt>' . t('Performing updates through the user interface') . '</dt>';
        $output .= '<dd>' . t('The Update manager module allows administrators to perform updates directly through the administration interface. At the top of the <a href="@modules_page">modules</a> and <a href="@themes_page">themes</a> pages you will see a link to update to new releases. This will direct you to the <a href="@update-page">update page</a> where you see a listing of all the missing updates and confirm which ones you want to upgrade. From there, you are prompted for your FTP/SSH password, which then transfers the files into your Drupal installation, overwriting your old files. More detailed instructions can be found in the <a href="@update">online handbook</a>.', array('@modules_page' => url('admin/modules'), '@themes_page' => url('admin/appearance'),  '@update-page' => url('admin/reports/updates/update'), '@update' => 'http://drupal.org/documentation/modules/update')) . '</dd>';
        $output .= '<dt>' . t('Installing new modules and themes through the user interface') . '</dt>';
        $output .= '<dd>' . t('You can also install new modules and themes in the same fashion, through the <a href="@install">install page</a>, or by clicking the <em>Install new module/theme</em> link at the top of the <a href="@modules_page">modules</a> and <a href="@themes_page">themes</a> pages. In this case, you are prompted to provide either the URL to the download, or to upload a packaged release file from your local computer.', array('@modules_page' => url('admin/modules'), '@themes_page' => url('admin/appearance'), '@install' => url('admin/reports/updates/install'))) . '</dd>';
      }
      $output .= '</dl>';
      return $output;
  }
}
```

---
_Drupal 7.103 · [modules/update/update.module](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module) · Licensed GPL-2.0-or-later (see LICENSE)._
