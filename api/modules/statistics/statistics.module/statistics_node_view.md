# statistics_node_view()

- **Type:** Function
- **File:** [`modules/statistics/statistics.module`](_file.md), lines 115–144 · [local source](../../../../source/modules/statistics/statistics.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.module#L115-L144)
- **Module/theme:** statistics
- **Implements:** [hook_node_view()](../../node/node.api.php/hook_node_view.md)

## Signature

```php
function statistics_node_view($node, $view_mode)
```

## Documentation

```text
Implements hook_node_view().
```

## Code

```php
function statistics_node_view($node, $view_mode) {
  // Attach Ajax node count statistics if configured.
  if (variable_get('statistics_count_content_views', 0) && variable_get('statistics_count_content_views_ajax', 0)) {
    if (!empty($node->nid) && $view_mode == 'full' && node_is_page($node) && empty($node->in_preview)) {
      $statistics = drupal_get_path('module', 'statistics') . '/statistics.js';
      $node->content['#attached']['js'][$statistics] = array(
        'scope' => 'footer',
      );
      $settings = array('data' => array('nid' => $node->nid), 'url' => url(drupal_get_path('module', 'statistics') . '/statistics.php'));
      $node->content['#attached']['js'][] = array(
        'data' => array('statistics' => $settings),
        'type' => 'setting',
      );
    }
  }

  if ($view_mode != 'rss') {
    if (user_access('view post access counter')) {
      $statistics = statistics_get($node->nid);
      if ($statistics) {
        $links['statistics_counter']['title'] = format_plural($statistics['totalcount'], '1 read', '@count reads');
        $node->content['links']['statistics'] = array(
          '#theme' => 'links__node__statistics',
          '#links' => $links,
          '#attributes' => array('class' => array('links', 'inline')),
        );
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/statistics/statistics.module](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.module) · Licensed GPL-2.0-or-later (see LICENSE)._
