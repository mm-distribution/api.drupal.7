# statistics_block_save()

- **Type:** Function
- **File:** [`modules/statistics/statistics.module`](_file.md), lines 351–355 · [local source](../../../../source/modules/statistics/statistics.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.module#L351-L355)
- **Module/theme:** statistics
- **Implements:** [hook_block_save()](../../block/block.api.php/hook_block_save.md)

## Signature

```php
function statistics_block_save($delta = '', $edit = array())
```

## Documentation

```text
Implements hook_block_save().
```

## Code

```php
function statistics_block_save($delta = '', $edit = array()) {
  variable_set('statistics_block_top_day_num', $edit['statistics_block_top_day_num']);
  variable_set('statistics_block_top_all_num', $edit['statistics_block_top_all_num']);
  variable_set('statistics_block_top_last_num', $edit['statistics_block_top_last_num']);
}
```

---
_Drupal 7.103 · [modules/statistics/statistics.module](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.module) · Licensed GPL-2.0-or-later (see LICENSE)._
