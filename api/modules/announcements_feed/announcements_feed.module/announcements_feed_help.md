# announcements_feed_help()

- **Type:** Function
- **File:** [`modules/announcements_feed/announcements_feed.module`](_file.md), lines 36–49 · [local source](../../../../source/modules/announcements_feed/announcements_feed.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/announcements_feed.module#L36-L49)
- **Module/theme:** announcements_feed
- **Implements:** [hook_help()](../../system/system.api.php/hook_help.md)

## Signature

```php
function announcements_feed_help($path)
```

## Documentation

```text
Implements hook_help().
```

## Code

```php
function announcements_feed_help($path) {
  if ($path == 'admin/help#announcements_feed') {
    $output = '';
    $output .= '<h3>' . t('About') . '</h3>';
    $output .= '<p>' . t('The Announcements module displays announcements from the Drupal community. For more information, see the <a href="@documentation">online documentation for the Announcements module</a>.', array('@documentation' => 'https://www.drupal.org/docs/core-modules-and-themes/core-modules/announcements-feed')) . '</p>';
    $output .= '<h3>' . t('Uses') . '</h3>';
    $output .= '<dl><dt>' . t('Accessing announcements') . '</dt>';
    $output .= '<dd>' . t('Users with the "View drupal.org announcements" permission may click on the "Announcements" item in the administration menu, or access <a href="@link">Announcements</a>, to see all announcements relevant to the Drupal version of your site.', array('@link' => url('admin/announcements_feed'))) . '</dd>';
    $output .= '</dl>';

    return $output;
  }

}
```

---
_Drupal 7.103 · [modules/announcements_feed/announcements_feed.module](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/announcements_feed.module) · Licensed GPL-2.0-or-later (see LICENSE)._
