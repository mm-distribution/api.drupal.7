# install_run_task()

- **Type:** Function
- **File:** [`includes/install.core.inc`](_file.md), lines 374–473 · [local source](../../../source/includes/install.core.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc#L374-L473)

## Signature

```php
function install_run_task($task, &$install_state)
```

## Documentation

```text
Runs an individual installation task.

@param $task
  An array of information about the task to be run as returned by
  hook_install_tasks().
@param $install_state
  An array of information about the current installation state. This is
  passed in by reference so that it can be modified by the task.

@return
  The output of the task function, if there is any.
```

## Code

```php
function install_run_task($task, &$install_state) {
  $function = $task['function'];

  if ($task['type'] == 'form') {
    require_once DRUPAL_ROOT . '/includes/form.inc';
    if ($install_state['interactive']) {
      // For interactive forms, build the form and ensure that it will not
      // redirect, since the installer handles its own redirection only after
      // marking the form submission task complete.
      $form_state = array(
        // We need to pass $install_state by reference in order for forms to
        // modify it, since the form API will use it in call_user_func_array(),
        // which requires that referenced variables be passed explicitly.
        'build_info' => array('args' => array(&$install_state)),
        'no_redirect' => TRUE,
      );
      $form = drupal_build_form($function, $form_state);
      // If a successful form submission did not occur, the form needs to be
      // rendered, which means the task is not complete yet.
      if (empty($form_state['executed'])) {
        $install_state['task_not_complete'] = TRUE;
        return drupal_render($form);
      }
      // Otherwise, return nothing so the next task will run in the same
      // request.
      return;
    }
    else {
      // For non-interactive forms, submit the form programmatically with the
      // values taken from the installation state. Throw an exception if any
      // errors were encountered.
      $form_state = array(
        'values' => !empty($install_state['forms'][$function]) ? $install_state['forms'][$function] : array(),
        // We need to pass $install_state by reference in order for forms to
        // modify it, since the form API will use it in call_user_func_array(),
        // which requires that referenced variables be passed explicitly.
        'build_info' => array('args' => array(&$install_state)),
      );
      drupal_form_submit($function, $form_state);
      $errors = form_get_errors();
      if (!empty($errors)) {
        throw new Exception(implode("\n", $errors));
      }
    }
  }

  elseif ($task['type'] == 'batch') {
    // Start a new batch based on the task function, if one is not running
    // already.
    $current_batch = variable_get('install_current_batch');
    if (!$install_state['interactive'] || !$current_batch) {
      $batch = $function($install_state);
      if (empty($batch)) {
        // If the task did some processing and decided no batch was necessary,
        // there is nothing more to do here.
        return;
      }
      batch_set($batch);
      // For interactive batches, we need to store the fact that this batch
      // task is currently running. Otherwise, we need to make sure the batch
      // will complete in one page request.
      if ($install_state['interactive']) {
        variable_set('install_current_batch', $function);
      }
      else {
        $batch =& batch_get();
        $batch['progressive'] = FALSE;
      }
      // Process the batch. For progressive batches, this will redirect.
      // Otherwise, the batch will complete.
      batch_process(install_redirect_url($install_state), install_full_redirect_url($install_state));
    }
    // If we are in the middle of processing this batch, keep sending back
    // any output from the batch process, until the task is complete.
    elseif ($current_batch == $function) {
      include_once DRUPAL_ROOT . '/includes/batch.inc';
      $output = _batch_page();
      // The task is complete when we try to access the batch page and receive
      // FALSE in return, since this means we are at a URL where we are no
      // longer requesting a batch ID.
      if ($output === FALSE) {
        // Return nothing so the next task will run in the same request.
        variable_del('install_current_batch');
        return;
      }
      else {
        // We need to force the page request to end if the task is not
        // complete, since the batch API sometimes prints JSON output
        // rather than returning a themed page.
        $install_state['task_not_complete'] = $install_state['stop_page_request'] = TRUE;
        return $output;
      }
    }
  }

  else {
    // For normal tasks, just return the function result, whatever it is.
    return $function($install_state);
  }
}
```

---
_Drupal 7.103 · [includes/install.core.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
