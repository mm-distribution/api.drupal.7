# template_preprocess_aggregator_summary_items()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.pages.inc`](_file.md), lines 526–530 · [local source](../../../../source/modules/aggregator/aggregator.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.pages.inc#L526-L530)
- **Module/theme:** aggregator

## Signature

```php
function template_preprocess_aggregator_summary_items(&$variables)
```

## Documentation

```text
Processes variables for aggregator-summary-items.tpl.php.

@see aggregator-summary-items.tpl.php
```

## Code

```php
function template_preprocess_aggregator_summary_items(&$variables) {
  $variables['title'] = check_plain($variables['source']->title);
  $variables['summary_list'] = theme('item_list', array('items' => $variables['summary_items']));
  $variables['source_url'] = $variables['source']->url;
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
