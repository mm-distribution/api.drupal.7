# _batch_process()

- **Type:** Function
- **File:** [`includes/batch.inc`](_file.md), lines 200–329 · [local source](../../../source/includes/batch.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/batch.inc#L200-L329)

## Signature

```php
function _batch_process()
```

## Documentation

```text
Processes sets in a batch.

If the batch was marked for progressive execution (default), this executes as
many operations in batch sets until an execution time of 1 second has been
exceeded. It will continue with the next operation of the same batch set in
the next request.

@return
  An array containing a completion value (in percent) and a status message.
```

## Code

```php
function _batch_process() {
  $batch       = &batch_get();
  $current_set = &_batch_current_set();
  // Indicate that this batch set needs to be initialized.
  $set_changed = TRUE;

  // If this batch was marked for progressive execution (e.g. forms submitted by
  // drupal_form_submit()), initialize a timer to determine whether we need to
  // proceed with the same batch phase when a processing time of 1 second has
  // been exceeded.
  if ($batch['progressive']) {
    timer_start('batch_processing');
  }

  if (empty($current_set['start'])) {
    $current_set['start'] = microtime(TRUE);
  }

  $queue = _batch_queue($current_set);

  while (!$current_set['success']) {
    // If this is the first time we iterate this batch set in the current
    // request, we check if it requires an additional file for functions
    // definitions.
    if ($set_changed && isset($current_set['file']) && is_file($current_set['file'])) {
      include_once DRUPAL_ROOT . '/' . $current_set['file'];
    }

    $task_message = '';
    // Assume a single pass operation and set the completion level to 1 by
    // default.
    $finished = 1;

    if ($item = $queue->claimItem()) {
      list($function, $args) = $item->data;

      // Build the 'context' array and execute the function call.
      $batch_context = array(
        'sandbox'  => &$current_set['sandbox'],
        'results'  => &$current_set['results'],
        'finished' => &$finished,
        'message'  => &$task_message,
      );
      call_user_func_array($function, array_merge($args, array(&$batch_context)));

      if ($finished >= 1) {
        // Make sure this step is not counted twice when computing $current.
        $finished = 0;
        // Remove the processed operation and clear the sandbox.
        $queue->deleteItem($item);
        $current_set['count']--;
        $current_set['sandbox'] = array();
      }
    }

    // When all operations in the current batch set are completed, browse
    // through the remaining sets, marking them 'successfully processed'
    // along the way, until we find a set that contains operations.
    // _batch_next_set() executes form submit handlers stored in 'control'
    // sets (see form_execute_handlers()), which can in turn add new sets to
    // the batch.
    $set_changed = FALSE;
    $old_set = $current_set;
    while (empty($current_set['count']) && ($current_set['success'] = TRUE) && _batch_next_set()) {
      $current_set = &_batch_current_set();
      $current_set['start'] = microtime(TRUE);
      $set_changed = TRUE;
    }

    // At this point, either $current_set contains operations that need to be
    // processed or all sets have been completed.
    $queue = _batch_queue($current_set);

    // If we are in progressive mode, break processing after 1 second.
    if ($batch['progressive'] && timer_read('batch_processing') > 1000) {
      // Record elapsed wall clock time.
      $current_set['elapsed'] = round((microtime(TRUE) - $current_set['start']) * 1000, 2);
      break;
    }
  }

  if ($batch['progressive']) {
    // Gather progress information.

    // Reporting 100% progress will cause the whole batch to be considered
    // processed. If processing was paused right after moving to a new set,
    // we have to use the info from the new (unprocessed) set.
    if ($set_changed && isset($current_set['queue'])) {
      // Processing will continue with a fresh batch set.
      $remaining        = $current_set['count'];
      $total            = $current_set['total'];
      $progress_message = $current_set['init_message'];
      $task_message     = '';
    }
    else {
      // Processing will continue with the current batch set.
      $remaining        = $old_set['count'];
      $total            = $old_set['total'];
      $progress_message = $old_set['progress_message'];
    }

    // Total progress is the number of operations that have fully run plus the
    // completion level of the current operation.
    $current    = $total - $remaining + $finished;
    $percentage = _batch_api_percentage($total, $current);
    $elapsed    = isset($current_set['elapsed']) ? $current_set['elapsed'] : 0;
    $values     = array(
      '@remaining'  => $remaining,
      '@total'      => $total,
      '@current'    => floor($current),
      '@percentage' => $percentage,
      '@elapsed'    => format_interval($elapsed / 1000),
      // If possible, estimate remaining processing time.
      '@estimate'   => ($current > 0) ? format_interval(($elapsed * ($total - $current) / $current) / 1000) : '-',
    );
    $message = strtr($progress_message, $values);
    if (!empty($message)) {
      $message .= '<br />';
    }
    if (!empty($task_message)) {
      $message .= $task_message;
    }

    return array($percentage, $message);
  }
  else {
    // If we are not in progressive mode, the entire batch has been processed.
    return _batch_finished();
  }
}
```

---
_Drupal 7.103 · [includes/batch.inc](https://github.com/drupal/drupal/blob/7.103/includes/batch.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
