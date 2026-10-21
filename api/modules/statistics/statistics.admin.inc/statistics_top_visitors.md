# statistics_top_visitors()

- **Type:** Function
- **File:** [`modules/statistics/statistics.admin.inc`](_file.md), lines 117–166 · [local source](../../../../source/modules/statistics/statistics.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.admin.inc#L117-L166)
- **Module/theme:** statistics

## Signature

```php
function statistics_top_visitors()
```

## Documentation

```text
Page callback: Displays the "top visitors" page.

This displays the pages with the top number of visitors in a given time
interval that haven't been flushed yet. The flush interval is set on the
statistics settings form, but is dependent on cron running.

@return
  A render array containing the top visitors information.
```

## Code

```php
function statistics_top_visitors() {

  $header = array(
    array('data' => t('Hits'), 'field' => 'hits', 'sort' => 'desc'),
    array('data' => t('Visitor'), 'field' => 'u.name'),
    array('data' => t('Total page generation time'), 'field' => 'total'),
    array('data' => user_access('block IP addresses') ? t('Operations') : '', 'colspan' => 2),
  );
  $query = db_select('accesslog', 'a', array('target' => 'slave'))->extend('PagerDefault')->extend('TableSort');
  $query->leftJoin('blocked_ips', 'bl', 'a.hostname = bl.ip');
  $query->leftJoin('users', 'u', 'a.uid = u.uid');

  $query->addExpression('COUNT(a.uid)', 'hits');
  $query->addExpression('SUM(a.timer)', 'total');
  $query
    ->fields('a', array('uid', 'hostname'))
    ->fields('u', array('name'))
    ->fields('bl', array('iid'))
    ->groupBy('a.hostname')
    ->groupBy('a.uid')
    ->groupBy('u.name')
    ->groupBy('bl.iid')
    ->limit(30)
    ->orderByHeader($header)
    ->orderBy('a.hostname');

  $uniques_query = db_select('accesslog')->distinct();
  $uniques_query->fields('accesslog', array('uid', 'hostname'));
  $count_query = db_select($uniques_query);
  $count_query->addExpression('COUNT(*)');
  $query->setCountQuery($count_query);

  $result = $query->execute();
  $rows = array();
  $destination = drupal_get_destination();
  foreach ($result as $account) {
    $ban_link = $account->iid ? l(t('unblock IP address'), "admin/config/people/ip-blocking/delete/$account->iid", array('query' => $destination)) : l(t('block IP address'), "admin/config/people/ip-blocking/$account->hostname", array('query' => $destination));
    $rows[] = array($account->hits, ($account->uid ? theme('username', array('account' => $account)) : $account->hostname), format_interval(round($account->total / 1000)), (user_access('block IP addresses') && !$account->uid) ? $ban_link : '');
  }

  drupal_set_title(t('Top visitors in the past %interval', array('%interval' => format_interval(variable_get('statistics_flush_accesslog_timer', 259200)))), PASS_THROUGH);
  $build['statistics_top_visitors_table'] = array(
    '#theme' => 'table',
    '#header' => $header,
    '#rows' => $rows,
    '#empty' => t('No statistics available.'),
  );
  $build['statistics_top_visitors_pager'] = array('#theme' => 'pager');
  return $build;
}
```

---
_Drupal 7.103 · [modules/statistics/statistics.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
