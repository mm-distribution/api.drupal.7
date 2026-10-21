# AnnounceFeedTestSanitizationTestCase

- **Type:** Class
- **File:** [`modules/announcements_feed/tests/announce_feed_test.test`](_file.md), lines 358–412 · [local source](../../../../../source/modules/announcements_feed/tests/announce_feed_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/tests/announce_feed_test.test#L358-L412)
- **Module/theme:** announce_feed_test

## Signature

```php
class AnnounceFeedTestSanitizationTestCase extends DrupalWebTestCase
```

## Documentation

```text
Tests the announcements feed with malicious content.
```

## Properties

### $user

```php
protected $user;
```

```text
A user with permission to access toolbar and access announcements.

@var object
```

### $hackedJson

```php
protected $hackedJson;
```

```text
A test endpoint which contains the malicious content.

@var string
```

## Methods (derived index)

- [getInfo()](AnnounceFeedTestSanitizationTestCase/getInfo.md)
- [setUp()](AnnounceFeedTestSanitizationTestCase/setUp.md) — {@inheritdoc}
- [testSanitizedFeedResponse()](AnnounceFeedTestSanitizationTestCase/testSanitizedFeedResponse.md) — Test the announcements feed with malicious content.

---
_Drupal 7.103 · [modules/announcements_feed/tests/announce_feed_test.test](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/tests/announce_feed_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
