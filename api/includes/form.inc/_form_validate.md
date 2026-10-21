# _form_validate()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 1348–1487 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L1348-L1487)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function _form_validate(&$elements, &$form_state, $form_id = NULL)
```

## Documentation

```text
Performs validation on form elements.

First ensures required fields are completed, #maxlength is not exceeded, and
selected options were in the list of options given to the user. Then calls
user-defined validators.

@param $elements
  An associative array containing the structure of the form.
@param $form_state
  A keyed array containing the current state of the form. The current
  user-submitted data is stored in $form_state['values'], though
  form validation functions are passed an explicit copy of the
  values for the sake of simplicity. Validation handlers can also
  $form_state to pass information on to submit handlers. For example:
    $form_state['data_for_submission'] = $data;
  This technique is useful when validation requires file parsing,
  web service requests, or other expensive requests that should
  not be repeated in the submission step.
@param $form_id
  A unique string identifying the form for validation, submission,
  theming, and hook_form_alter functions.
```

## Code

```php
function _form_validate(&$elements, &$form_state, $form_id = NULL) {
  // Also used in the installer, pre-database setup.
  $t = get_t();

  // Recurse through all children.
  foreach (element_children($elements) as $key) {
    if (isset($elements[$key]) && $elements[$key]) {
      _form_validate($elements[$key], $form_state);
    }
  }

  // Validate the current input.
  if (!isset($elements['#validated']) || !$elements['#validated']) {
    // The following errors are always shown.
    if (isset($elements['#needs_validation'])) {
      // Verify that the value is not longer than #maxlength.
      if (isset($elements['#maxlength']) && (isset($elements['#value']) && !is_scalar($elements['#value']))) {
        form_error($elements, $t('An illegal value has been detected. Please contact the site administrator.'));
      }
      elseif (isset($elements['#maxlength']) && drupal_strlen($elements['#value']) > $elements['#maxlength']) {
        form_error($elements, $t('!name cannot be longer than %max characters but is currently %length characters long.', array('!name' => empty($elements['#title']) ? $elements['#parents'][0] : $elements['#title'], '%max' => $elements['#maxlength'], '%length' => drupal_strlen($elements['#value']))));
      }

      if (isset($elements['#options']) && isset($elements['#value'])) {
        if ($elements['#type'] == 'select') {
          $options = form_options_flatten($elements['#options']);
        }
        else {
          $options = $elements['#options'];
        }
        if (is_array($elements['#value'])) {
          $value = in_array($elements['#type'], array('checkboxes', 'tableselect')) ? array_keys($elements['#value']) : $elements['#value'];
          foreach ($value as $v) {
            if (!isset($options[$v])) {
              form_error($elements, $t('An illegal choice has been detected. Please contact the site administrator.'));
              watchdog('form', 'Illegal choice %choice in !name element.', array('%choice' => $v, '!name' => empty($elements['#title']) ? $elements['#parents'][0] : $elements['#title']), WATCHDOG_ERROR);
            }
          }
        }
        // Non-multiple select fields always have a value in HTML. If the user
        // does not change the form, it will be the value of the first option.
        // Because of this, form validation for the field will almost always
        // pass, even if the user did not select anything. To work around this
        // browser behavior, required select fields without a #default_value get
        // an additional, first empty option. In case the submitted value is
        // identical to the empty option's value, we reset the element's value
        // to NULL to trigger the regular #required handling below.
        // @see form_process_select()
        elseif ($elements['#type'] == 'select' && $elements['#required']
        && (!array_key_exists('#multiple', $elements) || !$elements['#multiple'])
        && !isset($elements['#default_value'])
        && $elements['#value'] === $elements['#empty_value']) {
          $elements['#value'] = NULL;
          form_set_value($elements, NULL, $form_state);
        }
        elseif (!isset($options[$elements['#value']])) {
          form_error($elements, $t('An illegal choice has been detected. Please contact the site administrator.'));
          watchdog('form', 'Illegal choice %choice in %name element.', array('%choice' => $elements['#value'], '%name' => empty($elements['#title']) ? $elements['#parents'][0] : $elements['#title']), WATCHDOG_ERROR);
        }
      }
    }

    // While this element is being validated, it may be desired that some calls
    // to form_set_error() be suppressed and not result in a form error, so
    // that a button that implements low-risk functionality (such as "Previous"
    // or "Add more") that doesn't require all user input to be valid can still
    // have its submit handlers triggered. The triggering element's
    // #limit_validation_errors property contains the information for which
    // errors are needed, and all other errors are to be suppressed. The
    // #limit_validation_errors property is ignored if submit handlers will run,
    // but the element doesn't have a #submit property, because it's too large a
    // security risk to have any invalid user input when executing form-level
    // submit handlers.
    if (isset($form_state['triggering_element']['#limit_validation_errors']) && ($form_state['triggering_element']['#limit_validation_errors'] !== FALSE) && !($form_state['submitted'] && !isset($form_state['triggering_element']['#submit']))) {
      form_set_error(NULL, '', $form_state['triggering_element']['#limit_validation_errors']);
    }
    // If submit handlers won't run (due to the submission having been triggered
    // by an element whose #executes_submit_callback property isn't TRUE), then
    // it's safe to suppress all validation errors, and we do so by default,
    // which is particularly useful during an Ajax submission triggered by a
    // non-button. An element can override this default by setting the
    // #limit_validation_errors property. For button element types,
    // #limit_validation_errors defaults to FALSE (via system_element_info()),
    // so that full validation is their default behavior.
    elseif (isset($form_state['triggering_element']) && !isset($form_state['triggering_element']['#limit_validation_errors']) && !$form_state['submitted']) {
      form_set_error(NULL, '', array());
    }
    // As an extra security measure, explicitly turn off error suppression if
    // one of the above conditions wasn't met. Since this is also done at the
    // end of this function, doing it here is only to handle the rare edge case
    // where a validate handler invokes form processing of another form.
    else {
      drupal_static_reset('form_set_error:limit_validation_errors');
    }

    // Make sure a value is passed when the field is required.
    if (isset($elements['#needs_validation']) && $elements['#required']) {
      // A simple call to empty() will not cut it here as some fields, like
      // checkboxes, can return a valid value of '0'. Instead, check the
      // length if it's a string, and the item count if it's an array.
      // An unchecked checkbox has a #value of integer 0, different than string
      // '0', which could be a valid value.
      $is_countable = is_array($elements['#value']) || $elements['#value'] instanceof Countable;
      $is_empty_multiple = $is_countable && count($elements['#value']) == 0;
      $is_empty_string = (is_string($elements['#value']) && drupal_strlen(trim($elements['#value'])) == 0);
      $is_empty_value = ($elements['#value'] === 0);
      $is_empty_null = is_null($elements['#value']);
      if ($is_empty_multiple || $is_empty_string || $is_empty_value || $is_empty_null) {
        // Although discouraged, a #title is not mandatory for form elements. In
        // case there is no #title, we cannot set a form error message.
        // Instead of setting no #title, form constructors are encouraged to set
        // #title_display to 'invisible' to improve accessibility.
        if (isset($elements['#title'])) {
          form_error($elements, $t('!name field is required.', array('!name' => $elements['#title'])));
        }
        else {
          form_error($elements);
        }
      }
    }

    // Call user-defined form level validators.
    if (isset($form_id)) {
      form_execute_handlers('validate', $elements, $form_state);
    }
    // Call any element-specific validators. These must act on the element
    // #value data.
    elseif (isset($elements['#element_validate'])) {
      foreach ($elements['#element_validate'] as $function) {
        $function($elements, $form_state, $form_state['complete form']);
      }
    }
    $elements['#validated'] = TRUE;
  }

  // Done validating this element, so turn off error suppression.
  // _form_validate() turns it on again when starting on the next element, if
  // it's still appropriate to do so.
  drupal_static_reset('form_set_error:limit_validation_errors');
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
