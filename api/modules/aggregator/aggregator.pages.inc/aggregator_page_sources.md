# aggregator_page_sources()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.pages.inc`](_file.md), lines 350–369 · [local source](../../../../source/modules/aggregator/aggregator.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.pages.inc#L350-L369)
- **Module/theme:** aggregator

## Signature

```php
function aggregator_page_sources()
```

## Documentation

```text
Page callback: Displays all the feeds used by the aggregator.

@return
  An HTML-formatted string.

@see aggregator_menu()
```

## Code

```php
function aggregator_page_sources() {
  $result = db_query('SELECT f.fid, f.title, f.description, f.image, MAX(i.timestamp) AS last FROM {aggregator_feed} f LEFT JOIN {aggregator_item} i ON f.fid = i.fid GROUP BY f.fid, f.title, f.description, f.image ORDER BY last DESC, f.title');

  $output = '';
  foreach ($result as $feed) {
    // Most recent items:
    $summary_items = array();
    if (variable_get('aggregator_summary_items', 3)) {
      $items = db_query_range('SELECT i.title, i.timestamp, i.link FROM {aggregator_item} i WHERE i.fid = :fid ORDER BY i.timestamp DESC', 0, variable_get('aggregator_summary_items', 3), array(':fid' => $feed->fid));
      foreach ($items as $item) {
        $summary_items[] = theme('aggregator_summary_item', array('item' => $item));
      }
    }
    $feed->url = url('aggregator/sources/' . $feed->fid);
    $output .= theme('aggregator_summary_items', array('summary_items' => $summary_items, 'source' => $feed));
  }
  $output .= theme('feed_icon', array('url' => 'aggregator/opml', 'title' => t('OPML feed')));

  return theme('aggregator_wrapper', array('content' => $output));
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
