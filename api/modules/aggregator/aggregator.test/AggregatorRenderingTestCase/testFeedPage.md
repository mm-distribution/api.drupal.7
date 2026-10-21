# AggregatorRenderingTestCase::testFeedPage()

- **Type:** Method
- **File:** [`modules/aggregator/aggregator.test`](../_file.md), lines 988–1005 · [local source](../../../../../source/modules/aggregator/aggregator.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test#L988-L1005)
- **Class:** [AggregatorRenderingTestCase](../AggregatorRenderingTestCase.md)
- **Module/theme:** aggregator

## Signature

```php
public function testFeedPage()
```

## Documentation

```text
Creates a feed and checks that feed's page.
```

## Code

```php
  public function testFeedPage() {
    // Increase the number of items published in the rss.xml feed so we have
    // enough articles to test paging.
    variable_set('feed_default_items', 30);

    // Create a feed with 30 items.
    $this->createSampleNodes(30);
    $feed = $this->createFeed();
    $this->updateFeedItems($feed, 30);

    // Check for the presence of a pager.
    $this->drupalGet('aggregator/sources/' . $feed->fid);
    $elements = $this->xpath("//ul[@class=:class]", array(':class' => 'pager'));
    $this->assertTrue(!empty($elements), 'Individual source page contains a pager.');

    // Reset the number of items in rss.xml to the default value.
    variable_set('feed_default_items', 10);
  }
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.test](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test) · Licensed GPL-2.0-or-later (see LICENSE)._
