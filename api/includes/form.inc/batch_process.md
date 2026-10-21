# batch_process()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 4708–4782 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L4708-L4782)
- **Topics:** [batch](../../topics/batch.md)

## Signature

```php
function batch_process($redirect = NULL, $url = 'batch', $redirect_callback = 'drupal_goto')
```

## Documentation

```text
Processes the batch.

Unless the batch has been marked with 'progressive' = FALSE, the function
issues a drupal_goto and thus ends page execution.

This function is generally not needed in form submit handlers;
Form API takes care of batches that were set during form submission.

@param $redirect
  (optional) Path to redirect to when the batch has finished processing.
@param $url
  (optional - should only be used for separate scripts like update.php)
  URL of the batch processing page.
@param $redirect_callback
  (optional) Specify a function to be called to redirect to the progressive
  processing page. By default drupal_goto() will be used to redirect to a
  page which will do the progressive page. Specifying another function will
  allow the progressive processing to be processed differently.
```

## Code

```php
function batch_process($redirect = NULL, $url = 'batch', $redirect_callback = 'drupal_goto') {
  $batch =& batch_get();

  drupal_theme_initialize();

  if (isset($batch)) {
    // Add process information
    $process_info = array(
      'current_set' => 0,
      'progressive' => TRUE,
      'url' => $url,
      'url_options' => array(),
      'source_url' => $_GET['q'],
      'redirect' => $redirect,
      'theme' => $GLOBALS['theme_key'],
      'redirect_callback' => $redirect_callback,
    );
    $batch += $process_info;

    // The batch is now completely built. Allow other modules to make changes
    // to the batch so that it is easier to reuse batch processes in other
    // environments.
    drupal_alter('batch', $batch);

    // Assign an arbitrary id: don't rely on a serial column in the 'batch'
    // table, since non-progressive batches skip database storage completely.
    $batch['id'] = db_next_id();

    // Move operations to a job queue. Non-progressive batches will use a
    // memory-based queue.
    foreach ($batch['sets'] as $key => $batch_set) {
      _batch_populate_queue($batch, $key);
    }

    // Initiate processing.
    if ($batch['progressive']) {
      // Now that we have a batch id, we can generate the redirection link in
      // the generic error message.
      $t = get_t();
      $batch['error_message'] = $t('Please continue to <a href="@error_url">the error page</a>', array('@error_url' => url($url, array('query' => array('id' => $batch['id'], 'op' => 'finished')))));

      // Clear the way for the drupal_goto() redirection to the batch processing
      // page, by saving and unsetting the 'destination', if there is any.
      if (isset($_GET['destination'])) {
        $batch['destination'] = $_GET['destination'];
        unset($_GET['destination']);
      }

      // Store the batch.
      db_insert('batch')
        ->fields(array(
          'bid' => $batch['id'],
          'timestamp' => REQUEST_TIME,
          'token' => drupal_get_token($batch['id']),
          'batch' => serialize($batch),
        ))
        ->execute();

      // Set the batch number in the session to guarantee that it will stay alive.
      $_SESSION['batches'][$batch['id']] = TRUE;

      // Redirect for processing.
      $function = $batch['redirect_callback'];
      if (function_exists($function)) {
        $function($batch['url'], array('query' => array('op' => 'start', 'id' => $batch['id'])));
      }
    }
    else {
      // Non-progressive execution: bypass the whole progressbar workflow
      // and execute the batch in one pass.
      require_once DRUPAL_ROOT . '/includes/batch.inc';
      _batch_process();
    }
  }
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
