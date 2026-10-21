# _form_button_was_clicked()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 2226–2244 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L2226-L2244)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function _form_button_was_clicked($element, &$form_state)
```

## Documentation

```text
Determines if a given button triggered the form submission.

This detects button controls that trigger a form submission by being clicked
and having the click processed by the browser rather than being captured by
JavaScript. Essentially, it detects if the button's name and value are part
of the POST data, but with extra code to deal with the convoluted way in
which browsers submit data for image button clicks.

This does not detect button clicks processed by Ajax (that is done in
_form_element_triggered_scripted_submission()) and it does not detect form
submissions from Internet Explorer in response to an ENTER key pressed in a
textfield (form_builder() has extra code for that).

Because this function contains only part of the logic needed to determine
$form_state['triggering_element'], it should not be called from anywhere
other than within the Form API. Form validation and submit handlers needing
to know which button was clicked should get that information from
$form_state['triggering_element'].
```

## Code

```php
function _form_button_was_clicked($element, &$form_state) {
  // First detect normal 'vanilla' button clicks. Traditionally, all
  // standard buttons on a form share the same name (usually 'op'),
  // and the specific return value is used to determine which was
  // clicked. This ONLY works as long as $form['#name'] puts the
  // value at the top level of the tree of $_POST data.
  if (isset($form_state['input'][$element['#name']]) && $form_state['input'][$element['#name']] == $element['#value']) {
    return TRUE;
  }
  // When image buttons are clicked, browsers do NOT pass the form element
  // value in $_POST. Instead they pass an integer representing the
  // coordinates of the click on the button image. This means that image
  // buttons MUST have unique $form['#name'] values, but the details of
  // their $_POST data should be ignored.
  elseif (!empty($element['#has_garbage_value']) && isset($element['#value']) && $element['#value'] !== '') {
    return TRUE;
  }
  return FALSE;
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
