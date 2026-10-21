# statistics_node_tracker()

- **Type:** Function
- **File:** [`modules/statistics/statistics.pages.inc`](_file.md), lines 15–58 · [local source](../../../../source/modules/statistics/statistics.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.pages.inc#L15-L58)
- **Module/theme:** statistics

## Signature

```php
function statistics_node_tracker()
```

## Documentation

```text
Page callback: Displays statistics for a node.

@return
  A render array containing node statistics. If information for the node was
  not found, this will deliver a page not found error via drupal_not_found().
```

## Code

```php
function statistics_node_tracker() {
  if ($node = node_load(arg(1))) {

    $header = array(
        array('data' => t('Time'), 'field' => 'a.timestamp', 'sort' => 'desc'),
        array('data' => t('Referrer'), 'field' => 'a.url'),
        array('data' => t('User'), 'field' => 'u.name'),
        array('data' => t('Operations')));

    $query = db_select('accesslog', 'a', array('target' => 'slave'))->extend('PagerDefault')->extend('TableSort');
    $query->join('users', 'u', 'a.uid = u.uid');

    $query
      ->fields('a', array('aid', 'timestamp', 'url', 'uid'))
      ->fields('u', array('name'))
      ->condition(db_or()
        ->condition('a.path', 'node/' . $node->nid)
        ->condition('a.path', 'node/' . $node->nid . '/%', 'LIKE'))
      ->limit(30)
      ->orderByHeader($header);

    $result = $query->execute();
    $rows = array();
    foreach ($result as $log) {
      $rows[] = array(
        array('data' => format_date($log->timestamp, 'short'), 'class' => array('nowrap')),
        _statistics_link($log->url),
        theme('username', array('account' => $log)),
        l(t('details'), "admin/reports/access/$log->aid"),
      );
    }

    drupal_set_title($node->title);
    $build['statistics_table'] = array(
      '#theme' => 'table',
      '#header' => $header,
      '#rows' => $rows,
      '#empty' => t('No statistics available.'),
    );
    $build['statistics_pager'] = array('#theme' => 'pager');
    return $build;
  }
  return MENU_NOT_FOUND;
}
```

---
_Drupal 7.103 · [modules/statistics/statistics.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
