# statistics_top_referrers()

- **Type:** Function
- **File:** [`modules/statistics/statistics.admin.inc`](_file.md), lines 178–219 · [local source](../../../../source/modules/statistics/statistics.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.admin.inc#L178-L219)
- **Module/theme:** statistics

## Signature

```php
function statistics_top_referrers()
```

## Documentation

```text
Page callback: Displays the "top referrers" in the access logs.

This displays the pages with the top referrers in a given time interval that
haven't been flushed yet. The flush interval is set on the statistics
settings form, but is dependent on cron running.

@return
  A render array containing the top referrers information.
```

## Code

```php
function statistics_top_referrers() {
  drupal_set_title(t('Top referrers in the past %interval', array('%interval' => format_interval(variable_get('statistics_flush_accesslog_timer', 259200)))), PASS_THROUGH);

  $header = array(
    array('data' => t('Hits'), 'field' => 'hits', 'sort' => 'desc'),
    array('data' => t('Url'), 'field' => 'url'),
    array('data' => t('Last visit'), 'field' => 'last'),
  );
  $query = db_select('accesslog', 'a')->extend('PagerDefault')->extend('TableSort');

  $query->addExpression('COUNT(url)', 'hits');
  $query->addExpression('MAX(timestamp)', 'last');
  $query
    ->fields('a', array('url'))
    ->condition('url', '%' . $_SERVER['HTTP_HOST'] . '%', 'NOT LIKE')
    ->condition('url', '', '<>')
    ->groupBy('url')
    ->limit(30)
    ->orderByHeader($header);

  $count_query = db_select('accesslog', 'a', array('target' => 'slave'));
  $count_query->addExpression('COUNT(DISTINCT url)');
  $count_query
    ->condition('url', '%' . $_SERVER['HTTP_HOST'] . '%', 'NOT LIKE')
    ->condition('url', '', '<>');
  $query->setCountQuery($count_query);

  $result = $query->execute();
  $rows = array();
  foreach ($result as $referrer) {
    $rows[] = array($referrer->hits, _statistics_link($referrer->url), t('@time ago', array('@time' => format_interval(REQUEST_TIME - $referrer->last))));
  }

  $build['statistics_top_referrers_table'] = array(
    '#theme' => 'table',
    '#header' => $header,
    '#rows' => $rows,
    '#empty' => t('No statistics available.'),
  );
  $build['statistics_top_referrers_pager'] = array('#theme' => 'pager');
  return $build;
}
```

---
_Drupal 7.103 · [modules/statistics/statistics.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
