# CategorizeFeedTestCase::testCategorizeFeed()

- **Type:** Method
- **File:** [`modules/aggregator/aggregator.test`](../_file.md), lines 427–478 · [local source](../../../../../source/modules/aggregator/aggregator.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test#L427-L478)
- **Class:** [CategorizeFeedTestCase](../CategorizeFeedTestCase.md)
- **Module/theme:** aggregator

## Signature

```php
function testCategorizeFeed()
```

## Documentation

```text
Creates a feed and makes sure you can add/delete categories to it.
```

## Code

```php
  function testCategorizeFeed() {

    // Create 2 categories.
    $category_1 = array('title' => $this->randomName(10), 'description' => '');
    $this->drupalPost('admin/config/services/aggregator/add/category', $category_1, t('Save'));
    $this->assertRaw(t('The category %title has been added.', array('%title' => $category_1['title'])), format_string('The category %title has been added.', array('%title' => $category_1['title'])));

    $category_2 = array('title' => $this->randomName(10), 'description' => '');
    $this->drupalPost('admin/config/services/aggregator/add/category', $category_2, t('Save'));
    $this->assertRaw(t('The category %title has been added.', array('%title' => $category_2['title'])), format_string('The category %title has been added.', array('%title' => $category_2['title'])));

    // Get categories from database.
    $categories = $this->getCategories();

    // Create a feed and assign 2 categories to it.
    $feed = $this->getFeedEditArray();
    $feed['block'] = 5;
    foreach ($categories as $cid => $category) {
      $feed['category'][$cid] = $cid;
    }

    // Use aggregator_save_feed() function to save the feed.
    aggregator_save_feed($feed);
    $db_feed = db_query("SELECT *  FROM {aggregator_feed} WHERE title = :title AND url = :url", array(':title' => $feed['title'], ':url' => $feed['url']))->fetch();

    // Assert the feed has two categories.
    $this->getFeedCategories($db_feed);
    $this->assertEqual(count($db_feed->categories), 2, 'Feed has 2 categories');

    // Use aggregator_save_feed() to delete a category.
    $category = reset($categories);
    aggregator_save_category(array('cid' => $category->cid));

    // Assert that category is deleted.
    $db_category = db_query("SELECT COUNT(*) FROM {aggregator_category} WHERE cid = :cid", array(':cid' => $category->cid))->fetchField();
    $this->assertFalse($db_category, format_string('The category %title has been deleted.', array('%title' => $category->title)));

    // Assert that category has been removed from feed.
    $categorized_feeds = db_query("SELECT COUNT(*) FROM {aggregator_category_feed} WHERE cid = :cid", array(':cid' => $category->cid))->fetchField();
    $this->assertFalse($categorized_feeds, format_string('The category %title has been removed from feed %feed_title.', array('%title' => $category->title, '%feed_title' => $feed['title'])));

    // Assert that no broken links (associated with the deleted category)
    // appear on one of the other category pages.
    $this->createSampleNodes();
    $this->drupalGet('admin/config/services/aggregator');
    $this->clickLink('update items');
    $categories = $this->getCategories();
    $category = reset($categories);
    $this->drupalGet('aggregator/categories/' . $category->cid);
    global $base_path;
    $this->assertNoRaw('<a href="' . $base_path . 'aggregator/categories/"></a>,');
  }
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.test](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test) · Licensed GPL-2.0-or-later (see LICENSE)._
