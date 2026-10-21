# statistics_ranking()

- **Type:** Function
- **File:** [`modules/statistics/statistics.module`](_file.md), lines 438–455 · [local source](../../../../source/modules/statistics/statistics.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.module#L438-L455)
- **Module/theme:** statistics
- **Implements:** [hook_ranking()](../../node/node.api.php/hook_ranking.md)

## Signature

```php
function statistics_ranking()
```

## Documentation

```text
Implements hook_ranking().
```

## Code

```php
function statistics_ranking() {
  if (variable_get('statistics_count_content_views', 0)) {
    return array(
      'views' => array(
        'title' => t('Number of views'),
        'join' => array(
          'type' => 'LEFT',
          'table' => 'node_counter',
          'alias' => 'node_counter',
          'on' => 'node_counter.nid = i.sid',
        ),
        // Inverse law that maps the highest view count on the site to 1 and 0 to 0.
        'score' => '2.0 - 2.0 / (1.0 + node_counter.totalcount * CAST(:scale AS DECIMAL))',
        'arguments' => array(':scale' => variable_get('node_cron_views_scale', 0)),
      ),
    );
  }
}
```

---
_Drupal 7.103 · [modules/statistics/statistics.module](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.module) · Licensed GPL-2.0-or-later (see LICENSE)._
