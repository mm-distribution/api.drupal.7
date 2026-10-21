# AnnounceFeedTestSanitizationTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/announcements_feed/tests/announce_feed_test.test`](../_file.md), lines 374–380 · [local source](../../../../../../source/modules/announcements_feed/tests/announce_feed_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/tests/announce_feed_test.test#L374-L380)
- **Class:** [AnnounceFeedTestSanitizationTestCase](../AnnounceFeedTestSanitizationTestCase.md)
- **Module/theme:** announce_feed_test

## Signature

```php
public static function getInfo()
```

## Documentation

_No docblock in source._

## Code

```php
  public static function getInfo() {
    return array(
      'name' => 'Hacked JSON feed URL',
      'description' => 'Testing announcements feed that contains malicious content.',
      'group' => 'Announcements',
    );
  }
```

---
_Drupal 7.103 · [modules/announcements_feed/tests/announce_feed_test.test](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/tests/announce_feed_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
