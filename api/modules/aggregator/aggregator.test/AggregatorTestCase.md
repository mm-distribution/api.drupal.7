# AggregatorTestCase

- **Type:** Class
- **File:** [`modules/aggregator/aggregator.test`](_file.md), lines 11–315 · [local source](../../../../source/modules/aggregator/aggregator.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test#L11-L315)
- **Module/theme:** aggregator

## Signature

```php
class AggregatorTestCase extends DrupalWebTestCase
```

## Documentation

```text
Defines a base class for testing the Aggregator module.
```

## Methods (derived index)

- [setUp()](AggregatorTestCase/setUp.md)
- [createFeed()](AggregatorTestCase/createFeed.md) — Creates an aggregator feed.
- [deleteFeed()](AggregatorTestCase/deleteFeed.md) — Deletes an aggregator feed.
- [getFeedEditArray()](AggregatorTestCase/getFeedEditArray.md) — Returns a randomly generated feed edit array.
- [getDefaultFeedItemCount()](AggregatorTestCase/getDefaultFeedItemCount.md) — Returns the count of the randomly created feed array.
- [updateFeedItems()](AggregatorTestCase/updateFeedItems.md) — Updates the feed items.
- [removeFeedItems()](AggregatorTestCase/removeFeedItems.md) — Confirms an item removal from a feed.
- [updateAndRemove()](AggregatorTestCase/updateAndRemove.md) — Adds and removes feed items and ensure that the count is zero.
- [getFeedCategories()](AggregatorTestCase/getFeedCategories.md) — Pulls feed categories from {aggregator_category_feed} table.
- [getCategories()](AggregatorTestCase/getCategories.md) — Pulls categories from {aggregator_category} table.
- [uniqueFeed()](AggregatorTestCase/uniqueFeed.md) — Checks whether the feed name and URL are unique.
- [getValidOpml()](AggregatorTestCase/getValidOpml.md) — Creates a valid OPML file from an array of feeds.
- [getInvalidOpml()](AggregatorTestCase/getInvalidOpml.md) — Creates an invalid OPML file.
- [getEmptyOpml()](AggregatorTestCase/getEmptyOpml.md) — Creates a valid but empty OPML file.
- [getRSS091Sample()](AggregatorTestCase/getRSS091Sample.md)
- [getAtomSample()](AggregatorTestCase/getAtomSample.md)
- [getHtmlEntitiesSample()](AggregatorTestCase/getHtmlEntitiesSample.md)
- [getNoTitleSample()](AggregatorTestCase/getNoTitleSample.md)
- [createSampleNodes()](AggregatorTestCase/createSampleNodes.md) — Creates sample article nodes.

---
_Drupal 7.103 · [modules/aggregator/aggregator.test](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test) · Licensed GPL-2.0-or-later (see LICENSE)._
