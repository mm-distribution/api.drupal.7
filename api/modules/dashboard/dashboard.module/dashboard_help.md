# dashboard_help()

- **Type:** Function
- **File:** [`modules/dashboard/dashboard.module`](_file.md), lines 10–31 · [local source](../../../../source/modules/dashboard/dashboard.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module#L10-L31)
- **Module/theme:** dashboard
- **Implements:** [hook_help()](../../system/system.api.php/hook_help.md)

## Signature

```php
function dashboard_help($path, $arg)
```

## Documentation

```text
Implements hook_help().
```

## Code

```php
function dashboard_help($path, $arg) {
  switch ($path) {
    case 'admin/help#dashboard':
      $output = '';
      $output .= '<h3>' . t('About') . '</h3>';
      $output .= '<p>' . t('The Dashboard module provides a <a href="@dashboard">Dashboard page</a> in the administrative interface for organizing administrative tasks and navigation, and tracking information within your site. The Dashboard page contains blocks, which you can add to and arrange using the drag-and-drop interface that appears when you click on the <em>Customize dashboard</em> link. Within this interface, blocks that are not primarily used for site administration do not appear by default, but can be added via the <em>Add other blocks</em> link. For more information, see the online handbook entry for <a href="@handbook">Dashboard module</a>.', array('@handbook' => 'http://drupal.org/documentation/modules/dashboard', '@dashboard' => url('admin/dashboard'))) . '</p>';
      $output .= '<h3>' . t('Uses') . '</h3>';
      $output .= '<dl>';
      $output .= '<dt>' . t('Tracking user activity') . '</dt>';
      $output .= '<dd>' . t("By enabling blocks such as <em>Who's online</em> and <em>Who's new</em>, site users can track who is logged in and new user signups at a centralized location.") . '</dd>';
      $output .= '<dt>' . t('Tracking content activity') . '</dt>';
      $output .= '<dd>' . t('By enabling blocks such as <em>Recent blog posts</em>, <em>New forum topics</em> and <em>Recent comments</em>, site users can view newly added site content at a glance.') . '</dd>';
      $output .= '</dl>';
      return $output;

    case 'admin/dashboard/configure':
      // @todo This assumes the current page is being displayed using the same
      //   theme that the dashboard is displayed in.
      $output = '<p>' . t('Rearrange blocks for display on the <a href="@dashboard-url">Dashboard page</a>. Blocks placed in the <em>Dashboard (inactive)</em> region are not displayed when viewing the Dashboard page, but are available within its <em>Customize dashboard</em> interface. Removing a block from active dashboard display makes it available on the main <a href="@blocks-url">blocks administration page</a>.', array('@dashboard-url' => url('admin/dashboard'), '@blocks-url' => url("admin/structure/block/list/{$GLOBALS['theme_key']}"))) . '</p>';
      return $output;
  }
}
```

---
_Drupal 7.103 · [modules/dashboard/dashboard.module](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module) · Licensed GPL-2.0-or-later (see LICENSE)._
