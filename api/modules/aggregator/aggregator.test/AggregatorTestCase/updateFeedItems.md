# AggregatorTestCase::updateFeedItems()

- **Type:** Method
- **File:** [`modules/aggregator/aggregator.test`](../_file.md), lines 102–124 · [local source](../../../../../source/modules/aggregator/aggregator.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test#L102-L124)
- **Class:** [AggregatorTestCase](../AggregatorTestCase.md)
- **Module/theme:** aggregator

## Signature

```php
function updateFeedItems(&$feed, $expected_count)
```

## Documentation

```text
Updates the feed items.

This method simulates a click to
admin/config/services/aggregator/update/$fid.

@param $feed
  Feed object representing the feed, passed by reference.
@param $expected_count
  Expected number of feed items.
```

## Code

```php
  function updateFeedItems(&$feed, $expected_count) {
    // First, let's ensure we can get to the rss xml.
    $this->drupalGet($feed->url);
    $this->assertResponse(200, format_string('!url is reachable.', array('!url' => $feed->url)));

    // Attempt to access the update link directly without an access token.
    $this->drupalGet('admin/config/services/aggregator/update/' . $feed->fid);
    $this->assertResponse(403);

    // Refresh the feed (simulated link click).
    $this->drupalGet('admin/config/services/aggregator');
    $this->clickLink('update items');

    // Ensure we have the right number of items.
    $result = db_query('SELECT iid FROM {aggregator_item} WHERE fid = :fid', array(':fid' => $feed->fid));
    $items = array();
    $feed->items = array();
    foreach ($result as $item) {
      $feed->items[] = $item->iid;
    }
    $feed->item_count = count($feed->items);
    $this->assertEqual($expected_count, $feed->item_count, format_string('Total items in feed equal to the total items in database (!val1 != !val2)', array('!val1' => $expected_count, '!val2' => $feed->item_count)));
  }
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.test](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test) · Licensed GPL-2.0-or-later (see LICENSE)._
