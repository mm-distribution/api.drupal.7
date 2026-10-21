# aggregator_uninstall()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.install`](_file.md), lines 11–20 · [local source](../../../../source/modules/aggregator/aggregator.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.install#L11-L20)
- **Module/theme:** aggregator
- **Implements:** [hook_uninstall()](../../system/system.api.php/hook_uninstall.md)

## Signature

```php
function aggregator_uninstall()
```

## Documentation

```text
Implements hook_uninstall().
```

## Code

```php
function aggregator_uninstall() {
  variable_del('aggregator_allowed_html_tags');
  variable_del('aggregator_summary_items');
  variable_del('aggregator_clear');
  variable_del('aggregator_category_selector');
  variable_del('aggregator_fetcher');
  variable_del('aggregator_parser');
  variable_del('aggregator_processors');
  variable_del('aggregator_teaser_length');
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.install](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.install) · Licensed GPL-2.0-or-later (see LICENSE)._
