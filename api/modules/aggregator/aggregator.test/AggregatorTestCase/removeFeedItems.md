# AggregatorTestCase::removeFeedItems()

- **Type:** Method
- **File:** [`modules/aggregator/aggregator.test`](../_file.md), lines 132–135 · [local source](../../../../../source/modules/aggregator/aggregator.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test#L132-L135)
- **Class:** [AggregatorTestCase](../AggregatorTestCase.md)
- **Module/theme:** aggregator

## Signature

```php
function removeFeedItems($feed)
```

## Documentation

```text
Confirms an item removal from a feed.

@param $feed
  Feed object representing the feed.
```

## Code

```php
  function removeFeedItems($feed) {
    $this->drupalPost('admin/config/services/aggregator/remove/' . $feed->fid, array(), t('Remove items'));
    $this->assertRaw(t('The news items from %title have been removed.', array('%title' => $feed->title)), 'Feed items removed.');
  }
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.test](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test) · Licensed GPL-2.0-or-later (see LICENSE)._
