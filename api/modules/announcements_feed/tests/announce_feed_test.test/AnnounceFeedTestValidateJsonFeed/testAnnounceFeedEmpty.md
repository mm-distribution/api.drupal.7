# AnnounceFeedTestValidateJsonFeed::testAnnounceFeedEmpty()

- **Type:** Method
- **File:** [`modules/announcements_feed/tests/announce_feed_test.test`](../_file.md), lines 103–111 · [local source](../../../../../../source/modules/announcements_feed/tests/announce_feed_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/tests/announce_feed_test.test#L103-L111)
- **Class:** [AnnounceFeedTestValidateJsonFeed](../AnnounceFeedTestValidateJsonFeed.md)
- **Module/theme:** announce_feed_test

## Signature

```php
public function testAnnounceFeedEmpty()
```

## Documentation

```text
Check the status of the feed with an empty JSON feed.
```

## Code

```php
  public function testAnnounceFeedEmpty() {
    // Change the feed URL to empty JSON file.
    variable_set('announcements_feed_json_url', $this->emptyJson);
    cache_clear_all('announcements_feed', 'cache', TRUE);
    $this->drupalLogin($this->user);
    // Only no announcements available message should show.
    $this->clickLink('Announcements');
    $this->assertText('No announcements available');
  }
```

---
_Drupal 7.103 · [modules/announcements_feed/tests/announce_feed_test.test](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/tests/announce_feed_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
