# _batch_finished()

- **Type:** Function
- **File:** [`includes/batch.inc`](_file.md), lines 412–482 · [local source](../../../source/includes/batch.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/batch.inc#L412-L482)

## Signature

```php
function _batch_finished()
```

## Documentation

```text
Ends the batch processing.

Call the 'finished' callback of each batch set to allow custom handling of
the results and resolve page redirection.
```

## Code

```php
function _batch_finished() {
  $batch = &batch_get();

  // Execute the 'finished' callbacks for each batch set, if defined.
  foreach ($batch['sets'] as $batch_set) {
    if (isset($batch_set['finished'])) {
      // Check if the set requires an additional file for function definitions.
      if (isset($batch_set['file']) && is_file($batch_set['file'])) {
        include_once DRUPAL_ROOT . '/' . $batch_set['file'];
      }
      if (is_callable($batch_set['finished'])) {
        $queue = _batch_queue($batch_set);
        $operations = $queue->getAllItems();
        call_user_func($batch_set['finished'], $batch_set['success'], $batch_set['results'], $operations, format_interval($batch_set['elapsed'] / 1000));
      }
    }
  }

  // Clean up the batch table and unset the static $batch variable.
  if ($batch['progressive']) {
    db_delete('batch')
      ->condition('bid', $batch['id'])
      ->execute();
    foreach ($batch['sets'] as $batch_set) {
      if ($queue = _batch_queue($batch_set)) {
        $queue->deleteQueue();
      }
    }
    // Clean-up the session. Not needed for CLI updates.
    if (isset($_SESSION)) {
      unset($_SESSION['batches'][$batch['id']]);
      if (empty($_SESSION['batches'])) {
        unset($_SESSION['batches']);
      }
    }
  }
  $_batch = $batch;
  $batch = NULL;

  // Redirect if needed.
  if ($_batch['progressive']) {
    // Revert the 'destination' that was saved in batch_process().
    if (isset($_batch['destination'])) {
      $_GET['destination'] = $_batch['destination'];
    }

    // Determine the target path to redirect to.
    if (!isset($_batch['form_state']['redirect'])) {
      if (isset($_batch['redirect'])) {
        $_batch['form_state']['redirect'] = $_batch['redirect'];
      }
      else {
        $_batch['form_state']['redirect'] = $_batch['source_url'];
      }
    }

    // Use drupal_redirect_form() to handle the redirection logic.
    drupal_redirect_form($_batch['form_state']);

    // If no redirection happened, redirect to the originating page. In case the
    // form needs to be rebuilt, save the final $form_state for
    // drupal_build_form().
    if (!empty($_batch['form_state']['rebuild'])) {
      $_SESSION['batch_form_state'] = $_batch['form_state'];
    }
    $function = $_batch['redirect_callback'];
    if (function_exists($function)) {
      $function($_batch['source_url'], array('query' => array('op' => 'finish', 'id' => $_batch['id'])));
    }
  }
}
```

---
_Drupal 7.103 · [includes/batch.inc](https://github.com/drupal/drupal/blob/7.103/includes/batch.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
