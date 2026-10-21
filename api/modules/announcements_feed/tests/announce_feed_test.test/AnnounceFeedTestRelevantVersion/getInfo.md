# AnnounceFeedTestRelevantVersion::getInfo()

- **Type:** Method
- **File:** [`modules/announcements_feed/tests/announce_feed_test.test`](../_file.md), lines 169–175 · [local source](../../../../../../source/modules/announcements_feed/tests/announce_feed_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/tests/announce_feed_test.test#L169-L175)
- **Class:** [AnnounceFeedTestRelevantVersion](../AnnounceFeedTestRelevantVersion.md)
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
      'name' => 'Version-specific logic validation',
      'description' => 'Unit test to check the version-specific logic.',
      'group' => 'Announcements',
    );
  }
```

---
_Drupal 7.103 · [modules/announcements_feed/tests/announce_feed_test.test](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/tests/announce_feed_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
