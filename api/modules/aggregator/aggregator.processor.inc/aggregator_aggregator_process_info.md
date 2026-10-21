# aggregator_aggregator_process_info()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.processor.inc`](_file.md), lines 11–16 · [local source](../../../../source/modules/aggregator/aggregator.processor.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.processor.inc#L11-L16)
- **Module/theme:** aggregator
- **Implements:** [hook_aggregator_process_info()](../aggregator.api.php/hook_aggregator_process_info.md)

## Signature

```php
function aggregator_aggregator_process_info()
```

## Documentation

```text
Implements hook_aggregator_process_info().
```

## Code

```php
function aggregator_aggregator_process_info() {
  return array(
    'title' => t('Default processor'),
    'description' => t('Creates lightweight records from feed items.'),
  );
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.processor.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.processor.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
