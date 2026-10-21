# hook_cron()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 575–594 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L575-L594)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_cron()
```

## Documentation

```text
Perform periodic actions.

Modules that require some commands to be executed periodically can
implement hook_cron(). The engine will then call the hook whenever a cron
run happens, as defined by the administrator. Typical tasks managed by
hook_cron() are database maintenance, backups, recalculation of settings
or parameters, automated mailing, and retrieving remote data.

Short-running or non-resource-intensive tasks can be executed directly in
the hook_cron() implementation.

Long-running tasks and tasks that could time out, such as retrieving remote
data, sending email, and intensive file tasks, should use the queue API
instead of executing the tasks directly. To do this, first define one or
more queues via hook_cron_queue_info(). Then, add items that need to be
processed to the defined queues.
```

## Code

```php
function hook_cron() {
  // Short-running operation example, not using a queue:
  // Delete all expired records since the last cron run.
  $expires = variable_get('mymodule_cron_last_run', REQUEST_TIME);
  db_delete('mymodule_table')
    ->condition('expires', $expires, '>=')
    ->execute();
  variable_set('mymodule_cron_last_run', REQUEST_TIME);

  // Long-running operation example, leveraging a queue:
  // Fetch feeds from other sites.
  $result = db_query('SELECT * FROM {aggregator_feed} WHERE checked + refresh < :time AND refresh <> :never', array(
    ':time' => REQUEST_TIME,
    ':never' => AGGREGATOR_CLEAR_NEVER,
  ));
  $queue = DrupalQueue::get('aggregator_feeds');
  foreach ($result as $feed) {
    $queue->createItem($feed);
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_cron()".

- [aggregator_cron()](../../aggregator/aggregator.module/aggregator_cron.md) — `modules/aggregator/aggregator.module`
- [announcements_feed_cron()](../../announcements_feed/announcements_feed.module/announcements_feed_cron.md) — `modules/announcements_feed/announcements_feed.module`
- [common_test_cron()](../../simpletest/tests/common_test.module/common_test_cron.md) — `modules/simpletest/tests/common_test.module`
- [common_test_cron_helper_cron()](../../simpletest/tests/common_test_cron_helper.module/common_test_cron_helper_cron.md) — `modules/simpletest/tests/common_test_cron_helper.module`
- [dblog_cron()](../../dblog/dblog.module/dblog_cron.md) — `modules/dblog/dblog.module`
- [field_cron()](../../field/field.module/field_cron.md) — `modules/field/field.module`
- [node_cron()](../../node/node.module/node_cron.md) — `modules/node/node.module`
- [openid_cron()](../../openid/openid.module/openid_cron.md) — `modules/openid/openid.module`
- [poll_cron()](../../poll/poll.module/poll_cron.md) — `modules/poll/poll.module`
- [search_cron()](../../search/search.module/search_cron.md) — `modules/search/search.module`
- [statistics_cron()](../../statistics/statistics.module/statistics_cron.md) — `modules/statistics/statistics.module`
- [system_cron()](../system.module/system_cron.md) — `modules/system/system.module`
- [tracker_cron()](../../tracker/tracker.module/tracker_cron.md) — `modules/tracker/tracker.module`
- [trigger_cron()](../../trigger/trigger.module/trigger_cron.md) — `modules/trigger/trigger.module`
- [update_cron()](../../update/update.module/update_cron.md) — `modules/update/update.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
