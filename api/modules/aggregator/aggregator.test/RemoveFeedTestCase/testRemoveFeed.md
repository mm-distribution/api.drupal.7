# RemoveFeedTestCase::testRemoveFeed()

- **Type:** Method
- **File:** [`modules/aggregator/aggregator.test`](../_file.md), lines 542–555 · [local source](../../../../../source/modules/aggregator/aggregator.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test#L542-L555)
- **Class:** [RemoveFeedTestCase](../RemoveFeedTestCase.md)
- **Module/theme:** aggregator

## Signature

```php
function testRemoveFeed()
```

## Documentation

```text
Removes a feed and ensures that all of its services are removed.
```

## Code

```php
  function testRemoveFeed() {
    $feed = $this->createFeed();

    // Delete feed.
    $this->deleteFeed($feed);

    // Check feed source.
    $this->drupalGet('aggregator/sources/' . $feed->fid);
    $this->assertResponse(404, 'Deleted feed source does not exists.');

    // Check database for feed.
    $result = db_query("SELECT COUNT(*) FROM {aggregator_feed} WHERE title = :title AND url = :url", array(':title' => $feed->title, ':url' => $feed->url))->fetchField();
    $this->assertFalse($result, 'Feed not found in database');
  }
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.test](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test) · Licensed GPL-2.0-or-later (see LICENSE)._
