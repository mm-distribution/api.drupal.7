# statistics_user_tracker()

- **Type:** Function
- **File:** [`modules/statistics/statistics.pages.inc`](_file.md), lines 67–101 · [local source](../../../../source/modules/statistics/statistics.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.pages.inc#L67-L101)
- **Module/theme:** statistics

## Signature

```php
function statistics_user_tracker()
```

## Documentation

```text
Page callback: Displays statistics for a user.

@return array
  A render array containing user statistics. If information for the user was
  not found, this will deliver a page not found error via drupal_not_found().
```

## Code

```php
function statistics_user_tracker() {
  if ($account = user_load(arg(1))) {

    $header = array(
        array('data' => t('Timestamp'), 'field' => 'timestamp', 'sort' => 'desc'),
        array('data' => t('Page'), 'field' => 'path'),
        array('data' => t('Operations')));
    $query = db_select('accesslog', 'a', array('target' => 'slave'))->extend('PagerDefault')->extend('TableSort');
    $query
      ->fields('a', array('aid', 'timestamp', 'path', 'title'))
      ->condition('uid', $account->uid)
      ->limit(30)
      ->orderByHeader($header);

    $result = $query->execute();
    $rows = array();
    foreach ($result as $log) {
      $rows[] = array(
        array('data' => format_date($log->timestamp, 'short'), 'class' => array('nowrap')),
        _statistics_format_item($log->title, $log->path),
        l(t('details'), "admin/reports/access/$log->aid"));
    }

    drupal_set_title(format_username($account));
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
