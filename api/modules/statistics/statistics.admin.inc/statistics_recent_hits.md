# statistics_recent_hits()

- **Type:** Function
- **File:** [`modules/statistics/statistics.admin.inc`](_file.md), lines 18–52 · [local source](../../../../source/modules/statistics/statistics.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.admin.inc#L18-L52)
- **Module/theme:** statistics

## Signature

```php
function statistics_recent_hits()
```

## Documentation

```text
Page callback: Displays the "recent hits" page.

This displays the pages with recent hits in a given time interval that
haven't been flushed yet. The flush interval is set on the statistics
settings form, but is dependent on cron running.

@return
  A render array containing information about the most recent hits.
```

## Code

```php
function statistics_recent_hits() {
  $header = array(
    array('data' => t('Timestamp'), 'field' => 'a.timestamp', 'sort' => 'desc'),
    array('data' => t('Page'), 'field' => 'a.path'),
    array('data' => t('User'), 'field' => 'u.name'),
    array('data' => t('Operations'))
  );

  $query = db_select('accesslog', 'a', array('target' => 'slave'))->extend('PagerDefault')->extend('TableSort');
  $query->join('users', 'u', 'a.uid = u.uid');
  $query
    ->fields('a', array('aid', 'timestamp', 'path', 'title', 'uid'))
    ->fields('u', array('name'))
    ->limit(30)
    ->orderByHeader($header);

  $result = $query->execute();
  $rows = array();
  foreach ($result as $log) {
    $rows[] = array(
      array('data' => format_date($log->timestamp, 'short'), 'class' => array('nowrap')),
      _statistics_format_item($log->title, $log->path),
      theme('username', array('account' => $log)),
      l(t('details'), "admin/reports/access/$log->aid"));
  }

  $build['statistics_table'] = array(
    '#theme' => 'table',
    '#header' => $header,
    '#rows' => $rows,
    '#empty' => t('No statistics available.'),
  );
  $build['statistics_pager'] = array('#theme' => 'pager');
  return $build;
}
```

---
_Drupal 7.103 · [modules/statistics/statistics.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
