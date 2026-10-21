# drupal_build_form()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 314–397 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L314-L397)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function drupal_build_form($form_id, &$form_state)
```

## Documentation

```text
Builds and process a form based on a form id.

The form may also be retrieved from the cache if the form was built in a
previous page-load. The form is then passed on for processing, validation
and submission if there is proper input.

@param $form_id
  The unique string identifying the desired form. If a function with that
  name exists, it is called to build the form array. Modules that need to
  generate the same form (or very similar forms) using different $form_ids
  can implement hook_forms(), which maps different $form_id values to the
  proper form constructor function. Examples may be found in node_forms(),
  and search_forms().
@param $form_state
  An array which stores information about the form. This is passed as a
  reference so that the caller can use it to examine what in the form changed
  when the form submission process is complete. Furthermore, it may be used
  to store information related to the processed data in the form, which will
  persist across page requests when the 'cache' or 'rebuild' flag is set.
  The following parameters may be set in $form_state to affect how the form
  is rendered:
  - build_info: Internal. An associative array of information stored by Form
    API that is necessary to build and rebuild the form from cache when the
    original context may no longer be available:
    - args: A list of arguments to pass to the form constructor.
    - files: An optional array defining include files that need to be loaded
      for building the form. Each array entry may be the path to a file or
      another array containing values for the parameters 'type', 'module' and
      'name' as needed by module_load_include(). The files listed here are
      automatically loaded by form_get_cache(). By default the current menu
      router item's 'file' definition is added, if any. Use
      form_load_include() to add include files from a form constructor.
    - form_id: Identification of the primary form being constructed and
      processed.
    - base_form_id: Identification for a base form, as declared in a
      hook_forms() implementation.
    - immutable: If this flag is set to TRUE, a new form build id is
      generated when the form is loaded from the cache. If it is subsequently
      saved to the cache again, it will have another cache id and therefore
      the original form and form-state will remain unaltered. This is
      important when page caching is enabled in order to prevent form state
      from leaking between anonymous users.
  - rebuild_info: Internal. Similar to 'build_info', but pertaining to
    drupal_rebuild_form().
  - rebuild: Normally, after the entire form processing is completed and
    submit handlers have run, a form is considered to be done and
    drupal_redirect_form() will redirect the user to a new page using a GET
    request (so a browser refresh does not re-submit the form). However, if
    'rebuild' has been set to TRUE, then a new copy of the form is
    immediately built and sent to the browser, instead of a redirect. This is
    used for multi-step forms, such as wizards and confirmation forms.
    Normally, $form_state['rebuild'] is set by a submit handler, since it is
    usually logic within a submit handler that determines whether a form is
    done or requires another step. However, a validation handler may already
    set $form_state['rebuild'] to cause the form processing to bypass submit
    handlers and rebuild the form instead, even if there are no validation
    errors.
  - redirect: Used to redirect the form on submission. It may either be a
    string containing the destination URL, or an array of arguments
    compatible with drupal_goto(). See drupal_redirect_form() for complete
    information.
  - no_redirect: If set to TRUE the form will NOT perform a drupal_goto(),
    even if 'redirect' is set.
  - method: The HTTP form method to use for finding the input for this form.
    May be 'post' or 'get'. Defaults to 'post'. Note that 'get' method
    forms do not use form ids so are always considered to be submitted, which
    can have unexpected effects. The 'get' method should only be used on
    forms that do not change data, as that is exclusively the domain of
    'post.'
  - cache: If set to TRUE the original, unprocessed form structure will be
    cached, which allows the entire form to be rebuilt from cache. A typical
    form workflow involves two page requests; first, a form is built and
    rendered for the user to fill in. Then, the user fills the form in and
    submits it, triggering a second page request in which the form must be
    built and processed. By default, $form and $form_state are built from
    scratch during each of these page requests. Often, it is necessary or
    desired to persist the $form and $form_state variables from the initial
    page request to the one that processes the submission. 'cache' can be set
    to TRUE to do this. A prominent example is an Ajax-enabled form, in which
    ajax_process_form() enables form caching for all forms that include an
    element with the #ajax property. (The Ajax handler has no way to build
    the form itself, so must rely on the cached version.) Note that the
    persistence of $form and $form_state happens automatically for
    (multi-step) forms having the 'rebuild' flag set, regardless of the value
    for 'cache'.
  - no_cache: If set to TRUE the form will NOT be cached, even if 'cache' is
    set.
  - values: An associative array of values submitted to the form. The
    validation functions and submit functions use this array for nearly all
    their decision making. (Note that #tree determines whether the values are
    a flat array or an array whose structure parallels the $form array. See
    @link forms_api_reference.html Form API reference @endlink for more
    information.) These are raw and unvalidated, so should not be used
    without a thorough understanding of security implications. In almost all
    cases, code should use the data in the 'values' array exclusively. The
    most common use of this key is for multi-step forms that need to clear
    some of the user input when setting 'rebuild'. The values correspond to
    $_POST or $_GET, depending on the 'method' chosen.
  - always_process: If TRUE and the method is GET, a form_id is not
    necessary. This should only be used on RESTful GET forms that do NOT
    write data, as this could lead to security issues. It is useful so that
    searches do not need to have a form_id in their query arguments to
    trigger the search.
  - must_validate: Ordinarily, a form is only validated once, but there are
    times when a form is resubmitted internally and should be validated
    again. Setting this to TRUE will force that to happen. This is most
    likely to occur during Ajax operations.
  - programmed: If TRUE, the form was submitted programmatically, usually
    invoked via drupal_form_submit(). Defaults to FALSE.
  - programmed_bypass_access_check: If TRUE, programmatic form submissions
    are processed without taking #access into account. Set this to FALSE
    when submitting a form programmatically with values that may have been
    input by the user executing the current request; this will cause #access
    to be respected as it would on a normal form submission. Defaults to
    TRUE.
  - process_input: Boolean flag. TRUE signifies correct form submission.
    This is always TRUE for programmed forms coming from drupal_form_submit()
    (see 'programmed' key), or if the form_id coming from the $_POST data is
    set and matches the current form_id.
  - submitted: If TRUE, the form has been submitted. Defaults to FALSE.
  - executed: If TRUE, the form was submitted and has been processed and
    executed. Defaults to FALSE.
  - triggering_element: (read-only) The form element that triggered
    submission. This is the same as the deprecated
    $form_state['clicked_button']. It is the element that caused submission,
    which may or may not be a button (in the case of Ajax forms). This key is
    often used to distinguish between various buttons in a submit handler,
    and is also used in Ajax handlers.
  - clicked_button: Deprecated. Use triggering_element instead.
  - has_file_element: Internal. If TRUE, there is a file element and Form API
    will set the appropriate 'enctype' HTML attribute on the form.
  - groups: Internal. An array containing references to fieldsets to render
    them within vertical tabs.
  - storage: $form_state['storage'] is not a special key, and no specific
    support is provided for it in the Form API. By tradition it was
    the location where application-specific data was stored for communication
    between the submit, validation, and form builder functions, especially
    in a multi-step-style form. Form implementations may use any key(s)
    within $form_state (other than the keys listed here and other reserved
    ones used by Form API internals) for this kind of storage. The
    recommended way to ensure that the chosen key doesn't conflict with ones
    used by the Form API or other modules is to use the module name as the
    key name or a prefix for the key name. For example, the Node module uses
    $form_state['node'] in node editing forms to store information about the
    node being edited, and this information stays available across successive
    clicks of the "Preview" button as well as when the "Save" button is
    finally clicked.
  - buttons: A list containing copies of all submit and button elements in
    the form.
  - complete form: A reference to the $form variable containing the complete
    form structure. #process, #after_build, #element_validate, and other
    handlers being invoked on a form element may use this reference to access
    other information in the form the element is contained in.
  - temporary: An array holding temporary data accessible during the current
    page request only. All $form_state properties that are not reserved keys
    (see form_state_keys_no_cache()) persist throughout a multistep form
    sequence. Form API provides this key for modules to communicate
    information across form-related functions during a single page request.
    It may be used to temporarily save data that does not need to or should
    not be cached during the whole form workflow; e.g., data that needs to be
    accessed during the current form build process only. There is no use-case
    for this functionality in Drupal core.
  - wrapper_callback: Modules that wish to pre-populate certain forms with
    common elements, such as back/next/save buttons in multi-step form
    wizards, may define a form builder function name that returns a form
    structure, which is passed on to the actual form builder function.
    Such implementations may either define the 'wrapper_callback' via
    hook_forms() or have to invoke drupal_build_form() (instead of
    drupal_get_form()) on their own in a custom menu callback to prepare
    $form_state accordingly.
  Information on how certain $form_state properties control redirection
  behavior after form submission may be found in drupal_redirect_form().

