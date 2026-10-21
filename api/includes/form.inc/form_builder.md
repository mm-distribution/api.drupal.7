# form_builder()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 1814–2025 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L1814-L2025)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function form_builder($form_id, &$element, &$form_state)
```

## Documentation

```text
Builds and processes all elements in the structured form array.

Adds any required properties to each element, maps the incoming input data
to the proper elements, and executes any #process handlers attached to a
specific element.

This is one of the three primary functions that recursively iterates a form
array. This one does it for completing the form building process. The other
two are _form_validate() (invoked via drupal_validate_form() and used to
invoke validation logic for each element) and drupal_render() (for rendering
each element). Each of these three pipelines provides ample opportunity for
modules to customize what happens. For example, during this function's life
cycle, the following functions get called for each element:
- $element['#value_callback']: A function that implements how user input is
  mapped to an element's #value property. This defaults to a function named
  'form_type_TYPE_value' where TYPE is $element['#type'].
- $element['#process']: An array of functions called after user input has
  been mapped to the element's #value property. These functions can be used
  to dynamically add child elements: for example, for the 'date' element
  type, one of the functions in this array is form_process_date(), which adds
  the individual 'year', 'month', 'day', etc. child elements. These functions
  can also be used to set additional properties or implement special logic
  other than adding child elements: for example, for the 'fieldset' element
  type, one of the functions in this array is form_process_fieldset(), which
  adds the attributes and JavaScript needed to make the fieldset collapsible
  if the #collapsible property is set. The #process functions are called in
  preorder traversal, meaning they are called for the parent element first,
  then for the child elements.
- $element['#after_build']: An array of functions called after form_builder()
  is done with its processing of the element. These are called in postorder
  traversal, meaning they are called for the child elements first, then for
  the parent element.
There are similar properties containing callback functions invoked by
_form_validate() and drupal_render(), appropriate for those operations.

Developers are strongly encouraged to integrate the functionality needed by
their form or module within one of these three pipelines, using the
appropriate callback property, rather than implementing their own recursive
traversal of a form array. This facilitates proper integration between
multiple modules. For example, module developers are familiar with the
relative order in which hook_form_alter() implementations and #process
functions run. A custom traversal function that affects the building of a
form is likely to not integrate with hook_form_alter() and #process in the
expected way. Also, deep recursion within PHP is both slow and memory
intensive, so it is best to minimize how often it's done.

As stated above, each element's #process functions are executed after its
#value has been set. This enables those functions to execute conditional
logic based on the current value. However, all of form_builder() runs before
drupal_validate_form() is called, so during #process function execution, the
element's #value has not yet been validated, so any code that requires
validated values must reside within a submit handler.

