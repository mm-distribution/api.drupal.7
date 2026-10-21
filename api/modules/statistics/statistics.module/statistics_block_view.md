# statistics_block_view()

- **Type:** Function
- **File:** [`modules/statistics/statistics.module`](_file.md), lines 360–388 · [local source](../../../../source/modules/statistics/statistics.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.module#L360-L388)
- **Module/theme:** statistics
- **Implements:** [hook_block_view()](../../block/block.api.php/hook_block_view.md)

## Signature

```php
function statistics_block_view($delta = '')
```

## Documentation

```text
Implements hook_block_view().
```

## Code

```php
function statistics_block_view($delta = '') {
  if (user_access('access content')) {
    $content = array();

    $daytop = variable_get('statistics_block_top_day_num', 0);
    if ($daytop && ($result = statistics_title_list('daycount', $daytop)) && ($node_title_list = node_title_list($result, t("Today's:")))) {
      $content['top_day'] = $node_title_list;
      $content['top_day']['#suffix'] = '<br />';
    }

    $alltimetop = variable_get('statistics_block_top_all_num', 0);
    if ($alltimetop && ($result = statistics_title_list('totalcount', $alltimetop)) && ($node_title_list = node_title_list($result, t('All time:')))) {
      $content['top_all'] = $node_title_list;
      $content['top_all']['#suffix'] = '<br />';
    }

    $lasttop = variable_get('statistics_block_top_last_num', 0);
    if ($lasttop && ($result = statistics_title_list('timestamp', $lasttop)) && ($node_title_list = node_title_list($result, t('Last viewed:')))) {
      $content['top_last'] = $node_title_list;
      $content['top_last']['#suffix'] = '<br />';
    }

    if (count($content)) {
      $block['content'] = $content;
      $block['subject'] = t('Popular content');
      return $block;
    }
  }
}
```

---
_Drupal 7.103 · [modules/statistics/statistics.module](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.module) · Licensed GPL-2.0-or-later (see LICENSE)._
