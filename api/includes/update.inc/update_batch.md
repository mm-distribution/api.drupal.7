# update_batch()

- **Type:** Function
- **File:** [`includes/update.inc`](_file.md), lines 1042–1088 · [local source](../../../source/includes/update.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/update.inc#L1042-L1088)

## Signature

```php
function update_batch($start, $redirect = NULL, $url = NULL, $batch = array(), $redirect_callback = 'drupal_goto')
```

## Documentation

```text
Starts the database update batch process.

@param $start
  An array whose keys contain the names of modules to be updated during the
  current batch process, and whose values contain the number of the first
  requested update for that module. The actual updates that are run (and the
  order they are run in) will depend on the results of passing this data
  through the update dependency system.
@param $redirect
  Path to redirect to when the batch has finished processing.
@param $url
  URL of the batch processing page (should only be used for separate
  scripts like update.php).
@param $batch
  Optional parameters to pass into the batch API.
@param $redirect_callback
  (optional) Specify a function to be called to redirect to the progressive
  processing page.

@see update_resolve_dependencies()
```

## Code

```php
function update_batch($start, $redirect = NULL, $url = NULL, $batch = array(), $redirect_callback = 'drupal_goto') {
  // During the update, bring the site offline so that schema changes do not
  // affect visiting users.
  $_SESSION['maintenance_mode'] = variable_get('maintenance_mode', FALSE);
  if ($_SESSION['maintenance_mode'] == FALSE) {
    variable_set('maintenance_mode', TRUE);
  }

  // Resolve any update dependencies to determine the actual updates that will
  // be run and the order they will be run in.
  $updates = update_resolve_dependencies($start);

  // Store the dependencies for each update function in an array which the
  // batch API can pass in to the batch operation each time it is called. (We
  // do not store the entire update dependency array here because it is
  // potentially very large.)
  $dependency_map = array();
  foreach ($updates as $function => $update) {
    $dependency_map[$function] = !empty($update['reverse_paths']) ? array_keys($update['reverse_paths']) : array();
  }

  $operations = array();
  foreach ($updates as $update) {
    if ($update['allowed']) {
      // Set the installed version of each module so updates will start at the
      // correct place. (The updates are already sorted, so we can simply base
      // this on the first one we come across in the above foreach loop.)
      if (isset($start[$update['module']])) {
        drupal_set_installed_schema_version($update['module'], $update['number'] - 1);
        unset($start[$update['module']]);
      }
      // Add this update function to the batch.
      $function = $update['module'] . '_update_' . $update['number'];
      $operations[] = array('update_do_one', array($update['module'], $update['number'], $dependency_map[$function]));
    }
  }
  $batch['operations'] = $operations;
  $batch += array(
    'title' => 'Updating',
    'init_message' => 'Starting updates',
    'error_message' => 'An unrecoverable error has occurred. You can find the error message below. It is advised to copy it to the clipboard for reference.',
    'finished' => 'update_finished',
    'file' => 'includes/update.inc',
  );
  batch_set($batch);
  batch_process($redirect, $url, $redirect_callback);
}
```

---
_Drupal 7.103 · [includes/update.inc](https://github.com/drupal/drupal/blob/7.103/includes/update.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
