# AnnounceFeedTestValidatePermissions::setUp()

- **Type:** Method
- **File:** [`modules/announcements_feed/tests/announce_feed_test.test`](../_file.md), lines 227–233 · [local source](../../../../../../source/modules/announcements_feed/tests/announce_feed_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/tests/announce_feed_test.test#L227-L233)
- **Class:** [AnnounceFeedTestValidatePermissions](../AnnounceFeedTestValidatePermissions.md)
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
    $response_json = $base_url . '/announcements-feed-json/community-feeds';
    variable_set('announcements_feed_json_url', $response_json);
  }
```

---
_Drupal 7.103 · [modules/announcements_feed/tests/announce_feed_test.test](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/tests/announce_feed_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
