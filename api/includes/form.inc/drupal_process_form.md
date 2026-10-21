# drupal_process_form()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 867–990 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L867-L990)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function drupal_process_form($form_id, &$form, &$form_state)
```

## Documentation

```text
Processes a form submission.

This function is the heart of form API. The form gets built, validated and in
appropriate cases, submitted and rebuilt.

@param $form_id
  The unique string identifying the current form.
@param $form
  An associative array containing the structure of the form.
@param $form_state
  A keyed array containing the current state of the form. This
  includes the current persistent storage data for the form, and
  any data passed along by earlier steps when displaying a
  multi-step form. Additional information, like the sanitized $_POST
  data, is also accumulated here.
```

## Code

```php
function drupal_process_form($form_id, &$form, &$form_state) {
  $form_state['values'] = array();

  // With $_GET, these forms are always submitted if requested.
  if ($form_state['method'] == 'get' && !empty($form_state['always_process'])) {
    if (!isset($form_state['input']['form_build_id'])) {
      $form_state['input']['form_build_id'] = $form['#build_id'];
    }
    if (!isset($form_state['input']['form_id'])) {
      $form_state['input']['form_id'] = $form_id;
    }
    if (!isset($form_state['input']['form_token']) && isset($form['#token'])) {
      $form_state['input']['form_token'] = drupal_get_token($form['#token']);
    }
  }

  // form_builder() finishes building the form by calling element #process
  // functions and mapping user input, if any, to #value properties, and also
  // storing the values in $form_state['values']. We need to retain the
  // unprocessed $form in case it needs to be cached.
  $unprocessed_form = $form;
  $form = form_builder($form_id, $form, $form_state);

  // Only process the input if we have a correct form submission.
  if ($form_state['process_input']) {
    drupal_validate_form($form_id, $form, $form_state);

    // drupal_html_id() maintains a cache of element IDs it has seen,
    // so it can prevent duplicates. We want to be sure we reset that
    // cache when a form is processed, so scenarios that result in
    // the form being built behind the scenes and again for the
    // browser don't increment all the element IDs needlessly.
    if (!form_get_errors()) {
      // In case of errors, do not break HTML IDs of other forms.
      drupal_static_reset('drupal_html_id');
    }

    if ($form_state['submitted'] && !form_get_errors() && !$form_state['rebuild']) {
      // Execute form submit handlers.
      form_execute_handlers('submit', $form, $form_state);

      // We'll clear out the cached copies of the form and its stored data
      // here, as we've finished with them. The in-memory copies are still
      // here, though.
      if (!variable_get('cache', 0) && !empty($form_state['values']['form_build_id'])) {
        cache_clear_all('form_' . $form_state['values']['form_build_id'], 'cache_form');
        cache_clear_all('form_state_' . $form_state['values']['form_build_id'], 'cache_form');
      }

      // If batches were set in the submit handlers, we process them now,
      // possibly ending execution. We make sure we do not react to the batch
      // that is already being processed (if a batch operation performs a
      // drupal_form_submit).
      if ($batch =& batch_get() && !isset($batch['current_set'])) {
        // Store $form_state information in the batch definition.
        // We need the full $form_state when either:
        // - Some submit handlers were saved to be called during batch
        //   processing. See form_execute_handlers().
        // - The form is multistep.
        // In other cases, we only need the information expected by
        // drupal_redirect_form().
        if ($batch['has_form_submits'] || !empty($form_state['rebuild'])) {
          $batch['form_state'] = $form_state;
        }
        else {
          $batch['form_state'] = array_intersect_key($form_state, array_flip(array('programmed', 'rebuild', 'storage', 'no_redirect', 'redirect')));
        }

        $batch['progressive'] = !$form_state['programmed'];
        batch_process();

        // Execution continues only for programmatic forms.
        // For 'regular' forms, we get redirected to the batch processing
        // page. Form redirection will be handled in _batch_finished(),
        // after the batch is processed.
      }

      // Set a flag to indicate that the form has been processed and executed.
      $form_state['executed'] = TRUE;

      // Redirect the form based on values in $form_state.
      drupal_redirect_form($form_state);
    }

    // Don't rebuild or cache form submissions invoked via drupal_form_submit().
    if (!empty($form_state['programmed'])) {
      return;
    }

    // If $form_state['rebuild'] has been set and input has been processed
    // without validation errors, we are in a multi-step workflow that is not
    // yet complete. A new $form needs to be constructed based on the changes
    // made to $form_state during this request. Normally, a submit handler sets
    // $form_state['rebuild'] if a fully executed form requires another step.
    // However, for forms that have not been fully executed (e.g., Ajax
    // submissions triggered by non-buttons), there is no submit handler to set
    // $form_state['rebuild']. It would not make sense to redisplay the
    // identical form without an error for the user to correct, so we also
    // rebuild error-free non-executed forms, regardless of
    // $form_state['rebuild'].
    // @todo D8: Simplify this logic; considering Ajax and non-HTML front-ends,
    //   along with element-level #submit properties, it makes no sense to have
    //   divergent form execution based on whether the triggering element has
    //   #executes_submit_callback set to TRUE.
    if (($form_state['rebuild'] || !$form_state['executed']) && !form_get_errors()) {
      // Form building functions (e.g., _form_builder_handle_input_element())
      // may use $form_state['rebuild'] to determine if they are running in the
      // context of a rebuild, so ensure it is set.
      $form_state['rebuild'] = TRUE;
      $form = drupal_rebuild_form($form_id, $form_state, $form);
    }
  }

  // After processing the form, the form builder or a #process callback may
  // have set $form_state['cache'] to indicate that the form and form state
  // shall be cached. But the form may only be cached if the 'no_cache' property
  // is not set to TRUE. Only cache $form as it was prior to form_builder(),
  // because form_builder() must run for each request to accommodate new user
  // input. Rebuilt forms are not cached here, because drupal_rebuild_form()
  // already takes care of that.
  if (!$form_state['rebuild'] && $form_state['cache'] && empty($form_state['no_cache'])) {
    form_set_cache($form['#build_id'], $unprocessed_form, $form_state);
  }
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
