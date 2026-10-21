# AggregatorRenderingTestCase::testBlockLinks()

- **Type:** Method
- **File:** [`modules/aggregator/aggregator.test`](../_file.md), lines 929–983 · [local source](../../../../../source/modules/aggregator/aggregator.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test#L929-L983)
- **Class:** [AggregatorRenderingTestCase](../AggregatorRenderingTestCase.md)
- **Module/theme:** aggregator

## Signature

```php
public function testBlockLinks()
```

## Documentation

```text
Adds a feed block to the page and checks its links.

@todo Test the category block as well.
```

## Code

```php
  public function testBlockLinks() {
    // Create feed.
    $this->createSampleNodes();
    $feed = $this->createFeed();
    $this->updateFeedItems($feed, $this->getDefaultFeedItemCount());

    // Place block on page (@see block.test:moveBlockToRegion())
    // Need admin user to be able to access block admin.
    $this->admin_user = $this->drupalCreateUser(array(
      'administer blocks',
      'access administration pages',
      'administer news feeds',
      'access news feeds',
    ));
    $this->drupalLogin($this->admin_user);

    // Prepare to use the block admin form.
    $block = array(
      'module' => 'aggregator',
      'delta' => 'feed-' . $feed->fid,
      'title' => $feed->title,
    );
    $region = 'footer';
    $edit = array();
    $edit['blocks[' . $block['module'] . '_' . $block['delta'] . '][region]'] = $region;
    // Check the feed block is available in the block list form.
    $this->drupalGet('admin/structure/block');
    $this->assertFieldByName('blocks[' . $block['module'] . '_' . $block['delta'] . '][region]', '', 'Aggregator feed block is available for positioning.');
    // Position it.
    $this->drupalPost('admin/structure/block', $edit, t('Save blocks'));
    $this->assertText(t('The block settings have been updated.'), format_string('Block successfully moved to %region_name region.', array( '%region_name' => $region)));
    // Confirm that the block is now being displayed on pages.
    $this->drupalGet('node');
    $this->assertText(t($block['title']), 'Feed block is displayed on the page.');

    // Find the expected read_more link.
    $href = 'aggregator/sources/' . $feed->fid;
    $links = $this->xpath('//a[@href = :href]', array(':href' => url($href)));
    $this->assert(isset($links[0]), format_string('Link to href %href found.', array('%href' => $href)));

    // Visit that page.
    $this->drupalGet($href);
    $correct_titles = $this->xpath('//h1[normalize-space(text())=:title]', array(':title' => $feed->title));
    $this->assertFalse(empty($correct_titles), 'Aggregator feed page is available and has the correct title.');

    // Set the number of news items to 0 to test that the block does not show
    // up.
    $feed->block = 0;
    aggregator_save_feed((array) $feed);
    // It is necessary to flush the cache after saving the number of items.
    drupal_flush_all_caches();
    // Check that the block is no longer displayed.
    $this->drupalGet('node');
    $this->assertNoText(t($block['title']), 'Feed block is not displayed on the page when number of items is set to 0.');
  }
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.test](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test) · Licensed GPL-2.0-or-later (see LICENSE)._
