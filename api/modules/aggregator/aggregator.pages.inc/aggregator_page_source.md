# aggregator_page_source()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.pages.inc`](_file.md), lines 33–42 · [local source](../../../../source/modules/aggregator/aggregator.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.pages.inc#L33-L42)
- **Module/theme:** aggregator

## Signature

```php
function aggregator_page_source($feed)
```

## Documentation

```text
Page callback: Displays all the items captured from the particular feed.

@param $feed
  The feed for which to display all items.

@return
  The rendered list of items for a feed.

@see aggregator_menu()
```

## Code

```php
function aggregator_page_source($feed) {
  drupal_set_title($feed->title);
  $feed_source = theme('aggregator_feed_source', array('feed' => $feed));

  // It is safe to include the fid in the query because it's loaded from the
  // database by aggregator_feed_load.
  $items = aggregator_feed_items_load('source', $feed);

  return _aggregator_page_list($items, arg(3), $feed_source);
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
