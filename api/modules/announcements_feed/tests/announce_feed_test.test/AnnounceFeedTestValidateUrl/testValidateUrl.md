# AnnounceFeedTestValidateUrl::testValidateUrl()

- **Type:** Method
- **File:** [`modules/announcements_feed/tests/announce_feed_test.test`](../_file.md), lines 138–161 · [local source](../../../../../../source/modules/announcements_feed/tests/announce_feed_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/tests/announce_feed_test.test#L138-L161)
- **Class:** [AnnounceFeedTestValidateUrl](../AnnounceFeedTestValidateUrl.md)
- **Module/theme:** announce_feed_test

## Signature

```php
public function testValidateUrl()
```

## Documentation

```text
Test for validating the announcements_feed_validate_url function.
```

## Code

```php
  public function testValidateUrl() {
    $urls = array(
      array('https://www.drupal.org', TRUE),
      array('https://drupal.org', TRUE),
      array('https://api.drupal.org', TRUE),
      array('https://a.drupal.org', TRUE),
      array('https://123.drupal.org', TRUE),
      array('https://api-new.drupal.org', TRUE),
      array('https://api_new.drupal.org', TRUE),
      array('https://api-.drupal.org', TRUE),
      array('https://www.example.org', FALSE),
      array('https://example.org', FALSE),
      array('https://api.example.org/project/announce', FALSE),
      array('https://-api.drupal.org', FALSE),
      array('https://a.example.org/project/announce', FALSE),
      array('https://test.drupaal.com', FALSE),
      array('https://api.drupal.org.example.com', FALSE),
      array('https://example.org/drupal.org', FALSE),
    );
    foreach ($urls as $url) {
      $result = announcements_feed_validate_url($url[0]);
      $this->assertEqual($url[1], $result, 'Returned ' . ($url[1] ? 'TRUE' : 'FALSE'));
    }
  }
```

---
_Drupal 7.103 · [modules/announcements_feed/tests/announce_feed_test.test](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/tests/announce_feed_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
