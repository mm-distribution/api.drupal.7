# statistics_block_configure()

- **Type:** Function
- **File:** [`modules/statistics/statistics.module`](_file.md), lines 339–346 · [local source](../../../../source/modules/statistics/statistics.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.module#L339-L346)
- **Module/theme:** statistics
- **Implements:** [hook_block_configure()](../../block/block.api.php/hook_block_configure.md)

## Signature

```php
function statistics_block_configure($delta = '')
```

## Documentation

```text
Implements hook_block_configure().
```

## Code

```php
function statistics_block_configure($delta = '') {
  // Popular content block settings
  $numbers = array('0' => t('Disabled')) + drupal_map_assoc(array(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30, 40));
  $form['statistics_block_top_day_num'] = array('#type' => 'select', '#title' => t("Number of day's top views to display"), '#default_value' => variable_get('statistics_block_top_day_num', 0), '#options' => $numbers, '#description' => t('How many content items to display in "day" list.'));
  $form['statistics_block_top_all_num'] = array('#type' => 'select', '#title' => t('Number of all time views to display'), '#default_value' => variable_get('statistics_block_top_all_num', 0), '#options' => $numbers, '#description' => t('How many content items to display in "all time" list.'));
  $form['statistics_block_top_last_num'] = array('#type' => 'select', '#title' => t('Number of most recent views to display'), '#default_value' => variable_get('statistics_block_top_last_num', 0), '#options' => $numbers, '#description' => t('How many content items to display in "recently viewed" list.'));
  return $form;
}
```

---
_Drupal 7.103 · [modules/statistics/statistics.module](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.module) · Licensed GPL-2.0-or-later (see LICENSE)._
