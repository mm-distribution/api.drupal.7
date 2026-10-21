# announcements_feed_theme()

- **Type:** Function
- **File:** [`modules/announcements_feed/announcements_feed.module`](_file.md), lines 87–100 · [local source](../../../../source/modules/announcements_feed/announcements_feed.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/announcements_feed.module#L87-L100)
- **Module/theme:** announcements_feed
- **Implements:** [hook_theme()](../../system/system.api.php/hook_theme.md)

## Signature

```php
function announcements_feed_theme()
```

## Documentation

```text
Implements hook_theme().
```

## Code

```php
function announcements_feed_theme() {
  return array(
    'announcements_feed' => array(
      'variables' => array(
        'featured' => NULL,
        'standard' => NULL,
        'feed_link' => NULL,
        'count' => 0,
      ),
      'template' => 'announcements-feed',
      'path' => drupal_get_path('module', 'announcements_feed'),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/announcements_feed/announcements_feed.module](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/announcements_feed.module) · Licensed GPL-2.0-or-later (see LICENSE)._
