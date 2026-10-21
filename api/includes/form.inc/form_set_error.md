# form_set_error()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 1634–1675 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L1634-L1675)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function form_set_error($name = NULL, $message = '', $limit_validation_errors = NULL)
```

## Documentation

```text
Files an error against a form element.

When a validation error is detected, the validator calls form_set_error() to
indicate which element needs to be changed and provide an error message. This
causes the Form API to not execute the form submit handlers, and instead to
re-display the form to the user with the corresponding elements rendered with
an 'error' CSS class (shown as red by default).

The standard form_set_error() behavior can be changed if a button provides
the #limit_validation_errors property. Multistep forms not wanting to
validate the whole form can set #limit_validation_errors on buttons to
limit validation errors to only certain elements. For example, pressing the
"Previous" button in a multistep form should not fire validation errors just
because the current step has invalid values. If #limit_validation_errors is
set on a clicked button, the button must also define a #submit property
(may be set to an empty array). Any #submit handlers will be executed even if
there is invalid input, so extreme care should be taken with respect to any
actions taken by them. This is typically not a problem with buttons like
"Previous" or "Add more" that do not invoke persistent storage of the
submitted form values. Do not use the #limit_validation_errors property on
buttons that trigger saving of form values to the database.

The #limit_validation_errors property is a list of "sections" within
$form_state['values'] that must contain valid values. Each "section" is an
array with the ordered set of keys needed to reach that part of
$form_state['values'] (i.e., the #parents property of the element).

Example 1: Allow the "Previous" button to function, regardless of whether any
user input is valid.

@code
  $form['actions']['previous'] = array(
    '#type' => 'submit',
    '#value' => t('Previous'),
    '#limit_validation_errors' => array(),       // No validation.
    '#submit' => array('some_submit_function'),  // #submit required.
  );
@endcode

Example 2: Require some, but not all, user input to be valid to process the
submission of a "Previous" button.

@code
  $form['actions']['previous'] = array(
    '#type' => 'submit',
    '#value' => t('Previous'),
    '#limit_validation_errors' => array(
      array('step1'),       // Validate $form_state['values']['step1'].
      array('foo', 'bar'),  // Validate $form_state['values']['foo']['bar'].
    ),
    '#submit' => array('some_submit_function'), // #submit required.
  );
@endcode

This will require $form_state['values']['step1'] and everything within it
(for example, $form_state['values']['step1']['choice']) to be valid, so
calls to form_set_error('step1', $message) or
form_set_error('step1][choice', $message) will prevent the submit handlers
from running, and result in the error message being displayed to the user.
However, calls to form_set_error('step2', $message) and
form_set_error('step2][groupX][choiceY', $message) will be suppressed,
resulting in the message not being displayed to the user, and the submit
handlers will run despite $form_state['values']['step2'] and
$form_state['values']['step2']['groupX']['choiceY'] containing invalid
values. Errors for an invalid $form_state['values']['foo'] will be
suppressed, but errors flagging invalid values for
$form_state['values']['foo']['bar'] and everything within it will be
flagged and submission prevented.

Partial form validation is implemented by suppressing errors rather than by
skipping the input processing and validation steps entirely, because some
forms have button-level submit handlers that call Drupal API functions that
assume that certain data exists within $form_state['values'], and while not
doing anything with that data that requires it to be valid, PHP errors
would be triggered if the input processing and validation steps were fully
skipped.

@param $name
  The name of the form element. If the #parents property of your form
  element is array('foo', 'bar', 'baz') then you may set an error on 'foo'
  or 'foo][bar][baz'. Setting an error on 'foo' sets an error for every
  element where the #parents array starts with 'foo'.
@param $message
  The error message to present to the user.
@param $limit_validation_errors
  Internal use only. The #limit_validation_errors property of the clicked
  button, if it exists.

@return
  Return value is for internal use only. To get a list of errors, use
  form_get_errors() or form_get_error().

@see http://drupal.org/node/370537
@see http://drupal.org/node/763376
```

## Code

```php
function form_set_error($name = NULL, $message = '', $limit_validation_errors = NULL) {
  $form = &drupal_static(__FUNCTION__, array());
  $sections = &drupal_static(__FUNCTION__ . ':limit_validation_errors');
  if (isset($limit_validation_errors)) {
    $sections = $limit_validation_errors;
  }

  if (isset($name) && !isset($form[$name])) {
    $record = TRUE;
    if (isset($sections)) {
      // #limit_validation_errors is an array of "sections" within which user
      // input must be valid. If the element is within one of these sections,
      // the error must be recorded. Otherwise, it can be suppressed.
      // #limit_validation_errors can be an empty array, in which case all
      // errors are suppressed. For example, a "Previous" button might want its
      // submit action to be triggered even if none of the submitted values are
      // valid.
      $record = FALSE;
      foreach ($sections as $section) {
        // Exploding by '][' reconstructs the element's #parents. If the
        // reconstructed #parents begin with the same keys as the specified
        // section, then the element's values are within the part of
        // $form_state['values'] that the clicked button requires to be valid,
        // so errors for this element must be recorded. As the exploded array
        // will all be strings, we need to cast every value of the section
        // array to string.
        if (array_slice(explode('][', $name), 0, count($section)) === array_map('strval', $section)) {
          $record = TRUE;
          break;
        }
      }
    }
    if ($record) {
      $form[$name] = $message;
      if ($message) {
        drupal_set_message($message, 'error');
      }
    }
  }

  return $form;
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
