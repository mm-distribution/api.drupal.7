# drupal_rebuild_form()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 464–512 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L464-L512)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function drupal_rebuild_form($form_id, &$form_state, $old_form = NULL)
```

## Documentation

```text
Constructs a new $form from the information in $form_state.

This is the key function for making multi-step forms advance from step to
step. It is called by drupal_process_form() when all user input processing,
including calling validation and submission handlers, for the request is
finished. If a validate or submit handler set $form_state['rebuild'] to TRUE,
and if other conditions don't preempt a rebuild from happening, then this
function is called to generate a new $form, the next step in the form
workflow, to be returned for rendering.

Ajax form submissions are almost always multi-step workflows, so that is one
common use-case during which form rebuilding occurs. See ajax_form_callback()
for more information about creating Ajax-enabled forms.

@param $form_id
  The unique string identifying the desired form. If a function
  with that name exists, it is called to build the form array.
  Modules that need to generate the same form (or very similar forms)
  using different $form_ids can implement hook_forms(), which maps
  different $form_id values to the proper form constructor function. Examples
  may be found in node_forms() and search_forms().
@param $form_state
  A keyed array containing the current state of the form.
@param $old_form
  (optional) A previously built $form. Used to retain the #build_id and
  #action properties in Ajax callbacks and similar partial form rebuilds. The
  only properties copied from $old_form are the ones which both exist in
  $old_form and for which $form_state['rebuild_info']['copy'][PROPERTY] is
  TRUE. If $old_form is not passed, the entire $form is rebuilt freshly.
  'rebuild_info' needs to be a separate top-level property next to
  'build_info', since the contained data must not be cached.

@return
  The newly built form.

@see drupal_process_form()
@see ajax_form_callback()
```

## Code

```php
function drupal_rebuild_form($form_id, &$form_state, $old_form = NULL) {
  $form = drupal_retrieve_form($form_id, $form_state);

  // If only parts of the form will be returned to the browser (e.g., Ajax or
  // RIA clients), or if the form already had a new build ID regenerated when it
  // was retrieved from the form cache, reuse the existing #build_id.
  // Otherwise, a new #build_id is generated, to not clobber the previous
  // build's data in the form cache; also allowing the user to go back to an
  // earlier build, make changes, and re-submit.
  // @see drupal_prepare_form()
  $enforce_old_build_id = isset($old_form['#build_id']) && !empty($form_state['rebuild_info']['copy']['#build_id']);
  $old_form_is_mutable_copy = isset($old_form['#build_id_old']);
  if ($enforce_old_build_id || $old_form_is_mutable_copy) {
    $form['#build_id'] = $old_form['#build_id'];
    if ($old_form_is_mutable_copy) {
      $form['#build_id_old'] = $old_form['#build_id_old'];
    }
  }
  else {
    if (isset($old_form['#build_id'])) {
      $form['#build_id_old'] = $old_form['#build_id'];
    }
    $form['#build_id'] = 'form-' . drupal_random_key();
  }

  // #action defaults to request_uri(), but in case of Ajax and other partial
  // rebuilds, the form is submitted to an alternate URL, and the original
  // #action needs to be retained.
  if (isset($old_form['#action']) && !empty($form_state['rebuild_info']['copy']['#action'])) {
    $form['#action'] = $old_form['#action'];
  }

  drupal_prepare_form($form_id, $form, $form_state);

  // Caching is normally done in drupal_process_form(), but what needs to be
  // cached is the $form structure before it passes through form_builder(),
  // so we need to do it here.
  // @todo For Drupal 8, find a way to avoid this code duplication.
  if (empty($form_state['no_cache'])) {
    form_set_cache($form['#build_id'], $form, $form_state);
  }

  // Clear out all group associations as these might be different when
  // re-rendering the form.
  $form_state['groups'] = array();

  // Return a fully built form that is ready for rendering.
  return form_builder($form_id, $form, $form_state);
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
