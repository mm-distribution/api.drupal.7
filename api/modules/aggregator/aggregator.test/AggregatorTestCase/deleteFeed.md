# AggregatorTestCase::deleteFeed()

- **Type:** Method
- **File:** [`modules/aggregator/aggregator.test`](../_file.md), lines 49–52 · [local source](../../../../../source/modules/aggregator/aggregator.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test#L49-L52)
- **Class:** [AggregatorTestCase](../AggregatorTestCase.md)
- **Module/theme:** aggregator

## Signature

```php
function deleteFeed($feed)
```

## Documentation

```text
Deletes an aggregator feed.

@param $feed
  Feed object representing the feed.
```

## Code

```php
  function deleteFeed($feed) {
    $this->drupalPost('admin/config/services/aggregator/edit/feed/' . $feed->fid, array(), t('Delete'));
    $this->assertRaw(t('The feed %title has been deleted.', array('%title' => $feed->title)), 'Feed deleted successfully.');
  }
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.test](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test) · Licensed GPL-2.0-or-later (see LICENSE)._
