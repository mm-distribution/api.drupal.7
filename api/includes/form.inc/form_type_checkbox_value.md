# form_type_checkbox_value()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 2362–2388 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L2362-L2388)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function form_type_checkbox_value($element, $input = FALSE)
```

## Documentation

```text
Determines the value for a checkbox form element.

@param $form
  The form element whose value is being populated.
@param $input
  The incoming input to populate the form element. If this is FALSE,
  the element's default value should be returned.

@return
  The data that will appear in $form_state['values'] for this element, or
  nothing to use the default.
```

## Code

```php
function form_type_checkbox_value($element, $input = FALSE) {
  if ($input === FALSE) {
    // Use #default_value as the default value of a checkbox, except change
    // NULL to 0, because _form_builder_handle_input_element() would otherwise
    // replace NULL with empty string, but an empty string is a potentially
    // valid value for a checked checkbox.
    return isset($element['#default_value']) ? $element['#default_value'] : 0;
  }
  else {
    // Checked checkboxes are submitted with a value (possibly '0' or ''):
    // http://www.w3.org/TR/html401/interact/forms.html#successful-controls.
    // For checked checkboxes, browsers submit the string version of
    // #return_value, but we return the original #return_value. For unchecked
    // checkboxes, browsers submit nothing at all, but
    // _form_builder_handle_input_element() detects this, and calls this
    // function with $input=NULL. Returning NULL from a value callback means to
    // use the default value, which is not what is wanted when an unchecked
    // checkbox is submitted, so we use integer 0 as the value indicating an
    // unchecked checkbox. Therefore, modules must not use integer 0 as a
    // #return_value, as doing so results in the checkbox always being treated
    // as unchecked. The string '0' is allowed for #return_value. The most
    // common use-case for setting #return_value to either 0 or '0' is for the
    // first option within a 0-indexed array of checkboxes, and for this,
    // form_process_checkboxes() uses the string rather than the integer.
    return isset($input) ? $element['#return_value'] : 0;
  }
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
