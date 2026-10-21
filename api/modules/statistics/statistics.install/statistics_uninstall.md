# statistics_uninstall()

- **Type:** Function
- **File:** [`modules/statistics/statistics.install`](_file.md), lines 11–21 · [local source](../../../../source/modules/statistics/statistics.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.install#L11-L21)
- **Module/theme:** statistics
- **Implements:** [hook_uninstall()](../../system/system.api.php/hook_uninstall.md)

## Signature

```php
function statistics_uninstall()
```

## Documentation

```text
Implements hook_uninstall().
```

## Code

```php
function statistics_uninstall() {
  // Remove variables.
  variable_del('statistics_count_content_views');
  variable_del('statistics_count_content_views_ajax');
  variable_del('statistics_enable_access_log');
  variable_del('statistics_flush_accesslog_timer');
  variable_del('statistics_day_timestamp');
  variable_del('statistics_block_top_day_num');
  variable_del('statistics_block_top_all_num');
  variable_del('statistics_block_top_last_num');
}
```

---
_Drupal 7.103 · [modules/statistics/statistics.install](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.install) · Licensed GPL-2.0-or-later (see LICENSE)._
