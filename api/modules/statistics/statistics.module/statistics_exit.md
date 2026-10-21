# statistics_exit()

- **Type:** Function
- **File:** [`modules/statistics/statistics.module`](_file.md), lines 50–93 · [local source](../../../../source/modules/statistics/statistics.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.module#L50-L93)
- **Module/theme:** statistics
- **Implements:** [hook_exit()](../../system/system.api.php/hook_exit.md)

## Signature

```php
function statistics_exit()
```

## Documentation

```text
Implements hook_exit().

Gathers statistics for page accesses.
```

## Code

```php
function statistics_exit() {
  global $user;

  // When serving cached pages with the 'page_cache_without_database'
  // configuration, system variables need to be loaded. This is a major
  // performance decrease for non-database page caches, but with Statistics
  // module, it is likely to also have 'statistics_enable_access_log' enabled,
  // in which case we need to bootstrap to the session phase anyway.
  drupal_bootstrap(DRUPAL_BOOTSTRAP_VARIABLES);

  if (variable_get('statistics_count_content_views', 0) && !variable_get('statistics_count_content_views_ajax', 0)) {
    // We are counting content views.
    if (arg(0) == 'node' && is_numeric(arg(1)) && arg(2) == NULL) {
      // A node has been viewed, so update the node's counters.
      db_merge('node_counter')
        ->key(array('nid' => arg(1)))
        ->fields(array(
          'daycount' => 1,
          'totalcount' => 1,
          'timestamp' => REQUEST_TIME,
        ))
        ->expression('daycount', 'daycount + 1')
        ->expression('totalcount', 'totalcount + 1')
        ->execute();
    }
  }
  if (variable_get('statistics_enable_access_log', 0)) {
    // For anonymous users unicode.inc will not have been loaded.
    include_once DRUPAL_ROOT . '/includes/unicode.inc';
    // Log this page access.
    db_insert('accesslog')
      ->fields(array(
        'title' => truncate_utf8(strip_tags(drupal_get_title()), 255),
        'path' => truncate_utf8($_GET['q'], 255),
        'url' => isset($_SERVER['HTTP_REFERER']) ? $_SERVER['HTTP_REFERER'] : '',
        'hostname' => ip_address(),
        'uid' => $user->uid,
        'sid' => session_id(),
        'timer' => (int) timer_read('page'),
        'timestamp' => REQUEST_TIME,
      ))
      ->execute();
  }
}
```

---
_Drupal 7.103 · [modules/statistics/statistics.module](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.module) · Licensed GPL-2.0-or-later (see LICENSE)._
