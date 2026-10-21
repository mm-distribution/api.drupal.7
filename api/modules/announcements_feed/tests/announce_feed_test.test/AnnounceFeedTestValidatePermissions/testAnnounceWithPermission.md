# AnnounceFeedTestValidatePermissions::testAnnounceWithPermission()

- **Type:** Method
- **File:** [`modules/announcements_feed/tests/announce_feed_test.test`](../_file.md), lines 238–249 · [local source](../../../../../../source/modules/announcements_feed/tests/announce_feed_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/tests/announce_feed_test.test#L238-L249)
- **Class:** [AnnounceFeedTestValidatePermissions](../AnnounceFeedTestValidatePermissions.md)
- **Module/theme:** announce_feed_test

## Signature

```php
public function testAnnounceWithPermission()
```

## Documentation

```text
Testing the announcements page with access announcements permission.
```

## Code

```php
  public function testAnnounceWithPermission() {
    // Create a user with proper permission.
    $account = $this->drupalCreateUser(array(
      'access toolbar',
      'access announcements',
    ));
    $this->drupalLogin($account);
    $this->drupalGet('');
    $this->drupalGet('admin/announcements_feed');
    $this->assertText('Announcements');
    $this->drupalLogout();
  }
```

---
_Drupal 7.103 · [modules/announcements_feed/tests/announce_feed_test.test](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/tests/announce_feed_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
