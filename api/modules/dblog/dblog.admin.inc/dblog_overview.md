# dblog_overview()

- **Type:** Function
- **File:** [`modules/dblog/dblog.admin.inc`](_file.md), lines 21–86 · [local source](../../../../source/modules/dblog/dblog.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.admin.inc#L21-L86)
- **Module/theme:** dblog
- **Topics:** [logging_severity_levels](../../../topics/logging_severity_levels.md)

## Signature

```php
function dblog_overview()
```

## Documentation

```text
Page callback: Displays a listing of database log messages.

Messages are truncated at 56 chars. Full-length messages can be viewed on the
message details page.

@see dblog_clear_log_form()
@see dblog_event()
@see dblog_filter_form()
@see dblog_menu()

@ingroup logging_severity_levels
```

## Code

```php
function dblog_overview() {
  $filter = dblog_build_filter_query();
  $rows = array();
  $classes = array(
    WATCHDOG_DEBUG     => 'dblog-debug',
    WATCHDOG_INFO      => 'dblog-info',
    WATCHDOG_NOTICE    => 'dblog-notice',
    WATCHDOG_WARNING   => 'dblog-warning',
    WATCHDOG_ERROR     => 'dblog-error',
    WATCHDOG_CRITICAL  => 'dblog-critical',
    WATCHDOG_ALERT     => 'dblog-alert',
    WATCHDOG_EMERGENCY => 'dblog-emerg',
  );

  $build['dblog_filter_form'] = drupal_get_form('dblog_filter_form');
  $build['dblog_clear_log_form'] = drupal_get_form('dblog_clear_log_form');

  $header = array(
    '', // Icon column.
    array('data' => t('Type'), 'field' => 'w.type'),
    array('data' => t('Date'), 'field' => 'w.wid', 'sort' => 'desc'),
    t('Message'),
    array('data' => t('User'), 'field' => 'u.name'),
    array('data' => t('Operations')),
  );

  $query = db_select('watchdog', 'w')->extend('PagerDefault')->extend('TableSort');
  $query->leftJoin('users', 'u', 'w.uid = u.uid');
  $query
    ->fields('w', array('wid', 'uid', 'severity', 'type', 'timestamp', 'message', 'variables', 'link'))
    ->addField('u', 'name');
  if (!empty($filter['where'])) {
    $query->where($filter['where'], $filter['args']);
  }
  $result = $query
    ->limit(50)
    ->orderByHeader($header)
    ->execute();

  foreach ($result as $dblog) {
    $rows[] = array('data' =>
      array(
        // Cells
        array('class' => 'icon'),
        t($dblog->type),
        format_date($dblog->timestamp, 'short'),
        theme('dblog_message', array('event' => $dblog, 'link' => TRUE)),
        theme('username', array('account' => $dblog)),
        filter_xss($dblog->link),
      ),
      // Attributes for tr
      'class' => array(drupal_html_class('dblog-' . $dblog->type), $classes[$dblog->severity]),
    );
  }

  $build['dblog_table'] = array(
    '#theme' => 'table',
    '#header' => $header,
    '#rows' => $rows,
    '#attributes' => array('id' => 'admin-dblog'),
    '#empty' => t('No log messages available.'),
  );
  $build['dblog_pager'] = array('#theme' => 'pager');

  return $build;
}
```

---
_Drupal 7.103 · [modules/dblog/dblog.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
