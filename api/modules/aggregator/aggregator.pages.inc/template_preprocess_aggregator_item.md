# template_preprocess_aggregator_item()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.pages.inc`](_file.md), lines 316–340 · [local source](../../../../source/modules/aggregator/aggregator.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.pages.inc#L316-L340)
- **Module/theme:** aggregator

## Signature

```php
function template_preprocess_aggregator_item(&$variables)
```

## Documentation

```text
Processes variables for aggregator-item.tpl.php.

@see aggregator-item.tpl.php
```

## Code

```php
function template_preprocess_aggregator_item(&$variables) {
  $item = $variables['item'];

  $variables['feed_url'] = check_url($item->link);
  $variables['feed_title'] = check_plain($item->title);
  $variables['content'] = aggregator_filter_xss($item->description);

  $variables['source_url'] = '';
  $variables['source_title'] = '';
  if (isset($item->ftitle) && isset($item->fid)) {
    $variables['source_url'] = url("aggregator/sources/$item->fid");
    $variables['source_title'] = check_plain($item->ftitle);
  }
  if (date('Ymd', $item->timestamp) == date('Ymd')) {
    $variables['source_date'] = t('%ago ago', array('%ago' => format_interval(REQUEST_TIME - $item->timestamp)));
  }
  else {
    $variables['source_date'] = format_date($item->timestamp, 'custom', variable_get('date_format_medium', 'D, m/d/Y - H:i'));
  }

  $variables['categories'] = array();
  foreach ($item->categories as $category) {
    $variables['categories'][$category->cid] = l($category->title, 'aggregator/categories/' . $category->cid);
  }
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
