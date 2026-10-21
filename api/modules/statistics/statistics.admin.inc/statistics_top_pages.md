# statistics_top_pages()

- **Type:** Function
- **File:** [`modules/statistics/statistics.admin.inc`](_file.md), lines 64–105 · [local source](../../../../source/modules/statistics/statistics.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.admin.inc#L64-L105)
- **Module/theme:** statistics

## Signature

```php
function statistics_top_pages()
```

## Documentation

```text
Page callback: Displays statistics for the "top pages" (most accesses).

This displays the pages with the most hits (the "top pages") within a given
time period that haven't been flushed yet. The flush interval is set on the
statistics settings form, but is dependent on cron running.

@return
  A render array containing information about the top pages.
```

## Code

```php
function statistics_top_pages() {
  $header = array(
    array('data' => t('Hits'), 'field' => 'hits', 'sort' => 'desc'),
    array('data' => t('Page'), 'field' => 'path'),
    array('data' => t('Average page generation time'), 'field' => 'average_time'),
    array('data' => t('Total page generation time'), 'field' => 'total_time')
  );

  $query = db_select('accesslog', 'a', array('target' => 'slave'))->extend('PagerDefault')->extend('TableSort');
  $query->addExpression('COUNT(path)', 'hits');
  // MAX(title) avoids having empty node titles which otherwise causes
  // duplicates in the top pages list.
  $query->addExpression('MAX(title)', 'title');
  $query->addExpression('AVG(timer)', 'average_time');
  $query->addExpression('SUM(timer)', 'total_time');

  $query
    ->fields('a', array('path'))
    ->groupBy('path')
    ->limit(30)
    ->orderByHeader($header);

  $count_query = db_select('accesslog', 'a', array('target' => 'slave'));
  $count_query->addExpression('COUNT(DISTINCT path)');
  $query->setCountQuery($count_query);

  $result = $query->execute();
  $rows = array();
  foreach ($result as $page) {
    $rows[] = array($page->hits, _statistics_format_item($page->title, $page->path), t('%time ms', array('%time' => round($page->average_time))), format_interval(round($page->total_time / 1000)));
  }

  drupal_set_title(t('Top pages in the past %interval', array('%interval' => format_interval(variable_get('statistics_flush_accesslog_timer', 259200)))), PASS_THROUGH);
  $build['statistics_top_pages_table'] = array(
    '#theme' => 'table',
    '#header' => $header,
    '#rows' => $rows,
    '#empty' => t('No statistics available.'),
  );
  $build['statistics_top_pages_pager'] = array('#theme' => 'pager');
  return $build;
}
```

---
_Drupal 7.103 · [modules/statistics/statistics.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