As a security measure, user input is used for an element's #value only if the
element exists within $form, is not disabled (as per the #disabled property),
and can be accessed (as per the #access property, except that forms submitted
using drupal_form_submit() bypass #access restrictions). When user input is
ignored due to #disabled and #access restrictions, the element's default
value is used.

Because of the preorder traversal, where #process functions of an element run
before user input for its child elements is processed, and because of the
Form API security of user input processing with respect to #access and
#disabled described above, this generally means that #process functions
should not use an element's (unvalidated) #value to affect the #disabled or
#access of child elements. Use-cases where a developer may be tempted to
implement such conditional logic usually fall into one of two categories:
- Where user input from the current submission must affect the structure of a
  form, including properties like #access and #disabled that affect how the
  next submission needs to be processed, a multi-step workflow is needed.
  This is most commonly implemented with a submit handler setting persistent
  data within $form_state based on *validated* values in
  $form_state['values'] and setting $form_state['rebuild']. The form building
  functions must then be implemented to use the $form_state data to rebuild
  the form with the structure appropriate for the new state.
- Where user input must affect the rendering of the form without affecting
  its structure, the necessary conditional rendering logic should reside
  within functions that run during the rendering phase (#pre_render, #theme,
  #theme_wrappers, and #post_render).

@param $form_id
  A unique string identifying the form for validation, submission,
  theming, and hook_form_alter functions.
@param $element
  An associative array containing the structure of the current element.
@param $form_state
  A keyed array containing the current state of the form. In this
  context, it is used to accumulate information about which button
  was clicked when the form was submitted, as well as the sanitized
  $_POST data.
```

## Code

```php
function form_builder($form_id, &$element, &$form_state) {
  // Initialize as unprocessed.
  $element['#processed'] = FALSE;

  // Use element defaults.
  if (isset($element['#type']) && empty($element['#defaults_loaded']) && ($info = element_info($element['#type']))) {
    // Overlay $info onto $element, retaining preexisting keys in $element.
    $element += $info;
    $element['#defaults_loaded'] = TRUE;
  }
  // Assign basic defaults common for all form elements.
  $element += array(
    '#required' => FALSE,
    '#attributes' => array(),
    '#title_display' => 'before',
  );

  // Special handling if we're on the top level form element.
  if (isset($element['#type']) && $element['#type'] == 'form') {
    if (!empty($element['#https']) && variable_get('https', FALSE) &&
        !url_is_external($element['#action'])) {
      global $base_root;

      // Not an external URL so ensure that it is secure.
      $element['#action'] = str_replace('http://', 'https://', $base_root) . $element['#action'];
    }

    // Store a reference to the complete form in $form_state prior to building
    // the form. This allows advanced #process and #after_build callbacks to
    // perform changes elsewhere in the form.
    $form_state['complete form'] = &$element;

    // Set a flag if we have a correct form submission. This is always TRUE for
    // programmed forms coming from drupal_form_submit(), or if the form_id coming
    // from the POST data is set and matches the current form_id.
    if ($form_state['programmed'] || (!empty($form_state['input']) && (isset($form_state['input']['form_id']) && ($form_state['input']['form_id'] == $form_id)))) {
      $form_state['process_input'] = TRUE;
      // If the session token was set by drupal_prepare_form(), ensure that it
      // matches the current user's session.
      $form_state['invalid_token'] = FALSE;
      if (!empty($element['#token'])) {
        if (empty($form_state['input']['form_token']) || !drupal_valid_token($form_state['input']['form_token'], $element['#token'])) {
          // Set an early form error to block certain input processing since that
          // opens the door for CSRF vulnerabilities.
          _drupal_invalid_token_set_form_error();
          // This value is checked in _form_builder_handle_input_element().
          $form_state['invalid_token'] = TRUE;
          // Ignore all submitted values.
          $form_state['input'] = array();
          $_POST = array();
          // Make sure file uploads do not get processed.
          $_FILES = array();
        }
      }
    }
    else {
      $form_state['process_input'] = FALSE;
    }

    // All form elements should have an #array_parents property.
    $element['#array_parents'] = array();
  }

  if (!isset($element['#id'])) {
    $element['#id'] = drupal_html_id('edit-' . implode('-', $element['#parents']));
  }
  // Handle input elements.
  if (!empty($element['#input'])) {
    _form_builder_handle_input_element($form_id, $element, $form_state);
  }
  // Allow for elements to expand to multiple elements, e.g., radios,
  // checkboxes and files.
  if (isset($element['#process']) && !$element['#processed']) {
    foreach ($element['#process'] as $process) {
      $element = $process($element, $form_state, $form_state['complete form']);
    }
    $element['#processed'] = TRUE;
  }

  // We start off assuming all form elements are in the correct order.
  $element['#sorted'] = TRUE;

  // Recurse through all child elements.
  $count = 0;
  foreach (element_children($element) as $key) {
    // Prior to checking properties of child elements, their default properties
    // need to be loaded.
    if (isset($element[$key]['#type']) && empty($element[$key]['#defaults_loaded']) && ($info = element_info($element[$key]['#type']))) {
      $element[$key] += $info;
      $element[$key]['#defaults_loaded'] = TRUE;
    }

    // Don't squash an existing tree value.
    if (!isset($element[$key]['#tree'])) {
      $element[$key]['#tree'] = $element['#tree'];
    }

    // Deny access to child elements if parent is denied.
    if (isset($element['#access']) && !$element['#access']) {
      $element[$key]['#access'] = FALSE;
    }

    // Make child elements inherit their parent's #disabled and #allow_focus
    // values unless they specify their own.
    foreach (array('#disabled', '#allow_focus') as $property) {
      if (isset($element[$property]) && !isset($element[$key][$property])) {
        $element[$key][$property] = $element[$property];
      }
    }

    // Don't squash existing parents value.
    if (!isset($element[$key]['#parents'])) {
      // Check to see if a tree of child elements is present. If so,
      // continue down the tree if required.
      $element[$key]['#parents'] = $element[$key]['#tree'] && $element['#tree'] ? array_merge($element['#parents'], array($key)) : array($key);
    }
    // Ensure #array_parents follows the actual form structure.
    $array_parents = $element['#array_parents'];
    $array_parents[] = $key;
    $element[$key]['#array_parents'] = $array_parents;

    // Assign a decimal placeholder weight to preserve original array order.
    if (!isset($element[$key]['#weight'])) {
      $element[$key]['#weight'] = $count/1000;
    }
    else {
      // If one of the child elements has a weight then we will need to sort
      // later.
      unset($element['#sorted']);
    }
    $element[$key] = form_builder($form_id, $element[$key], $form_state);
    $count++;
  }

  // The #after_build flag allows any piece of a form to be altered
  // after normal input parsing has been completed.
  if (isset($element['#after_build']) && !isset($element['#after_build_done'])) {
    foreach ($element['#after_build'] as $function) {
      $element = $function($element, $form_state);
    }
    $element['#after_build_done'] = TRUE;
  }

  // If there is a file element, we need to flip a flag so later the
  // form encoding can be set.
  if (isset($element['#type']) && $element['#type'] == 'file') {
    $form_state['has_file_element'] = TRUE;
  }

  // Final tasks for the form element after form_builder() has run for all other
  // elements.
  if (isset($element['#type']) && $element['#type'] == 'form') {
    // If there is a file element, we set the form encoding.
    if (isset($form_state['has_file_element'])) {
      $element['#attributes']['enctype'] = 'multipart/form-data';
    }

    // Allow Ajax submissions to the form action to bypass verification. This is
    // especially useful for multipart forms, which cannot be verified via a
    // response header.
    $element['#attached']['js'][] = array(
      'type' => 'setting',
      'data' => array(
        'urlIsAjaxTrusted' => array(
          $element['#action'] => TRUE,
        ),
      ),
    );

    // If a form contains a single textfield, and the ENTER key is pressed
    // within it, Internet Explorer submits the form with no POST data
    // identifying any submit button. Other browsers submit POST data as though
    // the user clicked the first button. Therefore, to be as consistent as we
    // can be across browsers, if no 'triggering_element' has been identified
    // yet, default it to the first button.
    if (!$form_state['programmed'] && !isset($form_state['triggering_element']) && !empty($form_state['buttons'])) {
      $form_state['triggering_element'] = $form_state['buttons'][0];
    }

    // If the triggering element specifies "button-level" validation and submit
    // handlers to run instead of the default form-level ones, then add those to
    // the form state.
    foreach (array('validate', 'submit') as $type) {
      if (isset($form_state['triggering_element']['#' . $type])) {
        $form_state[$type . '_handlers'] = $form_state['triggering_element']['#' . $type];
      }
    }

    // If the triggering element executes submit handlers, then set the form
    // state key that's needed for those handlers to run.
    if (!empty($form_state['triggering_element']['#executes_submit_callback'])) {
      $form_state['submitted'] = TRUE;
    }

    // Special processing if the triggering element is a button.
    if (isset($form_state['triggering_element']['#button_type'])) {
      // Because there are several ways in which the triggering element could
      // have been determined (including from input variables set by JavaScript
      // or fallback behavior implemented for IE), and because buttons often
      // have their #name property not derived from their #parents property, we
      // can't assume that input processing that's happened up until here has
      // resulted in $form_state['values'][BUTTON_NAME] being set. But it's
      // common for forms to have several buttons named 'op' and switch on
      // $form_state['values']['op'] during submit handler execution.
      $form_state['values'][$form_state['triggering_element']['#name']] = $form_state['triggering_element']['#value'];

      // @todo Legacy support. Remove in Drupal 8.
      $form_state['clicked_button'] = $form_state['triggering_element'];
    }
  }
  return $element;
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
