# AnnounceFeedTestValidatePermissions::testAnnounceWithoutPermission()

- **Type:** Method
- **File:** [`modules/announcements_feed/tests/announce_feed_test.test`](../_file.md), lines 254–259 · [local source](../../../../../../source/modules/announcements_feed/tests/announce_feed_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/tests/announce_feed_test.test#L254-L259)
- **Class:** [AnnounceFeedTestValidatePermissions](../AnnounceFeedTestValidatePermissions.md)
- **Module/theme:** announce_feed_test

## Signature

```php
public function testAnnounceWithoutPermission()
```

## Documentation

```text
Testing the announcements page without access announcements permission.
```

## Code

```php
  public function testAnnounceWithoutPermission() {
    $account = $this->drupalCreateUser(array('access toolbar'));
    $this->drupalLogin($account);
    $this->drupalGet('admin/announcements_feed');
    $this->assertResponse(403);
  }
```

---
_Drupal 7.103 · [modules/announcements_feed/tests/announce_feed_test.test](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/tests/announce_feed_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
