# template_preprocess_aggregator_summary_item()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.pages.inc`](_file.md), lines 537–550 · [local source](../../../../source/modules/aggregator/aggregator.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.pages.inc#L537-L550)
- **Module/theme:** aggregator

## Signature

```php
function template_preprocess_aggregator_summary_item(&$variables)
```

## Documentation

```text
Processes variables for aggregator-summary-item.tpl.php.

@see aggregator-summary-item.tpl.php
```

## Code

```php
function template_preprocess_aggregator_summary_item(&$variables) {
  $item = $variables['item'];

  $variables['feed_url'] = check_url($item->link);
  $variables['feed_title'] = check_plain($item->title);
  $variables['feed_age'] = t('%age old', array('%age' => format_interval(REQUEST_TIME - $item->timestamp)));

  $variables['source_url'] = '';
  $variables['source_title'] = '';
  if (!empty($item->feed_link)) {
    $variables['source_url'] = check_url($item->feed_link);
    $variables['source_title'] = check_plain($item->feed_title);
  }
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
