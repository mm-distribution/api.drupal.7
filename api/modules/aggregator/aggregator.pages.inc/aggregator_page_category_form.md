# aggregator_page_category_form()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.pages.inc`](_file.md), lines 89–91 · [local source](../../../../source/modules/aggregator/aggregator.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.pages.inc#L89-L91)
- **Module/theme:** aggregator

## Signature

```php
function aggregator_page_category_form($form, $form_state, $category)
```

## Documentation

```text
Page callback: Displays a form containing items aggregated in a category.

@param $category
  The category for which to list all of the aggregated items.

@return
  The rendered list of items for the feed.

@see aggregator_page_category()
```

## Code

```php
function aggregator_page_category_form($form, $form_state, $category) {
  return aggregator_page_category($category);
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
