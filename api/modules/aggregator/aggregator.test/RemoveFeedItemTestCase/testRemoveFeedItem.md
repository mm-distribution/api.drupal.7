# RemoveFeedItemTestCase::testRemoveFeedItem()

- **Type:** Method
- **File:** [`modules/aggregator/aggregator.test`](../_file.md), lines 633–656 · [local source](../../../../../source/modules/aggregator/aggregator.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test#L633-L656)
- **Class:** [RemoveFeedItemTestCase](../RemoveFeedItemTestCase.md)
- **Module/theme:** aggregator

## Signature

```php
function testRemoveFeedItem()
```

## Documentation

```text
Tests running "remove items" from 'admin/config/services/aggregator' page.
```

## Code

```php
  function testRemoveFeedItem() {
    // Create a bunch of test feeds.
    $feed_urls = array();
    // No last-modified, no etag.
    $feed_urls[] = url('aggregator/test-feed', array('absolute' => TRUE));
    // Last-modified, but no etag.
    $feed_urls[] = url('aggregator/test-feed/1', array('absolute' => TRUE));
    // No Last-modified, but etag.
    $feed_urls[] = url('aggregator/test-feed/0/1', array('absolute' => TRUE));
    // Last-modified and etag.
    $feed_urls[] = url('aggregator/test-feed/1/1', array('absolute' => TRUE));

    foreach ($feed_urls as $feed_url) {
      $feed = $this->createFeed($feed_url);
      // Update and remove items two times in a row to make sure that removal
      // resets all 'modified' information (modified, etag, hash) and allows for
      // immediate update.
      $this->updateAndRemove($feed, 4);
      $this->updateAndRemove($feed, 4);
      $this->updateAndRemove($feed, 4);
      // Delete feed.
      $this->deleteFeed($feed);
    }
  }
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.test](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test) · Licensed GPL-2.0-or-later (see LICENSE)._
