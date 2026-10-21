# aggregator_page_rss()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.pages.inc`](_file.md), lines 404–419 · [local source](../../../../source/modules/aggregator/aggregator.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.pages.inc#L404-L419)
- **Module/theme:** aggregator

## Signature

```php
function aggregator_page_rss()
```

## Documentation

```text
Page callback: Generates an RSS 0.92 feed of aggregator items or categories.

@return string
  An HTML formatted string.
```

## Code

```php
function aggregator_page_rss() {
  $result = NULL;
  // arg(2) is the passed cid, only select for that category.
  if (arg(2)) {
    $category = db_query('SELECT cid, title FROM {aggregator_category} WHERE cid = :cid', array(':cid' => arg(2)))->fetchObject();
    $result = db_query_range('SELECT i.*, f.title AS ftitle, f.link AS flink FROM {aggregator_category_item} c LEFT JOIN {aggregator_item} i ON c.iid = i.iid LEFT JOIN {aggregator_feed} f ON i.fid = f.fid WHERE cid = :cid ORDER BY timestamp DESC, i.iid DESC', 0, variable_get('feed_default_items', 10), array(':cid' => $category->cid));
  }
  // Or, get the default aggregator items.
  else {
    $category = NULL;
    $result = db_query_range('SELECT i.*, f.title AS ftitle, f.link AS flink FROM {aggregator_item} i INNER JOIN {aggregator_feed} f ON i.fid = f.fid ORDER BY i.timestamp DESC, i.iid DESC', 0, variable_get('feed_default_items', 10));
  }

  $feeds = $result->fetchAll();
  return theme('aggregator_page_rss', array('feeds' => $feeds, 'category' => $category));
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
