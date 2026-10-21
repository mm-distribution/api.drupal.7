# _announcements_feed_preprocess_item()

- **Type:** Function
- **File:** [`modules/announcements_feed/announcements_feed.module`](_file.md), lines 126–133 · [local source](../../../../source/modules/announcements_feed/announcements_feed.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/announcements_feed.module#L126-L133)
- **Module/theme:** announcements_feed

## Signature

```php
function _announcements_feed_preprocess_item(&$item)
```

## Documentation

```text
Helper to preprocess individual announcement items.
```

## Code

```php
function _announcements_feed_preprocess_item(&$item) {
  $item['title'] = filter_xss($item['title']);
  $item['teaser'] = filter_xss($item['teaser']);
  $item['link'] = check_url($item['link']);
  $item['date_modified'] = check_plain($item['date_modified']);
  $item['date_published'] = check_plain($item['date_published']);
  $item['version'] = check_plain($item['version']);
}
```

---
_Drupal 7.103 · [modules/announcements_feed/announcements_feed.module](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/announcements_feed.module) · Licensed GPL-2.0-or-later (see LICENSE)._
