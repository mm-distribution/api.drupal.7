# template_preprocess_announcements_feed()

- **Type:** Function
- **File:** [`modules/announcements_feed/announcements_feed.module`](_file.md), lines 107–121 · [local source](../../../../source/modules/announcements_feed/announcements_feed.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/announcements_feed.module#L107-L121)
- **Module/theme:** announcements_feed

## Signature

```php
function template_preprocess_announcements_feed(&$variables)
```

## Documentation

```text
Processes variables for announcements-feed.tpl.php.

@see announcements-feed.tpl.php
```

## Code

```php
function template_preprocess_announcements_feed(&$variables) {
  if (!empty($variables['featured'])) {
    foreach($variables['featured'] as &$announcement) {
      _announcements_feed_preprocess_item($announcement);
    }
  }
  if (!empty($variables['standard'])) {
    foreach($variables['standard'] as &$announcement) {
      _announcements_feed_preprocess_item($announcement);
    }
  }
  if (isset($variables['feed_link'])) {
    $variables['feed_link'] = check_url($variables['feed_link']);
  }
}
```

---
_Drupal 7.103 · [modules/announcements_feed/announcements_feed.module](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/announcements_feed.module) · Licensed GPL-2.0-or-later (see LICENSE)._
