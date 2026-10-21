# Batch operations

- **Topic id:** `batch`
- **Defined in:** [`includes/form.inc`](../includes/form.inc/_file.md), line 4470 · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L4470)

## Documentation

```text
@defgroup batch Batch operations
@{
Creates and processes batch operations.

Functions allowing forms processing to be spread out over several page
requests, thus ensuring that the processing does not get interrupted
because of a PHP timeout, while allowing the user to receive feedback
on the progress of the ongoing operations.

The API is primarily designed to integrate nicely with the Form API
workflow, but can also be used by non-Form API scripts (like update.php)
or even simple page callbacks (which should probably be used sparingly).

Example:
@code
$batch = array(
  'title' => t('Exporting'),
  'operations' => array(
    array('my_function_1', array($account->uid, 'story')),
    array('my_function_2', array()),
  ),
  'finished' => 'my_finished_callback',
  'file' => 'path_to_file_containing_myfunctions',
);
batch_set($batch);
// Only needed if not inside a form _submit handler.
// Setting redirect in batch_process.
batch_process('node/1');
@endcode

Note: if the batch 'title', 'init_message', 'progress_message', or
'error_message' could contain any user input, it is the responsibility of
the code calling batch_set() to sanitize them first with a function like
check_plain() or filter_xss(). Furthermore, if the batch operation
returns any user input in the 'results' or 'message' keys of $context,
it must also sanitize them first.

Sample callback_batch_operation():
@code
// Simple and artificial: load a node of a given type for a given user
function my_function_1($uid, $type, &$context) {
  // The $context array gathers batch context information about the execution (read),
  // as well as 'return values' for the current operation (write)
  // The following keys are provided :
  // 'results' (read / write): The array of results gathered so far by
  //   the batch processing, for the current operation to append its own.
  // 'message' (write): A text message displayed in the progress page.
  // The following keys allow for multi-step operations :
  // 'sandbox' (read / write): An array that can be freely used to
  //   store persistent data between iterations. It is recommended to
  //   use this instead of $_SESSION, which is unsafe if the user
  //   continues browsing in a separate window while the batch is processing.
  // 'finished' (write): A float number between 0 and 1 informing
  //   the processing engine of the completion level for the operation.
  //   1 (or no value explicitly set) means the operation is finished
  //   and the batch processing can continue to the next operation.

  $node = node_load(array('uid' => $uid, 'type' => $type));
  $context['results'][] = $node->nid . ' : ' . check_plain($node->title);
  $context['message'] = check_plain($node->title);
}

// More advanced example: multi-step operation - load all nodes, five by five
function my_function_2(&$context) {
  if (empty($context['sandbox'])) {
    $context['sandbox']['progress'] = 0;
    $context['sandbox']['current_node'] = 0;
    $context['sandbox']['max'] = db_query('SELECT COUNT(DISTINCT nid) FROM {node}')->fetchField();
  }
  $limit = 5;
  $result = db_select('node')
    ->fields('node', array('nid'))
    ->condition('nid', $context['sandbox']['current_node'], '>')
    ->orderBy('nid')
    ->range(0, $limit)
    ->execute();
  foreach ($result as $row) {
    $node = node_load($row->nid, NULL, TRUE);
    $context['results'][] = $node->nid . ' : ' . check_plain($node->title);
    $context['sandbox']['progress']++;
    $context['sandbox']['current_node'] = $node->nid;
    $context['message'] = check_plain($node->title);
  }
  if ($context['sandbox']['progress'] != $context['sandbox']['max']) {
    $context['finished'] = $context['sandbox']['progress'] / $context['sandbox']['max'];
  }
}
@endcode

Sample callback_batch_finished():
@code
function my_finished_callback($success, $results, $operations) {
  // The 'success' parameter means no fatal PHP errors were detected. All
  // other error management should be handled using 'results'.
  if ($success) {
    $message = format_plural(count($results), 'One post processed.', '@count posts processed.');
  }
  else {
    $message = t('Finished with an error.');
  }
  drupal_set_message($message);
  // Providing data for the redirected page is done through $_SESSION.
  foreach ($results as $result) {
    $items[] = t('Loaded node %title.', array('%title' => $result));
  }
  $_SESSION['my_batch_results'] = $items;
}
@endcode
```

## Members (derived, 6)

From `@ingroup` tags and `@addtogroup`/`@defgroup` `@{ … @}` regions in the source.

- [_batch_populate_queue()](../includes/form.inc/_batch_populate_queue.md) (function) — Populates a job queue with the operations of a batch set.
- [_batch_queue()](../includes/form.inc/_batch_queue.md) (function) — Returns a queue object for a batch set.
- [batch_get()](../includes/form.inc/batch_get.md) (function) — Retrieves the current batch.
- [batch_process()](../includes/form.inc/batch_process.md) (function) — Processes the batch.
- [batch_set()](../includes/form.inc/batch_set.md) (function) — Adds a new batch.
- [hook_batch_alter()](../modules/system/system.api.php/hook_batch_alter.md) (function) — Alter batch information before a batch is processed.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
