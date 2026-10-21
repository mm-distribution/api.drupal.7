# announcements_feed_get_all_announcements()

- **Type:** Function
- **File:** [`modules/announcements_feed/announcements_feed.inc`](_file.md), lines 47–64 · [local source](../../../../source/modules/announcements_feed/announcements_feed.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/announcements_feed.inc#L47-L64)
- **Module/theme:** announcements_feed

## Signature

```php
function announcements_feed_get_all_announcements()
```

## Documentation

```text
Generate an array of announcements with keys.

@return array
  An array of announcements.
```

## Code

```php
function announcements_feed_get_all_announcements() {
  $announcements = announcements_feed_fetch();
  $announcements_feed = array();
  foreach ($announcements as $announcement) {
    $announcements_feed[] = array(
      'id' => $announcement['id'],
      'title' => $announcement['title'],
      'link' => $announcement['url'],
      'date_modified' => $announcement['date_modified'],
      'date_published' => $announcement['date_published'],
      'teaser' => $announcement['content_html'],
      'version' => $announcement['_drupalorg']['version'],
      'featured' => (bool) $announcement['_drupalorg']['featured'],
    );
  }

  return $announcements_feed;
}
```

---
_Drupal 7.103 · [modules/announcements_feed/announcements_feed.inc](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/announcements_feed.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
