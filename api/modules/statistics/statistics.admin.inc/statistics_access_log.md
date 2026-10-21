# statistics_access_log()

- **Type:** Function
- **File:** [`modules/statistics/statistics.admin.inc`](_file.md), lines 231–268 · [local source](../../../../source/modules/statistics/statistics.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.admin.inc#L231-L268)
- **Module/theme:** statistics

## Signature

```php
function statistics_access_log($aid)
```

## Documentation

```text
Page callback: Gathers page access statistics suitable for rendering.

@param $aid
  The unique accesslog ID.

@return
  A render array containing page access statistics. If information for the
  page was not found, drupal_not_found() is called.
```

## Code

```php
function statistics_access_log($aid) {
  $access = db_query('SELECT a.*, u.name FROM {accesslog} a LEFT JOIN {users} u ON a.uid = u.uid WHERE aid = :aid', array(':aid' => $aid))->fetch();
  if ($access) {
    $rows[] = array(
      array('data' => t('URL'), 'header' => TRUE),
      l(url($access->path, array('absolute' => TRUE)), $access->path)
    );
    // It is safe to avoid filtering $access->title through check_plain because
    // it comes from drupal_get_title().
    $rows[] = array(
      array('data' => t('Title'), 'header' => TRUE),
      $access->title
    );
    $rows[] = array(
      array('data' => t('Referrer'), 'header' => TRUE),
      ($access->url ? l($access->url, $access->url) : '')
    );
    $rows[] = array(
      array('data' => t('Date'), 'header' => TRUE),
      format_date($access->timestamp, 'long')
    );
    $rows[] = array(
      array('data' => t('User'), 'header' => TRUE),
      theme('username', array('account' => $access))
    );
    $rows[] = array(
      array('data' => t('Hostname'), 'header' => TRUE),
      check_plain($access->hostname)
    );

    $build['statistics_table'] = array(
      '#theme' => 'table',
      '#rows' => $rows,
    );
    return $build;
  }
  return MENU_NOT_FOUND;
}
```

---
_Drupal 7.103 · [modules/statistics/statistics.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
