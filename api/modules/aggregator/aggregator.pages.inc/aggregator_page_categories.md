# aggregator_page_categories()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.pages.inc`](_file.md), lines 379–396 · [local source](../../../../source/modules/aggregator/aggregator.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.pages.inc#L379-L396)
- **Module/theme:** aggregator

## Signature

```php
function aggregator_page_categories()
```

## Documentation

```text
Page callback: Displays all the categories used by the Aggregator module.

@return string
  An HTML formatted string.

@see aggregator_menu()
```

## Code

```php
function aggregator_page_categories() {
  $result = db_query('SELECT c.cid, c.title, c.description FROM {aggregator_category} c LEFT JOIN {aggregator_category_item} ci ON c.cid = ci.cid LEFT JOIN {aggregator_item} i ON ci.iid = i.iid GROUP BY c.cid, c.title, c.description');

  $output = '';
  foreach ($result as $category) {
    if (variable_get('aggregator_summary_items', 3)) {
      $summary_items = array();
      $items = db_query_range('SELECT i.title, i.timestamp, i.link, f.title as feed_title, f.link as feed_link FROM {aggregator_category_item} ci LEFT JOIN {aggregator_item} i ON i.iid = ci.iid LEFT JOIN {aggregator_feed} f ON i.fid = f.fid WHERE ci.cid = :cid ORDER BY i.timestamp DESC', 0, variable_get('aggregator_summary_items', 3), array(':cid' => $category->cid));
      foreach ($items as $item) {
        $summary_items[] = theme('aggregator_summary_item', array('item' => $item));
      }
    }
    $category->url = url('aggregator/categories/' . $category->cid);
    $output .= theme('aggregator_summary_items', array('summary_items' => $summary_items, 'source' => $category));
  }

  return theme('aggregator_wrapper', array('content' => $output));
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
