# announcements_feed_filter_announcements()

- **Type:** Function
- **File:** [`modules/announcements_feed/announcements_feed.inc`](_file.md), lines 156–167 · [local source](../../../../source/modules/announcements_feed/announcements_feed.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/announcements_feed.inc#L156-L167)
- **Module/theme:** announcements_feed

## Signature

```php
function announcements_feed_filter_announcements($announcement)
```

## Documentation

```text
Filter the announcements relevant to the Drupal version used with valid URL controlled by drupal.org.

@param array $announcement
  Announcement feed array item to check.

@return bool
  Return TRUE if $announcement is relevant and the URL is valid.
```

## Code

```php
function announcements_feed_filter_announcements($announcement) {
  $announcement_url = '';
  $announcement_version = '';
  if (!empty($announcement['url'])) {
    $announcement_url = $announcement['url'];
  }
  if (!empty($announcement['_drupalorg']['version'])) {
    $announcement_version = $announcement['_drupalorg']['version'];
  }

  return announcements_feed_validate_url($announcement_url) && announcements_feed_is_relevant_item($announcement_version);
}
```

---
_Drupal 7.103 · [modules/announcements_feed/announcements_feed.inc](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/announcements_feed.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
