# AnnounceFeedTestInvalidJsonTestCase::testInvalidFeedResponse()

- **Type:** Method
- **File:** [`modules/announcements_feed/tests/announce_feed_test.test`](../_file.md), lines 331–352 · [local source](../../../../../../source/modules/announcements_feed/tests/announce_feed_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/tests/announce_feed_test.test#L331-L352)
- **Class:** [AnnounceFeedTestInvalidJsonTestCase](../AnnounceFeedTestInvalidJsonTestCase.md)
- **Module/theme:** announce_feed_test

## Signature

```php
public function testInvalidFeedResponse()
```

## Documentation

```text
Test the announcements feed with invalid JSON or non-existing JSON URL.
```

## Code

```php
  public function testInvalidFeedResponse() {
    // Test when the JSON URL is not found.
    $this->drupalLogin($this->user);
    $this->drupalGet('');
    $this->clickLink('Announcements');
    variable_set('announcements_feed_json_url', $this->unknownJson);
    cache_clear_all('announcements_feed', 'cache', TRUE);
    $this->drupalGet('admin/announcements_feed');
    $this->assertText('An error occurred while parsing the announcements feed, check the logs for more information.');

    // Test when the JSON feed is invalid.
    $this->drupalLogout();
    $this->drupalLogin($this->user);
    $this->drupalGet('');
    $this->clickLink('Announcements');
    variable_set('announcements_feed_json_url', $this->invalidJson);
    cache_clear_all('announcements_feed', 'cache', TRUE);
    $this->drupalGet('admin/announcements_feed');
    $this->assertText('An error occurred while parsing the announcements feed, check the logs for more information.');

    $this->drupalLogout();
  }
```

---
_Drupal 7.103 · [modules/announcements_feed/tests/announce_feed_test.test](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/tests/announce_feed_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
