# AddFeedTestCase::testAddFeed()

- **Type:** Method
- **File:** [`modules/aggregator/aggregator.test`](../_file.md), lines 364–380 · [local source](../../../../../source/modules/aggregator/aggregator.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test#L364-L380)
- **Class:** [AddFeedTestCase](../AddFeedTestCase.md)
- **Module/theme:** aggregator

## Signature

```php
function testAddFeed()
```

## Documentation

```text
Creates and ensures that a feed is unique, checks source, and deletes feed.
```

## Code

```php
  function testAddFeed() {
    $feed = $this->createFeed();

    // Check feed data.
    $this->assertEqual($this->getUrl(), url('admin/config/services/aggregator/add/feed', array('absolute' => TRUE)), 'Directed to correct url.');
    $this->assertTrue($this->uniqueFeed($feed->title, $feed->url), 'The feed is unique.');

    // Check feed source.
    $this->drupalGet('aggregator/sources/' . $feed->fid);
    $this->assertResponse(200, 'Feed source exists.');
    $this->assertText($feed->title, 'Page title');
    $this->drupalGet('aggregator/sources/' . $feed->fid . '/categorize');
    $this->assertResponse(200, 'Feed categorization page exists.');

    // Delete feed.
    $this->deleteFeed($feed);
  }
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.test](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test) · Licensed GPL-2.0-or-later (see LICENSE)._
