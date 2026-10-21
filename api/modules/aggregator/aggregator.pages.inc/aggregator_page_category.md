# aggregator_page_category()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.pages.inc`](_file.md), lines 68–76 · [local source](../../../../source/modules/aggregator/aggregator.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.pages.inc#L68-L76)
- **Module/theme:** aggregator

## Signature

```php
function aggregator_page_category($category)
```

## Documentation

```text
Page callback: Displays all the items aggregated in a particular category.

@param $category
  The category for which to list all of the aggregated items.

@return
  The rendered list of items for the feed.
```

## Code

```php
function aggregator_page_category($category) {
  drupal_add_feed('aggregator/rss/' . $category['cid'], variable_get('site_name', 'Drupal') . ' ' . t('aggregator - @title', array('@title' => $category['title'])));

  // It is safe to include the cid in the query because it's loaded from the
  // database by aggregator_category_load.
  $items = aggregator_feed_items_load('category', $category);

  return _aggregator_page_list($items, arg(3));
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
