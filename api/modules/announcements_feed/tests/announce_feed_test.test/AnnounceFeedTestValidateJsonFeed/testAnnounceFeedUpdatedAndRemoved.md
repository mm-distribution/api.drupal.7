# AnnounceFeedTestValidateJsonFeed::testAnnounceFeedUpdatedAndRemoved()

- **Type:** Method
- **File:** [`modules/announcements_feed/tests/announce_feed_test.test`](../_file.md), lines 78–98 · [local source](../../../../../../source/modules/announcements_feed/tests/announce_feed_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/tests/announce_feed_test.test#L78-L98)
- **Class:** [AnnounceFeedTestValidateJsonFeed](../AnnounceFeedTestValidateJsonFeed.md)
- **Module/theme:** announce_feed_test

## Signature

```php
public function testAnnounceFeedUpdatedAndRemoved()
```

## Documentation

```text
Testing the feed with Updated and Removed JSON feeds.
```

## Code

```php
  public function testAnnounceFeedUpdatedAndRemoved() {
    $this->drupalLogin($this->user);
    $this->drupalGet('');
    $this->clickLink('Announcements');
    variable_set('announcements_feed_json_url', $this->updatedJson);
    cache_clear_all('announcements_feed', 'cache', TRUE);
    $this->drupalGet('admin/announcements_feed');
    $this->assertText('Only 9 - Drupal 106 is available and this feed is Updated');
    $this->drupalLogout();

    // Testing the removed JSON feed.
    $this->drupalLogin($this->user);
    $this->drupalGet('');
    $this->clickLink('Announcements');
    variable_set('announcements_feed_json_url', $this->removed);
    cache_clear_all('announcements_feed', 'cache', TRUE);
    $this->drupalGet('admin/announcements_feed');
    $this->assertNoText('Only 9 - Drupal 106 is available and this feed is Updated');

    $this->drupalLogout();
  }
```

---
_Drupal 7.103 · [modules/announcements_feed/tests/announce_feed_test.test](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/tests/announce_feed_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
