# drupal_validate_form()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 1167–1235 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L1167-L1235)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function drupal_validate_form($form_id, &$form, &$form_state)
```

## Documentation

```text
Validates user-submitted form data in the $form_state array.

@param $form_id
  A unique string identifying the form for validation, submission,
  theming, and hook_form_alter functions.
@param $form
  An associative array containing the structure of the form, which is passed
  by reference. Form validation handlers are able to alter the form structure
  (like #process and #after_build callbacks during form building) in case of
  a validation error. If a validation handler alters the form structure, it
  is responsible for validating the values of changed form elements in
  $form_state['values'] to prevent form submit handlers from receiving
  unvalidated values.
@param $form_state
  A keyed array containing the current state of the form. The current
  user-submitted data is stored in $form_state['values'], though
  form validation functions are passed an explicit copy of the
  values for the sake of simplicity. Validation handlers can also use
  $form_state to pass information on to submit handlers. For example:
    $form_state['data_for_submission'] = $data;
  This technique is useful when validation requires file parsing,
  web service requests, or other expensive requests that should
  not be repeated in the submission step.
```

## Code

```php
function drupal_validate_form($form_id, &$form, &$form_state) {
  $validated_forms = &drupal_static(__FUNCTION__, array());

  if (isset($validated_forms[$form_id]) && empty($form_state['must_validate'])) {
    return;
  }

  // If the session token was set by drupal_prepare_form(), ensure that it
  // matches the current user's session. This is duplicate to code in
  // form_builder() but left to protect any custom form handling code.
  if (!empty($form['#token'])) {
    if (!drupal_valid_token($form_state['values']['form_token'], $form['#token']) || !empty($form_state['invalid_token'])) {
      _drupal_invalid_token_set_form_error();
      // Ignore all submitted values.
      $form_state['input'] = array();
      $_POST = array();
      // Make sure file uploads do not get processed.
      $_FILES = array();
      // Stop here and don't run any further validation handlers, because they
      // could invoke non-safe operations which opens the door for CSRF
      // vulnerabilities.
      $validated_forms[$form_id] = TRUE;
      return;
    }
  }

  _form_validate($form, $form_state, $form_id);
  $validated_forms[$form_id] = TRUE;

  // If validation errors are limited then remove any non validated form values,
  // so that only values that passed validation are left for submit callbacks.
  if (isset($form_state['triggering_element']['#limit_validation_errors']) && $form_state['triggering_element']['#limit_validation_errors'] !== FALSE) {
    $values = array();
    foreach ($form_state['triggering_element']['#limit_validation_errors'] as $section) {
      // If the section exists within $form_state['values'], even if the value
      // is NULL, copy it to $values.
      $section_exists = NULL;
      $value = drupal_array_get_nested_value($form_state['values'], $section, $section_exists);
      if ($section_exists) {
        drupal_array_set_nested_value($values, $section, $value);
      }
    }
    // A button's #value does not require validation, so for convenience we
    // allow the value of the clicked button to be retained in its normal
    // $form_state['values'] locations, even if these locations are not included
    // in #limit_validation_errors.
    if (isset($form_state['triggering_element']['#button_type'])) {
      $button_value = $form_state['triggering_element']['#value'];

      // Like all input controls, the button value may be in the location
      // dictated by #parents. If it is, copy it to $values, but do not override
      // what may already be in $values.
      $parents = $form_state['triggering_element']['#parents'];
      if (!drupal_array_nested_key_exists($values, $parents) && drupal_array_get_nested_value($form_state['values'], $parents) === $button_value) {
        drupal_array_set_nested_value($values, $parents, $button_value);
      }

      // Additionally, form_builder() places the button value in
      // $form_state['values'][BUTTON_NAME]. If it's still there, after
      // validation handlers have run, copy it to $values, but do not override
      // what may already be in $values.
      $name = $form_state['triggering_element']['#name'];
      if (!isset($values[$name]) && isset($form_state['values'][$name]) && $form_state['values'][$name] === $button_value) {
        $values[$name] = $button_value;
      }
    }
    $form_state['values'] = $values;
  }
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
