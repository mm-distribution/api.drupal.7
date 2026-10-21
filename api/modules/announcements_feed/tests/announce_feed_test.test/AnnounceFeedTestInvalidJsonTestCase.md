# AnnounceFeedTestInvalidJsonTestCase

- **Type:** Class
- **File:** [`modules/announcements_feed/tests/announce_feed_test.test`](_file.md), lines 265–353 · [local source](../../../../../source/modules/announcements_feed/tests/announce_feed_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/tests/announce_feed_test.test#L265-L353)
- **Module/theme:** announce_feed_test

## Signature

```php
class AnnounceFeedTestInvalidJsonTestCase extends DrupalWebTestCase
```

## Documentation

```text
Tests the announcements feed with invalid JSON URLs.
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

### $responseJson

```php
protected $responseJson;
```

```text
A test endpoint which contains the community feeds.

@var string
```

### $unknownJson

```php
protected $unknownJson;
```

```text
A test endpoint which does not exist.

@var string
```

### $invalidJson

```php
protected $invalidJson;
```

```text
A test endpoint which returns invalid JSON.

@var string
```

### $removed

```php
protected $removed;
```

```text
A test endpoint that will have some feeds removed.

@var string
```

## Methods (derived index)

- [getInfo()](AnnounceFeedTestInvalidJsonTestCase/getInfo.md)
- [setUp()](AnnounceFeedTestInvalidJsonTestCase/setUp.md) — {@inheritdoc}
- [testInvalidFeedResponse()](AnnounceFeedTestInvalidJsonTestCase/testInvalidFeedResponse.md) — Test the announcements feed with invalid JSON or non-existing JSON URL.

---
_Drupal 7.103 · [modules/announcements_feed/tests/announce_feed_test.test](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/tests/announce_feed_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
