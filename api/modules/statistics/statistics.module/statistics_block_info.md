# statistics_block_info()

- **Type:** Function
- **File:** [`modules/statistics/statistics.module`](_file.md), lines 325–334 · [local source](../../../../source/modules/statistics/statistics.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.module#L325-L334)
- **Module/theme:** statistics
- **Implements:** [hook_block_info()](../../block/block.api.php/hook_block_info.md)

## Signature

```php
function statistics_block_info()
```

## Documentation

```text
Implements hook_block_info().
```

## Code

```php
function statistics_block_info() {
  $blocks = array();

  if (variable_get('statistics_count_content_views', 0)) {
    $blocks['popular']['info'] = t('Popular content');
    // Too dynamic to cache.
    $blocks['popular']['cache'] = DRUPAL_NO_CACHE;
  }
  return $blocks;
}
```

---
_Drupal 7.103 · [modules/statistics/statistics.module](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.module) · Licensed GPL-2.0-or-later (see LICENSE)._
