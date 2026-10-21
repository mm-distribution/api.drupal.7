# form_execute_handlers()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 1505–1536 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L1505-L1536)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function form_execute_handlers($type, &$form, &$form_state)
```

## Documentation

```text
Executes custom validation and submission handlers for a given form.

Button-specific handlers are checked first. If none exist, the function
falls back to form-level handlers.

@param $type
  The type of handler to execute. 'validate' or 'submit' are the
  defaults used by Form API.
@param $form
  An associative array containing the structure of the form.
@param $form_state
  A keyed array containing the current state of the form. If the user
  submitted the form by clicking a button with custom handler functions
  defined, those handlers will be stored here.
```

## Code

```php
function form_execute_handlers($type, &$form, &$form_state) {
  $return = FALSE;
  // If there was a button pressed, use its handlers.
  if (isset($form_state[$type . '_handlers'])) {
    $handlers = $form_state[$type . '_handlers'];
  }
  // Otherwise, check for a form-level handler.
  elseif (isset($form['#' . $type])) {
    $handlers = $form['#' . $type];
  }
  else {
    $handlers = array();
  }

  foreach ($handlers as $function) {
    // Check if a previous _submit handler has set a batch, but make sure we
    // do not react to a batch that is already being processed (for instance
    // if a batch operation performs a drupal_form_submit()).
    if ($type == 'submit' && ($batch =& batch_get()) && !isset($batch['id'])) {
      // Some previous submit handler has set a batch. To ensure correct
      // execution order, store the call in a special 'control' batch set.
      // See _batch_next_set().
      $batch['sets'][] = array('form_submit' => $function);
      $batch['has_form_submits'] = TRUE;
    }
    else {
      $function($form, $form_state);
    }
    $return = TRUE;
  }
  return $return;
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
