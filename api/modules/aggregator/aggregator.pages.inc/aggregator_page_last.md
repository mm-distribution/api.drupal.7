# aggregator_page_last()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.pages.inc`](_file.md), lines 14–20 · [local source](../../../../source/modules/aggregator/aggregator.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.pages.inc#L14-L20)
- **Module/theme:** aggregator

## Signature

```php
function aggregator_page_last()
```

## Documentation

```text
Page callback: Displays the most recent items gathered from any feed.

@return
  The rendered list of items for the feed.
```

## Code

```php
function aggregator_page_last() {
  drupal_add_feed('aggregator/rss', variable_get('site_name', 'Drupal') . ' ' . t('aggregator'));

  $items = aggregator_feed_items_load('sum');

  return _aggregator_page_list($items, arg(1));
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
