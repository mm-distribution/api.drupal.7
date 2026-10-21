# AggregatorTestCase::getFeedCategories()

- **Type:** Method
- **File:** [`modules/aggregator/aggregator.test`](../_file.md), lines 160–166 · [local source](../../../../../source/modules/aggregator/aggregator.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test#L160-L166)
- **Class:** [AggregatorTestCase](../AggregatorTestCase.md)
- **Module/theme:** aggregator

## Signature

```php
function getFeedCategories($feed)
```

## Documentation

```text
Pulls feed categories from {aggregator_category_feed} table.

@param $feed
  Feed object representing the feed.
```

## Code

```php
  function getFeedCategories($feed) {
    // add the categories to the feed so we can use them
    $result = db_query('SELECT cid FROM {aggregator_category_feed} WHERE fid = :fid', array(':fid' => $feed->fid));
    foreach ($result as $category) {
      $feed->categories[] = $category->cid;
    }
  }
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.test](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test) · Licensed GPL-2.0-or-later (see LICENSE)._
