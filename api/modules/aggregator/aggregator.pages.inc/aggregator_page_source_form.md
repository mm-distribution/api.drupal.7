# aggregator_page_source_form()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.pages.inc`](_file.md), lines 55–57 · [local source](../../../../source/modules/aggregator/aggregator.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.pages.inc#L55-L57)
- **Module/theme:** aggregator

## Signature

```php
function aggregator_page_source_form($form, $form_state, $feed)
```

## Documentation

```text
Page callback: Displays a form with all items captured from a feed.

@param $feed
  The feed for which to list all of the aggregated items.

@return
  The rendered list of items for the feed.

@see aggregator_page_source()
```

## Code

```php
function aggregator_page_source_form($form, $form_state, $feed) {
  return aggregator_page_source($feed);
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
