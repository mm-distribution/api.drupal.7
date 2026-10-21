# AnnounceFeedTestInvalidJsonTestCase::setUp()

- **Type:** Method
- **File:** [`modules/announcements_feed/tests/announce_feed_test.test`](../_file.md), lines 313–326 · [local source](../../../../../../source/modules/announcements_feed/tests/announce_feed_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/tests/announce_feed_test.test#L313-L326)
- **Class:** [AnnounceFeedTestInvalidJsonTestCase](../AnnounceFeedTestInvalidJsonTestCase.md)
- **Module/theme:** announce_feed_test

## Signature

```php
public function setUp()
```

## Documentation

```text
{@inheritdoc}
```

## Code

```php
  public function setUp() {
    global $base_url;
    module_load_include('inc', 'announce_feed_test', 'announce_feed_test');
    parent::setUp('user', 'toolbar', 'announcements_feed', 'announce_feed_test');
    $this->user = $this->drupalCreateUser(array(
      'access toolbar',
      'access announcements',
    ));
    $this->drupalLogin($this->user);
    $this->responseJson = $base_url . '/announcements-feed-json/community-feeds';
    $this->unknownJson = $base_url . '/announcements-feed-json/unknown';
    $this->invalidJson = $base_url . '/announcements-feed-json/invalid-feeds';
    variable_set('announcements_feed_json_url', $this->responseJson);
  }
```

---
_Drupal 7.103 · [modules/announcements_feed/tests/announce_feed_test.test](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/tests/announce_feed_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
