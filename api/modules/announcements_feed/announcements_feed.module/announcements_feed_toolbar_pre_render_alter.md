# announcements_feed_toolbar_pre_render_alter()

- **Type:** Function
- **File:** [`modules/announcements_feed/announcements_feed.module`](_file.md), lines 148–159 · [local source](../../../../source/modules/announcements_feed/announcements_feed.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/announcements_feed.module#L148-L159)
- **Module/theme:** announcements_feed

## Signature

```php
function announcements_feed_toolbar_pre_render_alter($toolbar)
```

## Documentation

```text
Pre-render function for adding default class to announcement link.
```

## Code

```php
function announcements_feed_toolbar_pre_render_alter($toolbar) {
  $path = drupal_get_path('module', 'announcements_feed');
  $toolbar['#attached']['css'][] = $path . '/announcements_feed-toolbar.css';
  module_load_include('inc', 'announcements_feed');
  foreach ($toolbar['toolbar_menu']['#links'] as &$link) {
    if ($link['href'] === 'admin/announcements_feed') {
      $link['attributes']['class'][] = 'announcement-default';
    }
  }

  return $toolbar;
}
```

---
_Drupal 7.103 · [modules/announcements_feed/announcements_feed.module](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/announcements_feed.module) · Licensed GPL-2.0-or-later (see LICENSE)._
