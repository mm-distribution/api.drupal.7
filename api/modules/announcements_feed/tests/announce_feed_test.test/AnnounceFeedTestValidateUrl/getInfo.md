# AnnounceFeedTestValidateUrl::getInfo()

- **Type:** Method
- **File:** [`modules/announcements_feed/tests/announce_feed_test.test`](../_file.md), lines 119–125 · [local source](../../../../../../source/modules/announcements_feed/tests/announce_feed_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/tests/announce_feed_test.test#L119-L125)
- **Class:** [AnnounceFeedTestValidateUrl](../AnnounceFeedTestValidateUrl.md)
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
      'name' => 'JSON feed URLs validation',
      'description' => 'Unit test to check the validate URL functions.',
      'group' => 'Announcements',
    );
  }
```

---
_Drupal 7.103 · [modules/announcements_feed/tests/announce_feed_test.test](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/tests/announce_feed_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
