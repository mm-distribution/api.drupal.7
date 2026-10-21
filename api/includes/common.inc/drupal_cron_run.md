# drupal_cron_run()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 5517–5631 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L5517-L5631)

## Signature

```php
function drupal_cron_run()
```

## Documentation

```text
Executes a cron run when called.

Do not call this function from a test. Use $this->cronRun() instead.

@return bool
  TRUE if cron ran successfully and FALSE if cron is already running.
```

## Code

```php
function drupal_cron_run() {
  // Allow execution to continue even if the request gets canceled.
  @ignore_user_abort(TRUE);

  // Prevent session information from being saved while cron is running.
  $original_session_saving = drupal_save_session();
  drupal_save_session(FALSE);

  // Force the current user to anonymous to ensure consistent permissions on
  // cron runs.
  $original_user = $GLOBALS['user'];
  $GLOBALS['user'] = drupal_anonymous_user();

  // Try to allocate enough time to run all the hook_cron implementations.
  drupal_set_time_limit(240);

  $return = FALSE;
  // Grab the defined cron queues.
  $queues = module_invoke_all('cron_queue_info');
  drupal_alter('cron_queue_info', $queues);

  // Try to acquire cron lock.
  $cron_lock_expiration_timeout = variable_get('cron_lock_expiration_timeout', 900.0);
  if (!lock_acquire('cron', $cron_lock_expiration_timeout)) {
    // Cron is still running normally.
    watchdog('cron', 'Attempting to re-run cron while it is already running.', array(), WATCHDOG_WARNING);
  }
  else {
    // Make sure every queue exists. There is no harm in trying to recreate an
    // existing queue.
    foreach ($queues as $queue_name => $info) {
      DrupalQueue::get($queue_name)->createQueue();
    }

    $module_previous = '';

    // If detailed logging isn't enabled, don't log individual execution times.
    $time_logging_enabled = variable_get('cron_detailed_logging', DRUPAL_CRON_DETAILED_LOGGING);

    // Iterate through the modules calling their cron handlers (if any):
    foreach (module_implements('cron') as $module) {
      if ($time_logging_enabled) {
        if (!$module_previous) {
          watchdog('cron', 'Starting execution of @module_cron().', array('@module' => $module));
        }
        else {
          watchdog('cron', 'Starting execution of @module_cron(), execution of @module_previous_cron() took @time.', array(
            '@module' => $module,
            '@module_previous' => $module_previous,
            '@time' => timer_read('cron_' . $module_previous) . 'ms',
          ));
        }
        timer_start('cron_' . $module);
      }

      // Do not let an exception thrown by one module disturb another.
      try {
        module_invoke($module, 'cron');
      }
      catch (Exception $e) {
        watchdog_exception('cron', $e);
      }

      if ($time_logging_enabled) {
        timer_stop('cron_' . $module);
        $module_previous = $module;
      }
    }

    if ($time_logging_enabled) {
      if ($module_previous) {
        watchdog('cron', 'Execution of @module_previous_cron() took @time.', array(
          '@module_previous' => $module_previous,
          '@time' => timer_read('cron_' . $module_previous) . 'ms',
        ));
      }
    }

    // Record cron time.
    variable_set('cron_last', REQUEST_TIME);
    watchdog('cron', 'Cron run completed.', array(), WATCHDOG_NOTICE);

    // Release cron lock.
    lock_release('cron');

    // Return TRUE so other functions can check if it did run successfully
    $return = TRUE;
  }

  foreach ($queues as $queue_name => $info) {
    if (!empty($info['skip on cron'])) {
      // Do not run if queue wants to skip.
      continue;
    }
    $callback = $info['worker callback'];
    $end = time() + (isset($info['time']) ? $info['time'] : 15);
    $queue = DrupalQueue::get($queue_name);
    while (time() < $end && ($item = $queue->claimItem())) {
      try {
        call_user_func($callback, $item->data);
        $queue->deleteItem($item);
      }
      catch (Exception $e) {
        // In case of exception log it and leave the item in the queue
        // to be processed again later.
        watchdog_exception('cron', $e);
      }
    }
  }
  // Restore the user.
  $GLOBALS['user'] = $original_user;
  drupal_save_session($original_session_saving);

  return $return;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
