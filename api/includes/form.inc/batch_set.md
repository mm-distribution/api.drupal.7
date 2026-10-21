# batch_set()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 4630–4686 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L4630-L4686)
- **Topics:** [batch](../../topics/batch.md)

## Signature

```php
function batch_set($batch_definition)
```

## Documentation

```text
Adds a new batch.

Batch operations are added as new batch sets. Batch sets are used to spread
processing (primarily, but not exclusively, forms processing) over several
page requests. This helps to ensure that the processing is not interrupted
due to PHP timeouts, while users are still able to receive feedback on the
progress of the ongoing operations. Combining related operations into
distinct batch sets provides clean code independence for each batch set,
ensuring that two or more batches, submitted independently, can be processed
without mutual interference. Each batch set may specify its own set of
operations and results, produce its own UI messages, and trigger its own
'finished' callback. Batch sets are processed sequentially, with the progress
bar starting afresh for each new set.

@param $batch_definition
  An associative array defining the batch, with the following elements (all
  are optional except as noted):
  - operations: (required) Array of operations to be performed, where each
    item is an array consisting of the name of an implementation of
    callback_batch_operation() and an array of parameter.
    Example:
    @code
    array(
      array('callback_batch_operation_1', array($arg1)),
      array('callback_batch_operation_2', array($arg2_1, $arg2_2)),
    )
    @endcode
  - title: A safe, translated string to use as the title for the progress
    page. Defaults to t('Processing').
  - init_message: Message displayed while the processing is initialized.
    Defaults to t('Initializing.').
  - progress_message: Message displayed while processing the batch. Available
    placeholders are @current, @remaining, @total, @percentage, @estimate and
    @elapsed. Defaults to t('Completed @current of @total.').
  - error_message: Message displayed if an error occurred while processing
    the batch. Defaults to t('An error has occurred.').
  - finished: Name of an implementation of callback_batch_finished(). This is
    executed after the batch has completed. This should be used to perform
    any result massaging that may be needed, and possibly save data in
    $_SESSION for display after final page redirection.
  - file: Path to the file containing the definitions of the 'operations' and
    'finished' functions, for instance if they don't reside in the main
    .module file. The path should be relative to base_path(), and thus should
    be built using drupal_get_path().
  - css: Array of paths to CSS files to be used on the progress page.
  - url_options: options passed to url() when constructing redirect URLs for
    the batch.
```

## Code

```php
function batch_set($batch_definition) {
  if ($batch_definition) {
    $batch =& batch_get();

    // Initialize the batch if needed.
    if (empty($batch)) {
      $batch = array(
        'sets' => array(),
        'has_form_submits' => FALSE,
      );
    }

    // Base and default properties for the batch set.
    // Use get_t() to allow batches during installation.
    $t = get_t();
    $init = array(
      'sandbox' => array(),
      'results' => array(),
      'success' => FALSE,
      'start' => 0,
      'elapsed' => 0,
    );
    $defaults = array(
      'title' => $t('Processing'),
      'init_message' => $t('Initializing.'),
      'progress_message' => $t('Completed @current of @total.'),
      'error_message' => $t('An error has occurred.'),
      'css' => array(),
    );
    $batch_set = $init + $batch_definition + $defaults;

    // Tweak init_message to avoid the bottom of the page flickering down after
    // init phase.
    $batch_set['init_message'] .= '<br/>&nbsp;';

    // The non-concurrent workflow of batch execution allows us to save
    // numberOfItems() queries by handling our own counter.
    $batch_set['total'] = count($batch_set['operations']);
    $batch_set['count'] = $batch_set['total'];

    // Add the set to the batch.
    if (empty($batch['id'])) {
      // The batch is not running yet. Simply add the new set.
      $batch['sets'][] = $batch_set;
    }
    else {
      // The set is being added while the batch is running. Insert the new set
      // right after the current one to ensure execution order, and store its
      // operations in a queue.
      $index = $batch['current_set'] + 1;
      $slice1 = array_slice($batch['sets'], 0, $index);
      $slice2 = array_slice($batch['sets'], $index);
      $batch['sets'] = array_merge($slice1, array($batch_set), $slice2);
      _batch_populate_queue($batch, $index);
    }
  }
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
