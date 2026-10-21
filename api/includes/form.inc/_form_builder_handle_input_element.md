# _form_builder_handle_input_element()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 2030–2184 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L2030-L2184)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function _form_builder_handle_input_element($form_id, &$element, &$form_state)
```

## Documentation

```text
Adds the #name and #value properties of an input element before rendering.
```

## Code

```php
function _form_builder_handle_input_element($form_id, &$element, &$form_state) {
  static $safe_core_value_callbacks = array(
    'form_type_token_value',
    'form_type_textarea_value',
    'form_type_textfield_value',
    'form_type_checkbox_value',
    'form_type_checkboxes_value',
    'form_type_radios_value',
    'form_type_password_confirm_value',
    'form_type_select_value',
    'form_type_tableselect_value',
    'list_boolean_allowed_values_callback',
  );

  if (!isset($element['#name'])) {
    $name = array_shift($element['#parents']);
    $element['#name'] = $name;
    if ($element['#type'] == 'file') {
      // To make it easier to handle $_FILES in file.inc, we place all
      // file fields in the 'files' array. Also, we do not support
      // nested file names.
      $element['#name'] = 'files[' . $element['#name'] . ']';
    }
    elseif (count($element['#parents'])) {
      $element['#name'] .= '[' . implode('][', $element['#parents']) . ']';
    }
    array_unshift($element['#parents'], $name);
  }

  // Setting #disabled to TRUE results in user input being ignored, regardless
  // of how the element is themed or whether JavaScript is used to change the
  // control's attributes. However, it's good UI to let the user know that input
  // is not wanted for the control. HTML supports two attributes for this:
  // http://www.w3.org/TR/html401/interact/forms.html#h-17.12. If a form wants
  // to start a control off with one of these attributes for UI purposes only,
  // but still allow input to be processed if it's sumitted, it can set the
  // desired attribute in #attributes directly rather than using #disabled.
  // However, developers should think carefully about the accessibility
  // implications of doing so: if the form expects input to be enterable under
  // some condition triggered by JavaScript, how would someone who has
  // JavaScript disabled trigger that condition? Instead, developers should
  // consider whether a multi-step form would be more appropriate (#disabled can
  // be changed from step to step). If one still decides to use JavaScript to
  // affect when a control is enabled, then it is best for accessibility for the
  // control to be enabled in the HTML, and disabled by JavaScript on document
  // ready.
  if (!empty($element['#disabled'])) {
    if (!empty($element['#allow_focus'])) {
      $element['#attributes']['readonly'] = 'readonly';
    }
    else {
      $element['#attributes']['disabled'] = 'disabled';
    }
  }

  // With JavaScript or other easy hacking, input can be submitted even for
  // elements with #access=FALSE or #disabled=TRUE. For security, these must
  // not be processed. Forms that set #disabled=TRUE on an element do not
  // expect input for the element, and even forms submitted with
  // drupal_form_submit() must not be able to get around this. Forms that set
  // #access=FALSE on an element usually allow access for some users, so forms
  // submitted with drupal_form_submit() may bypass access restriction and be
  // treated as high-privilege users instead.
  $process_input = empty($element['#disabled']) && ($element['#type'] !== 'value') && (($form_state['programmed'] && $form_state['programmed_bypass_access_check']) || ($form_state['process_input'] && (!isset($element['#access']) || $element['#access'])));

  // Set the element's #value property.
  if (!isset($element['#value']) && !array_key_exists('#value', $element)) {
    $value_callback = !empty($element['#value_callback']) ? $element['#value_callback'] : 'form_type_' . $element['#type'] . '_value';
    if ($process_input) {
      // Get the input for the current element. NULL values in the input need to
      // be explicitly distinguished from missing input. (see below)
      $input_exists = NULL;
      $input = drupal_array_get_nested_value($form_state['input'], $element['#parents'], $input_exists);
      // For browser-submitted forms, the submitted values do not contain values
      // for certain elements (empty multiple select, unchecked checkbox).
      // During initial form processing, we add explicit NULL values for such
      // elements in $form_state['input']. When rebuilding the form, we can
      // distinguish elements having NULL input from elements that were not part
      // of the initially submitted form and can therefore use default values
      // for the latter, if required. Programmatically submitted forms can
      // submit explicit NULL values when calling drupal_form_submit(), so we do
      // not modify $form_state['input'] for them.
      if (!$input_exists && !$form_state['rebuild'] && !$form_state['programmed']) {
        // Add the necessary parent keys to $form_state['input'] and sets the
        // element's input value to NULL.
        drupal_array_set_nested_value($form_state['input'], $element['#parents'], NULL);
        $input_exists = TRUE;
      }
      // If we have input for the current element, assign it to the #value
      // property, optionally filtered through $value_callback.
      if ($input_exists) {
        if (function_exists($value_callback)) {
          // Skip all value callbacks except safe ones like text if the CSRF
          // token was invalid.
          if (empty($form_state['invalid_token']) || in_array($value_callback, $safe_core_value_callbacks)) {
            $element['#value'] = $value_callback($element, $input, $form_state);
          }
          else {
            $input = NULL;
          }
        }
        if (!isset($element['#value']) && isset($input)) {
          $element['#value'] = $input;
        }
      }
      // Mark all posted values for validation.
      if (isset($element['#value']) || (!empty($element['#required']))) {
        $element['#needs_validation'] = TRUE;
      }
    }
    // Load defaults.
    if (!isset($element['#value'])) {
      // Call #type_value without a second argument to request default_value handling.
      if (function_exists($value_callback)) {
        $element['#value'] = $value_callback($element, FALSE, $form_state);
      }
      // Final catch. If we haven't set a value yet, use the explicit default value.
      // Avoid image buttons (which come with garbage value), so we only get value
      // for the button actually clicked.
      if (!isset($element['#value']) && empty($element['#has_garbage_value'])) {
        $element['#value'] = isset($element['#default_value']) ? $element['#default_value'] : '';
      }
    }
  }

  // Determine which element (if any) triggered the submission of the form and
  // keep track of all the clickable buttons in the form for
  // form_state_values_clean(). Enforce the same input processing restrictions
  // as above.
  if ($process_input) {
    // Detect if the element triggered the submission via Ajax.
    if (_form_element_triggered_scripted_submission($element, $form_state)) {
      $form_state['triggering_element'] = $element;
    }

    // If the form was submitted by the browser rather than via Ajax, then it
    // can only have been triggered by a button, and we need to determine which
    // button within the constraints of how browsers provide this information.
    if (isset($element['#button_type'])) {
      // All buttons in the form need to be tracked for
      // form_state_values_clean() and for the form_builder() code that handles
      // a form submission containing no button information in $_POST.
      $form_state['buttons'][] = $element;
      if (_form_button_was_clicked($element, $form_state)) {
        $form_state['triggering_element'] = $element;
      }
    }
  }

  // Set the element's value in $form_state['values'], but only, if its key
  // does not exist yet (a #value_callback may have already populated it).
  if (!drupal_array_nested_key_exists($form_state['values'], $element['#parents'])) {
    form_set_value($element, $element['#value'], $form_state);
  }
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
