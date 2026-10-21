# statistics_help()

- **Type:** Function
- **File:** [`modules/statistics/statistics.module`](_file.md), lines 11–42 · [local source](../../../../source/modules/statistics/statistics.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.module#L11-L42)
- **Module/theme:** statistics
- **Implements:** [hook_help()](../../system/system.api.php/hook_help.md)

## Signature

```php
function statistics_help($path, $arg)
```

## Documentation

```text
Implements hook_help().
```

## Code

```php
function statistics_help($path, $arg) {
  switch ($path) {
    case 'admin/help#statistics':
      $output = '';
      $output .= '<h3>' . t('About') . '</h3>';
      $output .= '<p>' . t('The Statistics module shows you how often a given page is viewed, who viewed it, the previous page the user visited (referrer URL), and when it was viewed. These statistics are useful in determining how users are visiting and navigating your site. For more information, see the online handbook entry for the <a href="@statistics">Statistics module</a>.', array('@statistics' => url('http://drupal.org/documentation/modules/statistics/'))) . '</p>';
      $output .= '<h3>' . t('Uses') . '</h3>';
      $output .= '<dl>';
      $output .= '<dt>' . t('Managing logs') . '</dt>';
      $output .= '<dd>' . t('To enable collection of statistics, the <em>Enable access log</em> checkbox on the <a href="@statistics-settings">Statistics settings page</a> must be checked. The <em>Discard access logs older than</em> setting on the settings page specifies the length of time entries are kept in the log before they are deleted. This setting requires a correctly configured <a href="@cron">cron maintenance task</a> to run.', array('@statistics-settings' => url('admin/config/system/statistics'), '@cron' => 'http://drupal.org/cron')) . '</dd>';
      $output .= '<dt>' . t('Viewing site usage') . '</dt>';
      $output .= '<dd>' . t('The Statistics module can help you break down details about your users and how they are using the site. The module offers four reports:');
      $output .= '<ul><li>' . t('<a href="@recent-hits">Recent hits</a> displays information about the latest activity on your site, including the URL and title of the page that was accessed, the user name (if available) and the IP address of the viewer.', array('@recent-hits' => url('admin/reports/hits'))) . '</li>';
      $output .= '<li>' . t('<a href="@top-referrers">Top referrers</a> displays where visitors came from (referrer URL).', array('@top-referrers' => url('admin/reports/referrers'))) . '</li>';
      $output .= '<li>' . t('<a href="@top-pages">Top pages</a> displays a list of pages ordered by how often they were viewed.', array('@top-pages' => url('admin/reports/pages'))) . '</li>';
      $output .= '<li>' . t('<a href="@top-visitors">Top visitors</a> shows you the most active visitors for your site and allows you to ban abusive visitors.', array('@top-visitors' => url('admin/reports/visitors'))) . '</li></ul>';
      $output .= '<dt>' . t('Displaying popular content') . '</dt>';
      $output .= '<dd>' . t('The module includes a <em>Popular content</em> block that displays the most viewed pages today and for all time, and the last content viewed. To use the block, enable <em>Count content views</em> on the <a href="@statistics-settings">statistics settings page</a>, and then you can enable and configure the block on the <a href="@blocks">blocks administration page</a>.', array('@statistics-settings' => url('admin/config/system/statistics'), '@blocks' => url('admin/structure/block'))) . '</dd>';
      $output .= '<dt>' . t('Page view counter') . '</dt>';
      $output .= '<dd>' . t('The Statistics module includes a counter for each page that increases whenever the page is viewed. To use the counter, enable <em>Count content views</em> on the <a href="@statistics-settings">statistics settings page</a>, and set the necessary <a href="@permissions">permissions</a> (<em>View content hits</em>) so that the counter is visible to the users.', array('@statistics-settings' => url('admin/config/system/statistics'), '@permissions' => url('admin/people/permissions', array('fragment' => 'module-statistics')))) . '</dd>';
      $output .= '</dl>';
      return $output;
    case 'admin/config/system/statistics':
      return '<p>' . t('Settings for the statistical information that Drupal will keep about the site. See <a href="@statistics">site statistics</a> for the actual information.', array('@statistics' => url('admin/reports/hits'))) . '</p>';
    case 'admin/reports/hits':
      return '<p>' . t("This page displays the site's most recent hits.") . '</p>';
    case 'admin/reports/referrers':
      return '<p>' . t('This page displays all external referrers, or external references to your website.') . '</p>';
    case 'admin/reports/visitors':
      return '<p>' . t("When you ban a visitor, you prevent the visitor's IP address from accessing your site. Unlike blocking a user, banning a visitor works even for anonymous users. This is most commonly used to block resource-intensive bots or web crawlers.") . '</p>';
  }
}
```

---
_Drupal 7.103 · [modules/statistics/statistics.module](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.module) · Licensed GPL-2.0-or-later (see LICENSE)._
