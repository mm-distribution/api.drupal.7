# AnnounceFeedTestRelevantVersion::testIsRelevantItem()

- **Type:** Method
- **File:** [`modules/announcements_feed/tests/announce_feed_test.test`](../_file.md), lines 188–208 · [local source](../../../../../../source/modules/announcements_feed/tests/announce_feed_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/tests/announce_feed_test.test#L188-L208)
- **Class:** [AnnounceFeedTestRelevantVersion](../AnnounceFeedTestRelevantVersion.md)
- **Module/theme:** announce_feed_test

## Signature

```php
public function testIsRelevantItem()
```

## Documentation

```text
Test for validating the announcements_feed_is_relevant_item function.
```

## Code

```php
  public function testIsRelevantItem() {
    $version_strings = array(
      array('^7', TRUE),
      // TRUE only if Drupal version is exactly 7.0.
      array('=7.0', FALSE),
      array('>=7', TRUE),
      array('^7 || ^8 || ^9', TRUE),
      array('>=7.52', TRUE),
      array('^7.1 || ^8 || ^9', TRUE),
      // TRUE only if Drupal version is exactly 7.9999.
      array('=7.9999', FALSE),
      array('^8 || ^9', FALSE),
      array('>8', FALSE),
      array('>=8.1', FALSE),
      array('^8 || ^9 || ^10', FALSE),
    );
    foreach ($version_strings as $strings) {
      $result = announcements_feed_is_relevant_item($strings[0]);
      $this->assertEqual($strings[1], $result, 'Returned ' . ($strings[1] ? 'TRUE' : 'FALSE'));
    }
  }
```

---
_Drupal 7.103 · [modules/announcements_feed/tests/announce_feed_test.test](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/tests/announce_feed_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
