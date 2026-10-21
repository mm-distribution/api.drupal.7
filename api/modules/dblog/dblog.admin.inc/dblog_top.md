# dblog_top()

- **Type:** Function
- **File:** [`modules/dblog/dblog.admin.inc`](_file.md), lines 102–138 · [local source](../../../../source/modules/dblog/dblog.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.admin.inc#L102-L138)
- **Module/theme:** dblog

## Signature

```php
function dblog_top($type)
```

## Documentation

```text
Page callback: Shows the most frequent log messages of a given event type.

Messages are not truncated on this page because events detailed herein do not
have links to a detailed view.

@param string $type
  Type of database log events to display (e.g., 'search').

@return array
  A build array in the format expected by drupal_render().

@see dblog_menu()
```

## Code

```php
function dblog_top($type) {

  $header = array(
    array('data' => t('Count'), 'field' => 'count', 'sort' => 'desc'),
    array('data' => t('Message'), 'field' => 'message')
  );
  $count_query = db_select('watchdog');
  $count_query->addExpression('COUNT(DISTINCT(message))');
  $count_query->condition('type', $type);

  $query = db_select('watchdog', 'w')->extend('PagerDefault')->extend('TableSort');
  $query->addExpression('COUNT(wid)', 'count');
  $query = $query
    ->fields('w', array('message', 'variables'))
    ->condition('w.type', $type)
    ->groupBy('message')
    ->groupBy('variables')
    ->limit(30)
    ->orderByHeader($header);
  $query->setCountQuery($count_query);
  $result = $query->execute();

  $rows = array();
  foreach ($result as $dblog) {
    $rows[] = array($dblog->count, theme('dblog_message', array('event' => $dblog)));
  }

  $build['dblog_top_table']  = array(
    '#theme' => 'table',
    '#header' => $header,
    '#rows' => $rows,
    '#empty' => t('No log messages available.'),
  );
  $build['dblog_top_pager'] = array('#theme' => 'pager');

  return $build;
}
```

---
_Drupal 7.103 · [modules/dblog/dblog.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
