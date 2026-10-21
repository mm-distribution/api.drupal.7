# announcements_feed_page_alter()

- **Type:** Function
- **File:** [`modules/announcements_feed/announcements_feed.module`](_file.md), lines 138–143 · [local source](../../../../source/modules/announcements_feed/announcements_feed.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/announcements_feed.module#L138-L143)
- **Module/theme:** announcements_feed
- **Implements:** [hook_page_alter()](../../system/system.api.php/hook_page_alter.md)

## Signature

```php
function announcements_feed_page_alter(&$page)
```

## Documentation

```text
Implements hook_page_alter().
```

## Code

```php
function announcements_feed_page_alter(&$page) {
  if (isset($page['page_top']['toolbar'])) {
    // If the toolbar is available, add a pre-render function to add the class.
    $page['page_top']['toolbar']['#pre_render'][] = 'announcements_feed_toolbar_pre_render_alter';
  }
}
```

---
_Drupal 7.103 · [modules/announcements_feed/announcements_feed.module](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/announcements_feed.module) · Licensed GPL-2.0-or-later (see LICENSE)._