@return
  The rendered form. This function may also perform a redirect and hence may
  not return at all, depending upon the $form_state flags that were set.

@see drupal_redirect_form()
```

## Code

```php
function drupal_build_form($form_id, &$form_state) {
  // Ensure some defaults; if already set they will not be overridden.
  $form_state += form_state_defaults();

  if (!isset($form_state['input'])) {
    $form_state['input'] = $form_state['method'] == 'get' ? $_GET : $_POST;
  }

  if (isset($_SESSION['batch_form_state'])) {
    // We've been redirected here after a batch processing. The form has
    // already been processed, but needs to be rebuilt. See _batch_finished().
    $form_state = $_SESSION['batch_form_state'];
    unset($_SESSION['batch_form_state']);
    return drupal_rebuild_form($form_id, $form_state);
  }

  // If the incoming input contains a form_build_id, we'll check the cache for a
  // copy of the form in question. If it's there, we don't have to rebuild the
  // form to proceed. In addition, if there is stored form_state data from a
  // previous step, we'll retrieve it so it can be passed on to the form
  // processing code.
  $check_cache = isset($form_state['input']['form_id']) && $form_state['input']['form_id'] == $form_id && !empty($form_state['input']['form_build_id']);
  if ($check_cache) {
    $form = form_get_cache($form_state['input']['form_build_id'], $form_state);
  }

  // If the previous bit of code didn't result in a populated $form object, we
  // are hitting the form for the first time and we need to build it from
  // scratch.
  if (!isset($form)) {
    // If we attempted to serve the form from cache, uncacheable $form_state
    // keys need to be removed after retrieving and preparing the form, except
    // any that were already set prior to retrieving the form.
    if ($check_cache) {
      $form_state_before_retrieval = $form_state;
    }

    $form = drupal_retrieve_form($form_id, $form_state);
    drupal_prepare_form($form_id, $form, $form_state);

    // form_set_cache() removes uncacheable $form_state keys defined in
    // form_state_keys_no_cache() in order for multi-step forms to work
    // properly. This means that form processing logic for single-step forms
    // using $form_state['cache'] may depend on data stored in those keys
    // during drupal_retrieve_form()/drupal_prepare_form(), but form
    // processing should not depend on whether the form is cached or not, so
    // $form_state is adjusted to match what it would be after a
    // form_set_cache()/form_get_cache() sequence. These exceptions are
    // allowed to survive here:
    // - always_process: Does not make sense in conjunction with form caching
    //   in the first place, since passing form_build_id as a GET parameter is
    //   not desired.
    // - temporary: Any assigned data is expected to survives within the same
    //   page request.
    if ($check_cache) {
      $uncacheable_keys = array_flip(array_diff(form_state_keys_no_cache(), array('always_process', 'temporary')));
      $form_state = array_diff_key($form_state, $uncacheable_keys);
      $form_state += $form_state_before_retrieval;
    }
  }

  // Now that we have a constructed form, process it. This is where:
  // - Element #process functions get called to further refine $form.
  // - User input, if any, gets incorporated in the #value property of the
  //   corresponding elements and into $form_state['values'].
  // - Validation and submission handlers are called.
  // - If this submission is part of a multistep workflow, the form is rebuilt
  //   to contain the information of the next step.
  // - If necessary, the form and form state are cached or re-cached, so that
  //   appropriate information persists to the next page request.
  // All of the handlers in the pipeline receive $form_state by reference and
  // can use it to know or update information about the state of the form.
  drupal_process_form($form_id, $form, $form_state);

  // If this was a successful submission of a single-step form or the last step
  // of a multi-step form, then drupal_process_form() issued a redirect to
  // another page, or back to this page, but as a new request. Therefore, if
  // we're here, it means that this is either a form being viewed initially
  // before any user input, or there was a validation error requiring the form
  // to be re-displayed, or we're in a multi-step workflow and need to display
  // the form's next step. In any case, we have what we need in $form, and can
  // return it for rendering.
  return $form;
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
