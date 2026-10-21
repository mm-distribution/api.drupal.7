# AnnounceFeedTestValidateJsonFeed

- **Type:** Class
- **File:** [`modules/announcements_feed/tests/announce_feed_test.test`](_file.md), lines 11–113 · [local source](../../../../../source/modules/announcements_feed/tests/announce_feed_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/tests/announce_feed_test.test#L11-L113)
- **Module/theme:** announce_feed_test

## Signature

```php
class AnnounceFeedTestValidateJsonFeed extends DrupalWebTestCase
```

## Documentation

```text
Tests for validating JSON feed with different JSON URLs.
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

### $updatedJson

```php
protected $updatedJson;
```

```text
A test endpoint which include the new/updated feeds.

@var string
```

### $emptyJson

```php
protected $emptyJson;
```

```text
A test endpoint which displays an empty JSON.

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

- [getInfo()](AnnounceFeedTestValidateJsonFeed/getInfo.md)
- [setUp()](AnnounceFeedTestValidateJsonFeed/setUp.md) — {@inheritdoc}
- [testAnnounceFeedUpdatedAndRemoved()](AnnounceFeedTestValidateJsonFeed/testAnnounceFeedUpdatedAndRemoved.md) — Testing the feed with Updated and Removed JSON feeds.
- [testAnnounceFeedEmpty()](AnnounceFeedTestValidateJsonFeed/testAnnounceFeedEmpty.md) — Check the status of the feed with an empty JSON feed.

---
_Drupal 7.103 · [modules/announcements_feed/tests/announce_feed_test.test](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/tests/announce_feed_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
