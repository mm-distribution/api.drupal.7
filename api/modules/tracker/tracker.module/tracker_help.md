# tracker_help()

- **Type:** Function
- **File:** [`modules/tracker/tracker.module`](_file.md), lines 11–27 · [local source](../../../../source/modules/tracker/tracker.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.module#L11-L27)
- **Module/theme:** tracker
- **Implements:** [hook_help()](../../system/system.api.php/hook_help.md)

## Signature

```php
function tracker_help($path, $arg)
```

## Documentation

```text
Implements hook_help().
```

## Code

```php
function tracker_help($path, $arg) {
  switch ($path) {
    case 'admin/help#tracker':
      $output = '<h3>' . t('About') . '</h3>';
      $output .= '<p>' . t('The Tracker module displays the most recently added and updated content on your site, and allows you to follow new content created by each user. This module has no configuration options. For more information, see the online handbook entry for <a href="@tracker">Tracker module</a>.', array('@tracker' => 'http://drupal.org/documentation/modules/tracker/')) . '</p>';
      $output .= '<h3>' . t('Uses') . '</h3>';
      $output .= '<dl>';
      $output .= '<dt>' . t('Navigation') . '</dt>';
      $output .= '<dd>' . t('The Tracker module adds a new menu item to the Navigation menu, called <em>Recent content</em>. You can configure menu items via the <a href="@menus">Menus administration page</a>.', array('@menus' => url('admin/structure/menu'))) . '</dd>';
      $output .= '<dt>' . t('Tracking new and updated site content') . '</dt>';
      $output .= '<dd>' . t("The <a href='@recent'>Recent content</a> page shows new and updated content in reverse chronological order, listing the content type, title, author's name, number of comments, and time of last update. Content is considered updated when changes occur in the text, or when new comments are added. The <em>My recent content</em> tab limits the list to the currently logged-in user.", array('@recent' => url('tracker'))) . '</dd>';
      $output .= '<dt>' . t('Tracking user-specific content') . '</dt>';
      $output .= '<dd>' . t("To follow a specific user's new and updated content, select the <em>Track</em> tab from the user's profile page.") . '</dd>';
      $output .= '</dl>';
      return $output;
  }
}
```

---
_Drupal 7.103 · [modules/tracker/tracker.module](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.module) · Licensed GPL-2.0-or-later (see LICENSE)._
