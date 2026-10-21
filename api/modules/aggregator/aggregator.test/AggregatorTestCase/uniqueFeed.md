# AggregatorTestCase::uniqueFeed()

- **Type:** Method
- **File:** [`modules/aggregator/aggregator.test`](../_file.md), lines 195–198 · [local source](../../../../../source/modules/aggregator/aggregator.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test#L195-L198)
- **Class:** [AggregatorTestCase](../AggregatorTestCase.md)
- **Module/theme:** aggregator

## Signature

```php
function uniqueFeed($feed_name, $feed_url)
```

## Documentation

```text
Checks whether the feed name and URL are unique.

@param $feed_name
  String containing the feed name to check.
@param $feed_url
  String containing the feed URL to check.

@return
  TRUE if feed is unique.
```

## Code

```php
  function uniqueFeed($feed_name, $feed_url) {
    $result = db_query("SELECT COUNT(*) FROM {aggregator_feed} WHERE title = :title AND url = :url", array(':title' => $feed_name, ':url' => $feed_url))->fetchField();
    return (1 == $result);
  }
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.test](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test) · Licensed GPL-2.0-or-later (see LICENSE)._
