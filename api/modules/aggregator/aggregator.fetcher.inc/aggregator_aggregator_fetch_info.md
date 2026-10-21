# aggregator_aggregator_fetch_info()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.fetcher.inc`](_file.md), lines 11–16 · [local source](../../../../source/modules/aggregator/aggregator.fetcher.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.fetcher.inc#L11-L16)
- **Module/theme:** aggregator
- **Implements:** [hook_aggregator_fetch_info()](../aggregator.api.php/hook_aggregator_fetch_info.md)

## Signature

```php
function aggregator_aggregator_fetch_info()
```

## Documentation

```text
Implements hook_aggregator_fetch_info().
```

## Code

```php
function aggregator_aggregator_fetch_info() {
  return array(
    'title' => t('Default fetcher'),
    'description' => t('Downloads data from a URL using Drupal\'s HTTP request handler.'),
  );
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.fetcher.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.fetcher.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
