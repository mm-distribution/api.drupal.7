# AggregatorTestCase::getDefaultFeedItemCount()

- **Type:** Method
- **File:** [`modules/aggregator/aggregator.test`](../_file.md), lines 85–89 · [local source](../../../../../source/modules/aggregator/aggregator.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test#L85-L89)
- **Class:** [AggregatorTestCase](../AggregatorTestCase.md)
- **Module/theme:** aggregator

## Signature

```php
function getDefaultFeedItemCount()
```

## Documentation

```text
Returns the count of the randomly created feed array.

@return
  Number of feed items on default feed created by createFeed().
```

## Code

```php
  function getDefaultFeedItemCount() {
    // Our tests are based off of rss.xml, so let's find out how many elements should be related.
    $feed_count = db_query_range('SELECT COUNT(*) FROM {node} n WHERE n.promote = 1 AND n.status = 1', 0, variable_get('feed_default_items', 10))->fetchField();
    return $feed_count > 10 ? 10 : $feed_count;
  }
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.test](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test) · Licensed GPL-2.0-or-later (see LICENSE)._
