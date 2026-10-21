# announcements_feed_permission()

- **Type:** Function
- **File:** [`modules/announcements_feed/announcements_feed.module`](_file.md), lines 76–82 · [local source](../../../../source/modules/announcements_feed/announcements_feed.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/announcements_feed.module#L76-L82)
- **Module/theme:** announcements_feed
- **Implements:** [hook_permission()](../../system/system.api.php/hook_permission.md)

## Signature

```php
function announcements_feed_permission()
```

## Documentation

```text
Implements hook_permission().
```

## Code

```php
function announcements_feed_permission() {
  return array(
    'access announcements' => array(
      'title' => t('View official announcements related to Drupal'),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/announcements_feed/announcements_feed.module](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/announcements_feed.module) · Licensed GPL-2.0-or-later (see LICENSE)._
