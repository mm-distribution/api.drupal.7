# AggregatorTestCase::updateAndRemove()

- **Type:** Method
- **File:** [`modules/aggregator/aggregator.test`](../_file.md), lines 145–152 · [local source](../../../../../source/modules/aggregator/aggregator.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test#L145-L152)
- **Class:** [AggregatorTestCase](../AggregatorTestCase.md)
- **Module/theme:** aggregator

## Signature

```php
function updateAndRemove($feed, $expected_count)
```

## Documentation

```text
Adds and removes feed items and ensure that the count is zero.

@param $feed
  Feed object representing the feed.
@param $expected_count
  Expected number of feed items.
```

## Code

```php
  function updateAndRemove($feed, $expected_count) {
    $this->updateFeedItems($feed, $expected_count);
    $count = db_query('SELECT COUNT(*) FROM {aggregator_item} WHERE fid = :fid', array(':fid' => $feed->fid))->fetchField();
    $this->assertTrue($count);
    $this->removeFeedItems($feed);
    $count = db_query('SELECT COUNT(*) FROM {aggregator_item} WHERE fid = :fid', array(':fid' => $feed->fid))->fetchField();
    $this->assertTrue($count == 0);
  }
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.test](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test) · Licensed GPL-2.0-or-later (see LICENSE)._
