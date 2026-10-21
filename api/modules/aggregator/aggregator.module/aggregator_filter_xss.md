# aggregator_filter_xss()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.module`](_file.md), lines 742–744 · [local source](../../../../source/modules/aggregator/aggregator.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.module#L742-L744)
- **Module/theme:** aggregator

## Signature

```php
function aggregator_filter_xss($value)
```

## Documentation

```text
Renders the HTML content safely, as allowed.

@param $value
  The content to be filtered.

@return
  The filtered content.
```

## Code

```php
function aggregator_filter_xss($value) {
  return filter_xss($value, preg_split('/\s+|<|>/', variable_get('aggregator_allowed_html_tags', '<a> <b> <br> <dd> <dl> <dt> <em> <i> <li> <ol> <p> <strong> <u> <ul>'), -1, PREG_SPLIT_NO_EMPTY));
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.module](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.module) · Licensed GPL-2.0-or-later (see LICENSE)._
