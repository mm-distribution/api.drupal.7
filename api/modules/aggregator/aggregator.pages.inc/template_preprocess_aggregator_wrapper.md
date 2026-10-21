# template_preprocess_aggregator_wrapper()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.pages.inc`](_file.md), lines 307–309 · [local source](../../../../source/modules/aggregator/aggregator.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.pages.inc#L307-L309)
- **Module/theme:** aggregator

## Signature

```php
function template_preprocess_aggregator_wrapper(&$variables)
```

## Documentation

```text
Processes variables for aggregator-wrapper.tpl.php.

@see aggregator-wrapper.tpl.php
```

## Code

```php
function template_preprocess_aggregator_wrapper(&$variables) {
  $variables['pager'] = theme('pager');
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
