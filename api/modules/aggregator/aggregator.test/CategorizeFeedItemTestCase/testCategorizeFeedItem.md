# CategorizeFeedItemTestCase::testCategorizeFeedItem()

- **Type:** Method
- **File:** [`modules/aggregator/aggregator.test`](../_file.md), lines 677–729 · [local source](../../../../../source/modules/aggregator/aggregator.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test#L677-L729)
- **Class:** [CategorizeFeedItemTestCase](../CategorizeFeedItemTestCase.md)
- **Module/theme:** aggregator

## Signature

```php
function testCategorizeFeedItem()
```

## Documentation

```text
Checks that children of a feed inherit a defined category.

If a feed has a category, make sure that the children inherit that
categorization.
```

## Code

```php
  function testCategorizeFeedItem() {
    $this->createSampleNodes();

    // Simulate form submission on "admin/config/services/aggregator/add/category".
    $edit = array('title' => $this->randomName(10), 'description' => '');
    $this->drupalPost('admin/config/services/aggregator/add/category', $edit, t('Save'));
    $this->assertRaw(t('The category %title has been added.', array('%title' => $edit['title'])), format_string('The category %title has been added.', array('%title' => $edit['title'])));

    $category = db_query("SELECT * FROM {aggregator_category} WHERE title = :title", array(':title' => $edit['title']))->fetch();
    $this->assertTrue(!empty($category), 'The category found in database.');

    $link_path = 'aggregator/categories/' . $category->cid;
    $menu_link = db_query("SELECT * FROM {menu_links} WHERE link_path = :link_path", array(':link_path' => $link_path))->fetch();
    $this->assertTrue(!empty($menu_link), 'The menu link associated with the category found in database.');

    $feed = $this->createFeed();
    db_insert('aggregator_category_feed')
      ->fields(array(
        'cid' => $category->cid,
        'fid' => $feed->fid,
      ))
      ->execute();
    $this->updateFeedItems($feed, $this->getDefaultFeedItemCount());
    $this->getFeedCategories($feed);
    $this->assertTrue(!empty($feed->categories), 'The category found in the feed.');

    // For each category of a feed, ensure feed items have that category, too.
    if (!empty($feed->categories) && !empty($feed->items)) {
      foreach ($feed->categories as $category) {
        $categorized_count = db_select('aggregator_category_item')
          ->condition('iid', $feed->items, 'IN')
          ->countQuery()
          ->execute()
          ->fetchField();

        $this->assertEqual($feed->item_count, $categorized_count, 'Total items in feed equal to the total categorized feed items in database');
      }
    }

    // Delete category from feed items when category is deleted.
    $cid = reset($feed->categories);
    $categories = $this->getCategories();
    $category_title = $categories[$cid]->title;

    // Delete category.
    aggregator_save_category(array('cid' => $cid));

    // Assert category has been removed from feed items.
    $categorized_count = db_query("SELECT COUNT(*) FROM {aggregator_category_item} WHERE cid = :cid", array(':cid' => $cid))->fetchField();
    $this->assertFalse($categorized_count, format_string('The category %title has been removed from feed items.', array('%title' => $category_title)));
    // Delete feed.
    $this->deleteFeed($feed);
  }
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.test](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test) · Licensed GPL-2.0-or-later (see LICENSE)._
